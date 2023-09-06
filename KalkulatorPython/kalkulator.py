# Fungsi penjumlahan
def tambah(x, y):
    return x + y

# Fungsi pengurangan
def kurang(x, y):
    return x - y

# Fungsi perkalian
def kali(x, y):
    return x * y

# Fungsi pembagian
def bagi(x, y):
    if y == 0:
        return "Tidak bisa membagi dengan nol"
    return x / y

# Menampilkan menu
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

# Meminta input dari pengguna
pilihan = input("Masukkan nomor operasi yang dipilih (1/2/3/4): ")

# Meminta input angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Melakukan operasi berdasarkan pilihan
if pilihan == '1':
    print("Hasil penjumlahan:", tambah(angka1, angka2))
elif pilihan == '2':
    print("Hasil pengurangan:", kurang(angka1, angka2))
elif pilihan == '3':
    print("Hasil perkalian:", kali(angka1, angka2))
elif pilihan == '4':
    print("Hasil pembagian:", bagi(angka1, angka2))
else:
    print("Input tidak valid")

