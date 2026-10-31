while True:
    try:
        angka = int(input("Masukan Angka : "))
    except ValueError:
        print("Input Wajib Menggunakan Angka")
        angka = int(input("Masukan Angka : "))
    else:
        print("Input Berhasil")
    finally:
        print(f"Bilangan yang anda masukan adalah {angka}")
    break