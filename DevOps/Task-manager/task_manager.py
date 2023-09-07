import time

# Inisialisasi daftar tugas
daftar_tugas = []

# Fungsi untuk menambahkan tugas
def tambah_tugas(tugas):
    daftar_tugas.append(tugas)
    print("Tugas telah ditambahkan.")

# Fungsi untuk melihat daftar tugas
def lihat_tugas():
    if daftar_tugas:
        print("Daftar Tugas Anda:")
        for idx, tugas in enumerate(daftar_tugas, start=1):
            print(f"{idx}. {tugas}")
    else:
        print("Tidak ada tugas yang tersimpan.")

# Fungsi untuk menjalankan tugas
def jalankan_tugas():
    while True:
        lihat_tugas()
        pilihan = input("Pilih nomor tugas yang akan dijalankan (0 untuk kembali): ")
        
        if pilihan == '0':
            break
        elif pilihan.isdigit():
            index_tugas = int(pilihan) - 1
            if 0 <= index_tugas < len(daftar_tugas):
                print(f"Menjalankan tugas: {daftar_tugas[index_tugas]}")
                # Simulasi menjalankan tugas (anda bisa menambahkan kode sesuai kebutuhan)
                time.sleep(2)
                print(f"Tugas selesai: {daftar_tugas[index_tugas]}")
            else:
                print("Nomor tugas tidak valid.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menampilkan menu
while True:
    print("\nMenu Pengelola Tugas DevOps:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Jalankan Tugas")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1/2/3/4): ")

    if pilihan == '1':
        tugas_baru = input("Masukkan deskripsi tugas: ")
        tambah_tugas(tugas_baru)
    elif pilihan == '2':
        lihat_tugas()
    elif pilihan == '3':
        jalankan_tugas()
    elif pilihan == '4':
        print("Terima kasih! Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
