def adminSession():
    print("1. Daftarkan User\n2. Cari Item Berdasarkan Rarity\n3. Cari Item Berdasarkan Tahun\n4. Menambahkan Item\n5. Menghapus Item\n6. Mengubah Jumlah Item\n7. Riwayat Peminjaman Gadget\n8. Riwayat Pengembalian Gadget\n9. Riwayat Pengambilan Consumable")

def userSession():
    print("1. Cari Item Berdasarkan Rarity\n2. Cari Item Berdasarkan Tahun\n3. Peminjaman Gadget")

def printGroup(i,arr):
    if arr[i][0][0] == 'G':
        print("Type Item        :  Gadget")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print("Tahun Ditemukan  : ", arr[i][5])
        print()
    elif arr[i][0][0] == 'C':
        print("Type Item        :  Consumable")
        print("Nama             : ", arr[i][1])
        print("Deskripsi        : ", arr[i][2])
        print("Jumlah           : ", arr[i][3], "buah")
        print("Rarity           : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==5:
        print("ID Peminjaman       : ", arr[i][0])
        print("Nama Pengambil      : ", arr[i][1])
        print("Nama Gadget         : ", arr[i][2])
        print("Tanggal Peminjaman  : ", arr[i][3])
        print("Jumlah              : ", arr[i][4])
        print()
    elif arr[0][1] =='id_peminjam' and len(arr[0])==4:
        print("ID Pengembalian       : ", arr[i][0])
        print("Nama Pengambil        : ", arr[i][1])
        print("Nama Gadget           : ", arr[i][2])
        print("Tanggal Pengembalian  : ", arr[i][3])
        print()    
    elif arr[0][1] =='id_pengambil':
        print("ID Pengambilan       : ", arr[i][0])
        print("Nama Pengambil       : ", arr[i][1])
        print("Nama consumable      : ", arr[i][2])
        print("Tanggal Pengambilan  : ", arr[i][3])
        print("Jumlah               : ", arr[i][4])
        print()

def findGadgetByRarity(rarity, arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i][4] == rarity:
            printGroup(i,arr)

def findGadgetByYear(year, operator, arr):
    n = len(arr)
    for i in range(1,n):
        if operator == '=':
            if int(arr[i][5]) == year:
                printGroup(i, arr)
        elif operator == '<':
            if int(arr[i][5]) < year:
                printGroup(i, arr)
        elif operator == '>':
            if int(arr[i][5]) > year:
                printGroup(i, arr)    
        elif operator == '>=':
            if int(arr[i][5]) >= year:
                printGroup(i, arr)
        else:
            if int(arr[i][5]) <= year:
                printGroup(i, arr)

from datetime import datetime
def showHistory(arr):
    n = len(arr)
    urutan=['' for i in range (n-1)]
    for i in range(1,n):
        urutan[i-1]=arr[i][3]
    urutan.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    urutan=list(dict.fromkeys(urutan))
    k=0
    for i in range(n-1):
        for j in range (1,n):
            if k==5:
                break
            elif urutan[i]==arr[j][3]:
                printGroup(j,arr)
                k=k+1