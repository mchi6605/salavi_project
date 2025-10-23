from django.shortcuts import render, get_object_or_404, redirect
from .models import SanPham
from .forms import SanPhamForm
def sanpham_list(request):
    search = request.GET.get("q", "").strip().lower()
    tinh_trang = request.GET.get("tinh_trang", "").strip().lower()
    sanphams = []

    for sp in SanPham.objects.all():
        ma = (sp.ma_hang_hoa or "").lower()
        ten = (sp.ten_hang_hoa or "").lower()
        nhom = (sp.nhom_hang or "").lower()
        tt = (sp.tinh_trang or "").lower()

        if (not search or any(word in ma or word in ten or word in nhom for word in search.split())) \
           and (not tinh_trang or tinh_trang == tt):
            sanphams.append(sp)

    return render(request, "sanpham/list.html", {
        "sanphams": sanphams,
        "search_text": request.GET.get("q", ""),
        "tinh_trang": request.GET.get("tinh_trang", ""),
    })


def sanpham_add(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sanpham:list')
    else:
        form = SanPhamForm()
    return render(request, 'sanpham/form_add.html', {'form': form})

def sanpham_edit(request, pk):
    sanpham = get_object_or_404(SanPham, pk=pk)
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES, instance=sanpham)
        if form.is_valid():
            form.save()
            return redirect('sanpham:list')
    else:
        form = SanPhamForm(instance=sanpham)
    return render(request, 'sanpham/form_update.html', {'form': form, 'sanpham': sanpham})

def sanpham_delete(request, pk):
    sanpham = get_object_or_404(SanPham, pk=pk)
    sanpham.delete()
    return redirect('sanpham:list')


