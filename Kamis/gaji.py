gaji = float(input("\nMasukan gaji: "))

tunjangan = 20 % gaji
pajak = 15% (tunjangan*gaji)
gaji_bersih = gaji + tunjangan - pajak

print("\nGaji Bersih \t\t:",gaji_bersih)