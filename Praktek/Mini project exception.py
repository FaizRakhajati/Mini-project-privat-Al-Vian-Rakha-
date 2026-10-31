
try:
   with open("FileMateri09.csv","r") as filebaru :
    pass
except FileNotFoundError:
    print("File tidak ada")
else:
    print("File Ada")
finally:
    print("Selesai")