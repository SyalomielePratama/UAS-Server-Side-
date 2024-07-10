from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('kontak/', views.kontak, name='kontak'),
    path('produk/', views.produk , name='produk'),
    path('', views.home , name='home'),
    path('crud/', views.crud, name='crud'),
    path('crudfeed/', views.crudfeed, name='crudfeed'),
    path('addbrg/', views.tambah_produk, name='tambah_produk'),
    path('hapus/<int:id_produk>/', views.hapus_produk, name='hapus_produk'),
    path('ubah_brg/<int:id_produk>/', views.ubah_produk, name='ubah_produk'),
    path('hapus_feedback/<int:id_feedback>/', views.hapus_feedback, name='hapus_feedback'),
    path('ubah_feedback/<int:id_feedback>/', views.ubah_feedback, name='ubah_feedback'),
    path('tambah_feedback/', views.tambah_feedback, name='tambah_feedback')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)