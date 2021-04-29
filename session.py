import preparation
import function

def Judul():
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ ")
    print("|     __ __            __                       ___      _       _ __   |")
    print("|    / //_/___ _____  / /_____  ____  ____ _   /   |    (_)___ _(_) /_  |")
    print("|   / ,< / __ `/ __ \/ __/ __ \/ __ \/ __ `/  / /| |   / / __ `/ / __ \ |")
    print("|  / /| / /_/ / / / / /_/ /_/ / / / / /_/ /  / ___ |  / / /_/ / / /_/ / |")
    print("| /_/ |_\__,_/_/ /_/\__/\____/_/ /_/\__, /  /_/  |_|_/ /\__,_/_/_.___/  |")
    print("|                                  /____/         /___/                 |")
    print("|__ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __|")

def LoadData():
    #baru printnya aja
    print("Loading...")
    print("Memasukkan File User : user.csv")
    print("Memasukkan File Gadget : gadget.csv")
    print("Memasukkan File Consumable : consumable.csv")
    print("Memasukkan File Gadget Borrow History : gadget_borrow_history.csv")
    print("Memasukkan File Gadget Return History : gadget_return_history.csv")
    print("Memasukkan File Consumable_history : consumable_history.csv")
    print("Semua data sudah di-load")
    print()

def Help(menu):
    print("               __________________                ")
    print("              |      __      __  |               ")
    print("              | |__||__ |   |__| |               ")
    print("              | |  ||__ |__ |    |               ")
    print("              |__________________|               ")
    print()

    if menu=="awal":
        print("======================================================")
        print("register - Registrasi user baru")
        print("login    - Login untuk menggunakan aplikasi")
        print("help     - Bantuan berupa list perintah yang tersedia")
        print("exit     - Keluar dari aplikasi")
        print("======================================================")
    elif menu=="admin":
        print("================================================================")
        print("register         - Registrasi user baru")
        print("carirarity       - Mencari gadget berdasarkan rarity-nya")
        print("caritahun        - Mencari gadget berdasarkan tahun ditemukannya")
        print("tambahitem       - Menambahkan item ke dalam inventori")
        print("hapusitem        - Menghapus item dari inventori")
        print("ubahjumlah       - Mengubah jumlah item yang ada di inventori")
        print("riwayatpinjam    - Melihat riwayat peminjaman gadget")
        print("riwayatkembali   - Melihat riwayat pengembalian gadget")
        print("riwayatambil     - Melihat riwayat pengambilan consumable")
        print("save             - Menyimpan perubahan data setelah pemakaian")
        print("help             - Bantuan berupa list perintah yang tersedia")
        print("exit             - Keluar dari aplikasi")
        print("================================================================")
    elif menu=="user":
        print("================================================================")
        print("carirarity       - Mencari gadget berdasarkan rarity-nya")
        print("caritahun        - Mencari gadget berdasarkan tahun ditemukannya")
        print("pinjam           - Meminjam gadget")
        print("kembalikan       - Mengembalikan gadget")
        print("minta            - Meminta consumable")
        print("save             - Menyimpan perubahan data setelah pemakaian")
        print("help             - Bantuan berupa list perintah yang tersedia")
        print("exit             - Keluar dari aplikasi")
        print("================================================================")
    print()    


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

def printGroupHistory(j,k,l,arr,arr1,arr2):
    if arr[j][2][0] =='G':
        print("ID Peminjaman       : ", arr[j][0])
        print("Nama Pengambil      : ", arr2[l][2])
        print("Nama Gadget         : ", arr1[k][1])
        print("Tanggal Peminjaman  : ", arr[j][3])
        print("Jumlah              : ", arr[j][4])
        print()
    elif arr[j][2][0] =='C':
        print("ID Pengambilan       : ", arr[j][0])
        print("Nama Pengambil       : ", arr2[l][2])
        print("Nama consumable      : ", arr1[k][1])
        print("Tanggal Pengambilan  : ", arr[j][3])
        print("Jumlah               : ", arr[j][4])
        print()
    else:
        print("ID Pengembalian       : ", arr[j][0])
        print("Nama Pengambil        : ", arr2[l][2])
        print("Nama Gadget           : ", arr1[k][1])
        print("Tanggal Pengembalian  : ", arr[j][2])
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
def showHistory(arr,arr1,arr2):
    n = len(arr)
    o = len(arr1)
    p = len(arr2)
    urutan=['' for i in range (n-1)]
    for i in range(1,n):
        urutan[i-1]=arr[i][3]
    urutan.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    urutan=list(dict.fromkeys(urutan))
    jumlah=0
    for i in range(n-1):
        for j in range (1,n):
            for k in range (1,o):
                for l in range (1,p):
                        if jumlah==5:
                            break
                        elif urutan[i]==arr[j][3] and arr1[k][0]==arr[j][2] and arr2[l][0]==arr[j][1]:
                            printGroupHistory(j,k,l,arr,arr1,arr2)
                            jumlah=jumlah+1

