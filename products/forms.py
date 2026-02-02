from django import forms
from .models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        widgets = {
            'nama_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

    # Custom Validation: Harga harus angka (sudah otomatis) & wajib isi
    def clean_harga(self):
        harga = self.cleaned_data.get('harga')
        if harga is None:
            raise forms.ValidationError("Harga wajib diisi.")
        if harga < 0:
            raise forms.ValidationError("Harga tidak boleh negatif.")
        return harga