# Membaca tinggi segitiga dari pengguna
tinggi = int(input("Masukkan tinggi segitiga: "))

# Membuat segitiga bintang siku-siku
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end="")
    print()