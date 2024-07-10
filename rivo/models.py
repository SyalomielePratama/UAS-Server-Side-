from django.db import models

class JenisProduk(models.Model):
    jenis = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='jenis_gambar/', blank=True, null=True)

    def __str__(self):
        return self.jenis

class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    gambar = models.ImageField(upload_to='produk_gambar/')
    stok = models.PositiveIntegerField()
    jenis_produk = models.ForeignKey(JenisProduk, on_delete=models.CASCADE, related_name='produks')

    def __str__(self):
        return self.nama_produk

class Feedback(models.Model):
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f"{self.nama} - {self.email}"