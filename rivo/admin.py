from django.contrib import admin
from .models import JenisProduk, Produk
from .models import Feedback

@admin.register(JenisProduk)
class JenisProdukAdmin(admin.ModelAdmin):
    list_display = ('jenis', 'deskripsi')

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama_produk', 'harga', 'rating', 'stok', 'jenis_produk')
    list_filter = ('jenis_produk',)
    search_fields = ('nama_produk',)

admin.site.register(Feedback)