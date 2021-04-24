def introSession():
    print("Pilih role:\n1. Admin\n2. User")

def adminSession():
    print("1. Daftarkan User")

def userSession():
    print("1. Cari Item Berdasarkan Rarity")

def findGadgetByRarity(rarity, array_of_gadget):
    n = len(array_of_gadget)
    for i in range(n):
        if array_of_gadget[i][4] == rarity:
            print("Nama             : ", array_of_gadget[i][1])
            print("Deskripsi        : ", array_of_gadget[i][2])
            print("Jumlah           : ", array_of_gadget[i][3], " buah")
            print("Rarity           : ", array_of_gadget[i][4])
            print("Tahun Ditemukan  : ", array_of_gadget[i][5])
            print()