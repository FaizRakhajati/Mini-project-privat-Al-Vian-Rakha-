pilihan = input("Masukkan pilihan: \nA. Persegi panjang \nB.Segitiga \n")
if pilihan == "A":
  panjang = float(input("Masukkan panjang: "))
  lebar = float(input("Masukkan lebar: "))
  nilai = panjang*lebar
  print("luasnya :", nilai)
elif pilihan == "B":
  alas = float(input("Masukkan panjang alas: "))
  tinggi = float(input("Masukkan tinggi: "))
  nilai = 1/2*alas*tinggi
  print("luasnya : ", nilai)