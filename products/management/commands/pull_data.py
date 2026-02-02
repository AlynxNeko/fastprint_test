import requests
import hashlib
from datetime import datetime
from django.core.management.base import BaseCommand
from products.models import Produk, Kategori, Status
import pytz

class Command(BaseCommand):
    help = 'Tarik data dari API FastPrint'

    def handle(self, *args, **kwargs):
        # Set timezone to Asia/Jakarta (FastPrint server is likely there)
        tz = pytz.timezone('Asia/Jakarta')
        now = datetime.now(tz)

        username = f"tesprogrammer{now.strftime('%d%m%y')}C{now.strftime('%H')}"

        # 2. PASSWORD: bisacoding-d-m-y
        # Removing leading zeros manually to be safe
        raw_password = f"bisacoding-{now.strftime('%d')}-{now.strftime('%m')}-{now.strftime('%y')}"
        password = hashlib.md5(raw_password.encode()).hexdigest()


        self.stdout.write(f"Auth Attempt: {username} | {raw_password}")

        # 3. REQUEST WITH HEADERS
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        payload = {'username': username, 'password': password}
        
        # Adding a User-Agent is sometimes necessary for some PHP-based APIs
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        try:
            r = requests.post(url, data=payload, headers=headers)
            # The API might return 200 even on auth failure, check the JSON
            response_json = r.json()
            if response_json.get('error') == 0:
                for item in response_json['data']:
                    # 1. Get or Create Category & Status
                    kat_obj, _ = Kategori.objects.get_or_create(nama_kategori=item['kategori'])
                    stat_obj, _ = Status.objects.get_or_create(nama_status=item['status'])

                    # 2. Clean Price
                    try:
                        harga_clean = int(item['harga'])
                    except (ValueError, TypeError):
                        harga_clean = 0

                    # 3. Save Product
                    Produk.objects.update_or_create(
                        id_produk=item['id_produk'],
                        defaults={
                            'nama_produk': item['nama_produk'],
                            'harga': harga_clean,
                            'kategori': kat_obj,
                            'status': stat_obj
                        }
                    )
            else:
                self.stdout.write(self.style.ERROR(f"Gagal: {response_json['ket']}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error koneksi: {e}"))