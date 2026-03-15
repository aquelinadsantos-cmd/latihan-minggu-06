def perkalian(a, b):
    hasil = 0

    for i in range(a):
        hasil = hasil + b

    return hasil


# program utama
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hasil = perkalian(angka1, angka2)

print("Hasil perkalian:", hasil)