# forms.py
from django import forms
from .models import Feedback,Produk

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nama', 'email', 'feedback']

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

        # widgets = {
        #     'nama_produk': forms.TextInput({'class':'form-control'}),
        #     'harga': forms.NumberInput({'class':'form-control'}),
        #     'rating': forms.NumberInput({'class':'form-control'}),
        #     'gambar': forms.FileInput({'class':'form-control'}),
        #     'jenis_produk': forms.Select({'class':'form-control'}),
        # }