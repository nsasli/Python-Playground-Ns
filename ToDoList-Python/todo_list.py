# Membuat daftar tugas kosong
to_do_list = []

# Fungsi untuk menambahkan tugas
def tambah_tugas(tugas):
    to_do_list.append(tugas)
    print("Tugas ditambahkan:", tugas)

# Fungsi untuk melihat daftar tugas
def lihat_tugas():
    print("Daftar Tugas:")
    for idx, tugas in enumerate(to_do_list, start=1):
        print(f"{idx}. {tugas}")

# Fungsi untuk menghapus tugas
def hapus_tugas(index):
    if 1 <= index <= len(to_do_list):
        removed_task = to_do_list.pop(index - 1)
        print(f"Tugas dihapus: {removed_task}")
    else:
        print("Indeks tidak valid")

# Menampilkan menu
while True:
    print("\nMenu:")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1/2/3/4): ")

    if pilihan == '1':
        tugas_baru = input("Masukkan tugas baru: ")
        tambah_tugas(tugas_baru)
    elif pilihan == '2':
        lihat_tugas()
    elif pilihan == '3':
        index_hapus = int(input("Masukkan indeks tugas yang akan dihapus: "))
        hapus_tugas(index_hapus)
    elif pilihan == '4':
        print("Terima kasih! Selamat tinggal!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
