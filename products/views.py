from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm

# 1. READ (Hanya status "bisa dijual")
def produk_list(request):
    # Filter case-insensitive
    produks = Produk.objects.filter(status__nama_status__iexact='bisa dijual')
    return render(request, 'products/list.html', {'produks': produks})

# 2. CREATE
def produk_create(request):
    if request.method == 'POST':
        form = ProdukForm(request.POST)
        if form.is_valid():
            # Kita perlu generate ID manual karena API pakai ID integer
            # Cara simple: ambil ID terakhir + 1
            last_id = Produk.objects.order_by('-id_produk').first().id_produk
            obj = form.save(commit=False)
            obj.id_produk = last_id + 1
            obj.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
    return render(request, 'products/form.html', {'form': form, 'title': 'Tambah Produk'})

# 3. UPDATE
def produk_edit(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    if request.method == 'POST':
        form = ProdukForm(request.POST, instance=produk)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=produk)
    return render(request, 'products/form.html', {'form': form, 'title': 'Edit Produk'})

# 4. DELETE
def produk_delete(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    return redirect('produk_list')