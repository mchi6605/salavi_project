from django.db import models

class SanPham(models.Model):
    ma_hang_hoa = models.CharField(max_length=8,unique=True, editable=False)
    stt = models.IntegerField(editable=False)
    ten_hang_hoa = models.CharField(max_length=255)
    nhom_hang = models.CharField(max_length=100)
    hinh_anh = models.ImageField(upload_to='sanpham/', blank=True, null=True)
    mau_sac = models.CharField(max_length=100)
    kich_co = models.CharField(max_length=100)
    chat_lieu = models.CharField(max_length=100)
    don_vi_tinh = models.CharField(max_length=10)
    don_gia = models.DecimalField(max_digits=10, decimal_places=2)
    ghi_chu =models.TextField(null=True)
    TINH_TRANG_CHOICES = [('CONNHIEU', 'Còn nhiều'),
                    ('SAPHET', 'Sắp hết'),
                    ('HET', 'Hết'), ]
    tinh_trang = models.CharField(choices=TINH_TRANG_CHOICES, max_length=20)
    ton_kho = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.stt:
            last_item = SanPham.objects.all().order_by('stt').last()
            if last_item:
                self.stt = last_item.stt + 1
            else:
                self.stt = 1

        if self.ton_kho <= 0:
            self.tinh_trang = 'HET'
        elif self.ton_kho < 8:
            self.tinh_trang = 'SAPHET'
        else:
            self.tinh_trang = 'CONNHIEU'

        if not self.ma_hang_hoa:
            prefix = "SP"
            last_sp = SanPham.objects.all().order_by('id').last()
            next_id = (last_sp.id + 1) if last_sp else 1
            self.ma_hang_hoa = f"{prefix}{next_id:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ma_hang_hoa} - {self.ten_hang_hoa}"