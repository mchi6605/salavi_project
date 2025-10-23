from django.contrib import admin
from .models import SanPham

@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('ma_hang_hoa', 'ten_hang_hoa', 'nhom_hang', 'mau_sac', 'kich_co', 'don_vi_tinh', 'don_gia', 'tinh_trang', 'ton_kho')
    readonly_fields = ('tinh_trang',)
    list_filter = ('nhom_hang', 'ten_hang_hoa', 'tinh_trang')
    search_fields = ('ma_hang_hoa', 'ten_hang_hoa','tinh_trang','nhom_hang')
    list_editable = ('tinh_trang', 'ton_kho')
    ordering = ('ma_hang_hoa',)
    list_per_page = 20
