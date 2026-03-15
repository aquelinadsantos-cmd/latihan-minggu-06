jumlah = int(input("Masukkan jumlah mata kuliah: "))

total_nilai = 0

for i in range(jumlah):
    nilai = input("Masukkan nilai (A/B/C/D): ")

    if nilai == "A":
        bobot = 4
    elif nilai == "B":
        bobot = 3
    elif nilai == "C":
        bobot = 2
    elif nilai == "D":
        bobot = 1
    else:
        bobot = 0

    total_nilai = total_nilai + bobot


ips = total_nilai / jumlah

print("IPS anda adalah:", ips)