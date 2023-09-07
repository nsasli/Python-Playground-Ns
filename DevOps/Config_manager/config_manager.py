import os
import shutil
import json

# Nama berkas konfigurasi
CONFIG_FILE = 'config.json'

# Fungsi untuk membuat konfigurasi awal
def buat_konfigurasi_awal():
    konfigurasi_awal = {
        'nama': 'DevOps Engineer',
        'proyek': 'Manajemen Konfigurasi dengan Python',
        'versi': '1.0'
    }
    with open(CONFIG_FILE, 'w') as file:
        json.dump(konfigurasi_awal, file)
    print('Konfigurasi awal telah dibuat.')

# Fungsi untuk menampilkan konfigurasi
def tampilkan_konfigurasi():
    try:
        with open(CONFIG_FILE, 'r') as file:
            konfigurasi = json.load(file)
            print('Konfigurasi Anda:')
            for key, value in konfigurasi.items():
                print(f'{key}: {value}')
    except FileNotFoundError:
        print('Konfigurasi tidak ditemukan.')

# Fungsi untuk membuat salinan cadangan konfigurasi
def buat_cadangan():
    if os.path.exists(CONFIG_FILE):
        shutil.copy(CONFIG_FILE, 'config_backup.json')
        print('Salinan cadangan konfigurasi telah dibuat.')
    else:
        print('Konfigurasi tidak ditemukan.')

# Fungsi untuk memulihkan konfigurasi dari cadangan
def pulihkan_konfigurasi():
    if os.path.exists('config_backup.json'):
        shutil.copy('config_backup.json', CONFIG_FILE)
        print('Konfigurasi telah dipulihkan dari salinan cadangan.')
    else:
        print('Salinan cadangan tidak ditemukan.')

# Menampilkan menu
while True:
    print('\nMenu Manajemen Konfigurasi:')
    print('1. Buat Konfigurasi Awal')
    print('2. Tampilkan Konfigurasi')
    print('3. Buat Salinan Cadangan')
    print('4. Pulihkan Konfigurasi dari Cadangan')
    print('5. Keluar')

    pilihan = input('Pilih opsi (1/2/3/4/5): ')

    if pilihan == '1':
        buat_konfigurasi_awal()
    elif pilihan == '2':
        tampilkan_konfigurasi()
    elif pilihan == '3':
        buat_cadangan()
    elif pilihan == '4':
        pulihkan_konfigurasi()
    elif pilihan == '5':
        print('Terima kasih! Sampai jumpa!')
        break
    else:
        print('Pilihan tidak valid. Silakan coba lagi.')
