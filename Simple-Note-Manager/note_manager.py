def tampilkan_catatan():
    try:
        with open("catatan.txt", "r") as file:
            catatan = file.read()
            print("Catatan Anda:")
            print(catatan)
    except FileNotFoundError:
        print("Tidak ada catatan yang tersimpan.")

def tambah_catatan():
    catatan_baru = input("Tambahkan catatan baru: ")
    with open("catatan.txt", "a") as file:
        file.write(catatan_baru + "\n")
    print("Catatan telah ditambahkan.")

def main():
    while True:
        print("\nPengelola Catatan Sederhana")
        print("1. Tampilkan Catatan")
        print("2. Tambahkan Catatan")
        print("3. Keluar")

        pilihan = input("Pilih opsi (1/2/3): ")

        if pilihan == '1':
            tampilkan_catatan()
        elif pilihan == '2':
            tambah_catatan()
        elif pilihan == '3':
            print("Terima kasih! Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
