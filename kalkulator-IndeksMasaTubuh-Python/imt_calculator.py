def hitung_bmi(berat, tinggi):
    tinggi_meter = tinggi / 100
    bmi = berat / (tinggi_meter ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurang Berat (Underweight)"
    elif 18.5 <= bmi < 24.9:
        return "Normal (Healthy Weight)"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Selamat datang di Kalkulator BMI (Indeks Massa Tubuh)")
    berat = float(input("Masukkan berat Anda (kg): "))
    tinggi = float(input("Masukkan tinggi Anda (cm): "))

    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)

    print(f"BMI Anda adalah {bmi:.2f}")
    print(f"Kategori BMI Anda: {kategori}")

if __name__ == "__main__":
    main()
