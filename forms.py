from django import forms
from .models import SanPham

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        exclude = ('ma_hang_hoa','tinh_trang',)
        widgets = {
            'don_vi_tinh': forms.TextInput(attrs={'placeholder': 'Chiếc/cái'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Gắn CSS class để tùy chỉnh
        self.fields['hinh_anh'].widget.attrs.update({'class': 'custom-image-field'})