def showReturnHistory(arr,arr1,arr2,arr3):
    n = len(arr)
    o = len(arr1)
    p = len(arr2)
    q = len(arr3)
    urutan=['' for i in range (n-1)]
    for i in range(1,n):
        urutan[i-1]=arr[i][2]
    urutan.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y'))
    urutan=list(dict.fromkeys(urutan))
    jumlah=0
    for i in range(n-1):
        for j in range (1,n):
            for k in range (1,o):
                for l in range (1,p):
                    for m in range (1,q):
                        if jumlah==5:
                            break
                        elif urutan[i]==arr[j][2] and arr1[k][0]==arr[j][1] and arr2[l][0]==arr1[j][2] and arr3[m][0]==arr1[k][1]:
                            printGroupHistory(j,l,m,arr,arr2,arr3)
                            jumlah=jumlah+1

def returnGadget(array_of_gadget,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_user,idx):
    print("Berikut adalah daftar gadget yang Anda harus kembalikan: ")
    l = len(array_of_gadget)
    m = len(array_of_gadget_borrow_history)
    n = len(array_of_gadget_return_history)
    no = 0
    listgadget = []
    jumlahpinjam = []
    id_borrow = []
    flag = 0
    flag1 = 0
    same = 0
    belumdikembalikan = 0

    while flag == 0:
        for i in range (1,m,1):
            if array_of_gadget_borrow_history[i][1] == array_of_user[idx][0]:
                if array_of_gadget_borrow_history[i][5] == "FALSE":
                    no = no + 1 
                    id_borrow.append(array_of_gadget_borrow_history[i][0])
                    if no > 0:
                        for j in range (1,l,1):
                            if array_of_gadget_borrow_history[i][2] == array_of_gadget[j][0]:
                                jumlahpinjam.append(array_of_gadget_borrow_history[i][4])
                                listgadget.append(array_of_gadget[j][1])
                                print( str(no) + ". " + array_of_gadget[j][1])
                    flag = flag + 1
                    belumdikembalikan += 1
                elif array_of_gadget_borrow_history[i][5] == "TRUE":
                    flag = flag + 1
    
    if belumdikembalikan == 0:
        print("------------------------------------------------------")
        print("Anda sudah mengembalikan semua gadget yang Anda pinjam")
        print("------------------------------------------------------")
    else:
        while flag1 == 0:
            namagadget = input("Masukkan nama gadget yang ingin Anda kembalikan: ")
            tanggal = input("Tanggal pengembalian: ")
            for i in range (no):
                if namagadget == listgadget[i]:
                    index = i
                    idpinjam = id_borrow[i]
                    jumlah = jumlahpinjam[i]
                    same = same + 1
                    posisi = function.getposisi(namagadget,array_of_gadget,1)
                    posisi1 = function.getposisi(idpinjam, array_of_gadget_borrow_history, 0)
                    preparation.updateborrowhistory(posisi1, array_of_gadget_borrow_history)
                    preparation.updategadgetreturn(jumlah, posisi, array_of_gadget)
                    data_baru = [str(n), array_of_user[idx][0], tanggal]
                    array_of_gadget_return_history.append(data_baru)
                    string_data = preparation.convertArrayToString(array_of_gadget_return_history)
                    f = open("./csv_file/gadget_return_history.csv", "w")
                    f.write(string_data)
                    f.close()
            if same > 0:
                print("Item " + str(namagadget) + " (x" + str(jumlahpinjam[index]) + ") telah dikembalikan")
                flag1 = flag1 + 1
            elif same == 0:
                print("Anda memasukkan input yang salah")
                flag1 = flag1 + 1

def mintaConsumable(array_of_consumable, array_of_consumable_history, array_of_user, idx):
    n = len(array_of_consumable)
    m = len(array_of_consumable_history)
    id_item = input("Masukkan id item: ")
    
    if function.idItemIsValid(id_item):
        for i in range (1,n,1):
            if id_item == array_of_consumable[i][0]:
                posisi = i
                break
        tanggal = input("Tanggal Peminjaman(dd/mm/yyyy): ")
        jumlah = int(input("Jumlah: "))

        if 0 < jumlah :
            if jumlah <= int(array_of_consumable[posisi][3]) and int(array_of_consumable[posisi][3]) > 0:
                print("Item " + array_of_consumable[posisi][1] + "(x" + str(jumlah) + ") telah berhasil diambil!")
                array_of_consumable[posisi][3] = int(array_of_consumable[posisi][3]) -jumlah
                string = preparation.convertArrayToString(array_of_consumable)
                f = open("./csv_file/consumable.csv", "w")
                f.write(string)
                f.close()
                data_baru = [str(m), array_of_user[idx][0], id_item, tanggal, str(jumlah)]
                array_of_consumable_history.append(data_baru)
                string_data = preparation.convertArrayToString(array_of_consumable_history)
                f = open("./csv_file/consumable_history.csv", "w")
                f.write(string_data)
                f.close()
            else:
                print("Persediaan consumable tidak mencukupi") 
        else:
            print("Harap masukkan jumlah dengan benar")
    else: 
        print("ID item salah, harap masukkan id item dengan benar")