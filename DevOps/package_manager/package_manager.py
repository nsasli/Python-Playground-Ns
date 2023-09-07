import subprocess

# Fungsi untuk menambahkan paket
def tambah_paket(paket):
    try:
        subprocess.check_call(["pip", "install", paket])
        print(f"Paket {paket} telah berhasil ditambahkan.")
    except Exception as e:
        print(f"Gagal menambahkan paket {paket}: {str(e)}")

# Fungsi untuk menghapus paket
def hapus_paket(paket):
    try:
        subprocess.check_call(["pip", "uninstall", paket, "-y"])
        print(f"Paket {paket} telah berhasil dihapus.")
    except Exception as e:
        print(f"Gagal menghapus paket {paket}: {str(e)}")

# Fungsi untuk memperbarui paket
def perbarui_paket(paket):
    try:
        subprocess.check_call(["pip", "install", "--upgrade", paket])
        print(f"Paket {paket} telah berhasil diperbarui.")
    except Exception as e:
        print(f"Gagal memperbarui paket {paket}: {str(e)}")

# Menampilkan menu
while True:
    print("\nMenu Manajemen Paket dan Dependencies:")
    print("1. Tambah Paket")
    print("2. Hapus Paket")
    print("3. Perbarui Paket")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1/2/3/4): ")

    if pilihan == '1':
        paket = input("Masukkan nama paket yang akan ditambahkan: ")
        tambah_paket(paket)
    elif pilihan == '2':
        paket = input("Masukkan nama paket yang akan dihapus: ")
        hapus_paket(paket)
    elif pilihan == '3':
        paket = input("Masukkan nama paket yang akan diperbarui: ")
        perbarui_paket(paket)
    elif pilihan == '4':
        print("Terima kasih! Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
