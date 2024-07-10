from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, JenisProduk, Feedback
from .forms import FeedbackForm, ProdukForm
from django.contrib import messages

def home(request):
    title = 'Home'
    produk_hero = Produk.objects.filter(nama_produk="Hero").first()
    best_sellers = Produk.objects.filter(nama_produk__in=["Regular Fit Long Sleeve Top", "Black Crop Tailored Jacket", "Textured Sunset Shirt"])
    produk_offer = Produk.objects.filter(nama_produk="Offer").first()
    jenis_designer = JenisProduk.objects.all()[:3]
    konteks = {
        'title': title,
        'produk_hero': produk_hero,
        'best_sellers': best_sellers,
        'produk_offer': produk_offer,
        'jenis_designer': jenis_designer
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(konteks, request))

def produk(request):
  title = 'Produk'
  excluded_products = ['Offer', 'Hero', 'Textured Sunset Shirt', 'Black Crop Tailored Jacket', 'Regular Fit Long Sleeve Top']
  produk_list = Produk.objects.exclude(nama_produk__in=excluded_products)
  konteks = {
    'title' : title,
    'produk_list': produk_list 
  }
  template = loader.get_template('product.html')
  return HttpResponse(template.render(konteks, request))

def kontak(request):
    title = 'Kontak'

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data formulir ke dalam database
            messages.success(request, 'Feedback anda terkirim, terima kasih!')
            return redirect('/about/#testimon')
    else:
        form = FeedbackForm()

    konteks = {
        'title': title,
        'form': form,  # Sertakan formulir dalam konteks
    }
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(konteks, request))

def about(request):
  title = 'About'
  feedback_list = Feedback.objects.order_by('-id')[:3]
  konteks = {
    'title' : title,
    'feedback_list': feedback_list
  }
  template = loader.get_template('about.html')
  return HttpResponse(template.render(konteks, request))

def crud(request):
    produk = Produk.objects.all()
    feed = Feedback.objects.all()
    title = 'View produk & Testimonial'
  
    konteks = {
        'produk': produk,
        'title': title,
        'feed': feed
    }

    return render(request, 'crud.html', konteks)

def crudfeed(request):
    feedback = Feedback.objects.all()
    title = 'View Testimonial'
  
    konteks = {
        'title': title,
        'feedback': feedback
    }

    return render(request, 'crudfeed.html', konteks)

def ubah_produk(request, id_produk):
    produk = Produk.objects.get(id=id_produk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES, instance=produk)  # Pass request.FILES here
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diubah")
            return redirect('ubah_produk', id_produk=id_produk)
    else:
        form = ProdukForm(instance=produk)
    
    konteks = {
        'form': form,
        'produk': produk
    }
    return render(request, 'ubah_produk.html', konteks)

def hapus_produk(request, id_produk):
    produk = get_object_or_404(Produk, id=id_produk)
    produk.delete()
    messages.success(request, "Produk berhasil dihapus")
    return redirect('crud')

def tambah_produk(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Ditambahkan")
            return redirect('tambah_produk')
    else:
        form = ProdukForm()

    konteks = {
        'form': form,
        'title': 'Tambah Barang'
    }

    return render(request, 'tambah_produk.html', konteks)


def tambah_feedback(request):
    feed = Feedback.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback berhasil ditambahkan.")
            return redirect('crudfeed')
    else:
        form = FeedbackForm()
    
    konteks = {
        'form': form,
        'feed': feed,
        'title': 'Tambah Feedback'
    }
    return render(request, 'tambah_feedback.html', konteks)

def hapus_feedback(request, id_feedback):
    feedback = get_object_or_404(Feedback, id=id_feedback)
    feedback.delete()
    messages.success(request, "Feedback berhasil dihapus.")
    return redirect('crudfeed')

def ubah_feedback(request, id_feedback):
    feedback = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            messages.success(request, "Feedback berhasil diubah.")
            return redirect('crudfeed')
    else:
        form = FeedbackForm(instance=feedback)
    
    konteks = {
        'form': form,
        'feedback': feedback,
        'title': 'ubah Feedback'
    }
    return render(request, 'ubah_feedback.html', konteks)
