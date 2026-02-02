from django.db import models

class Kategori(models.Model):
    # AutoField 'id' sudah otomatis dibuat Django
    nama_kategori = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_kategori

class Status(models.Model):
    nama_status = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_status

class Produk(models.Model):
    # Kita izinkan id di-set manual karena kita ambil ID dari API
    id_produk = models.IntegerField(primary_key=True) 
    nama_produk = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=15, decimal_places=0)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk