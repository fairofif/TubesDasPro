import preparation
import session
import function
import argparse
import sys
import os

### kantongajaib.py berfungsi sebagain "MAIN SESSION" dalam program ini

parser=argparse.ArgumentParser()
parser.add_argument('nama_folder')
try:
    args=parser.parse_args()
except:
    print("Tidak ada nama folder yang diberikan!")
    sys.exit()

for (root,dirs,files) in os.walk(sys.path[0], topdown=True):
    for folder in dirs:
        if folder == args.nama_folder:
            folderbaru=folder
            rootbaru=root
array_of_user = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"user.csv"))
array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
array_of_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
array_of_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
array_of_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
array_of_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
# load dibawah sebagai "Temp" untuk saved data
saved_data_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
saved_data_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
saved_data_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
saved_data_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
session.LoadData()
session.Judul()
print()
print("*__________________________________*")
print(' Selamat Datang di "Kantong Ajaib"')
print(' Semoga Aplikasi ini Bermanfaat ^_^')
print()
status_apps = True
while status_apps == True:
    print("*=======================================================*")
    print("Silakan masukkan perintah di antara pilihan di bawah ini.")
    print()
    print("                    *______________*")
    print("                    |  __________  |")
    print("                    | |          | |")
    print("                    | |login     | |")
    print("                    | |register  | |")
    print("                    | |help      | |")
    print("                    | |exit      | |")
    print("                    | |__________| |")
    print("                    |______________|")
    print()
    print("*=======================================================*")
    print()
    aksi = str(input("Masukkan perintah: "))
    while aksi!='register' and aksi!='login' and aksi!='help' and aksi!='exit':
        print("Maaf '"+aksi+"'"+" tidak ada dalam pilihan")
        print()
        aksi = str(input("Masukkan perintah: "))

    if aksi == "help":
        session.Help('awal')

    elif aksi == "register":
        print("<=============================================>")
        print("Silakan masukkan data sesuai yang diperintahkan")
        nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
        preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user,rootbaru,folderbaru)
        array_of_user = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"user.csv"))
        print("User "+ nama_register +" telah berhasil register ke dalam kantong ajaib")
        print("<=============================================>")
        print()
    
    elif aksi == "exit":
        print("----------------------Sampai Jumpa!----------------------")
        print("Terima kasih telah menggunakan aplikasi Kantong Ajaib >_<")
        status_apps = False

    elif aksi == "login":
        print("<=============================================>")
        print("Silakan masukkan data sesuai yang diperintahkan")
        # log in dan penentuan role berdasarkan username dan pass
        uname_form, password_form = function.loginForm()
        while function.loginIsTrue(uname_form, password_form, array_of_user) == False:
            print("Maaf, username atau password yang anda masukkan salah atau tidak ada dalam data kami")
            print()
            print("Silakan masukkan data lagi dengan benar")
            uname_form, password_form = function.loginForm()
        print("<=============================================>")
        print()
        role, idx_user = function.decideRoleAndGetIndex(uname_form, array_of_user)
        status_sesi = True
        
        # jika role sebagai admin
        if role == "admin":
            ## admin session (memilih aksi)
            print("Halo " + array_of_user[idx_user][1] + "! Senang bertemu kembali dengan Anda")
            while status_sesi == True:
                print("*================================================================*")
                print("Silakan masukkan perintah di antara pilihan di bawah ini")
                print()
                print("                *_______________________*")
                print("                |   _________________   |")
                print("                |  |                 |  |")
                print("                |  | register        |  |")
                print("                |  | carirarity      |  |")
                print("                |  | caritahun       |  |")
                print("                |  | tambahitem      |  |")
                print("                |  | hapusitem       |  |")
                print("                |  | ubahjumlah      |  |")
                print("                |  | riwayatpinjam   |  |")
                print("                |  | riwayatkembali  |  |")
                print("                |  | riwayatambil    |  |")
                print("                |  | help            |  |")
                print("                |  | save            |  |")
                print("                |  | exit            |  |")
                print("                |  |_________________|  |")
                print("                |_______________________|")
                print()
                print("*================================================================*")
                print()
                ## sesi admin (memilih aksi yang akan dilakukan)
                pilihan = str(input("Masukkan perintah: "))
                while pilihan!='register' and pilihan!='carirarity' and pilihan!='caritahun' and pilihan!='tambahitem' and pilihan!='hapusitem' and pilihan!='ubahjumlah' and pilihan!='riwayatpinjam' and pilihan!='riwayatkembali' and pilihan!='riwayatambil' and pilihan!='help' and pilihan != 'save' and pilihan!='exit':
                    print("Maaf '"+pilihan+"'"+" tidak ada dalam pilihan")
                    print()
                    pilihan = str(input("Masukkan perintah: "))
                print()
                
                if pilihan == "help":
                    session.Help('admin')
            
                ## aksi untuk menambahkan user baru (register)
                elif pilihan == "register":
                    print("<=============================================>")
                    print("Silakan masukkan data sesuai yang diperintahkan")
                    nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
                    preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user,rootbaru,folderbaru)
                    array_of_user = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"user.csv"))
                    print("User "+ nama_register +" telah berhasil register ke dalam kantong ajaib")
                    print("<=============================================>")
                    print()
                ## aksi untuk mencari gadget berdasarkan raritynya
                elif pilihan == "carirarity":
                    print("<=============================================>")
                    rarity = str(input("Masukkan rarity: "))
                    print()
                    print("Hasil Pencarian: ")
                    print()
                    session.findGadgetByRarity(rarity, array_of_gadget)
                    print("<=============================================>")
                    print()
                ## aksi untuk mencari gadget berdasarkan tahun dan operator
                elif pilihan == "caritahun":
                    print("<=============================================>")
                    year = int(input("Masukkan tahun: "))
                    operator = str(input("Masukkan kategori: "))
                    print()
                    print("Hasil Pencarian: ")
                    session.findGadgetByYear(year, operator, array_of_gadget)
                    print("<=============================================>")
                    print()
                ## aksi untuk menamahkan item baru ke dalam data
                elif pilihan == "tambahitem":
                    print("<=============================================>")
                    arr_input = function.addItemForm(array_of_gadget, array_of_consumable)
                    preparation.writeItemToData(arr_input, array_of_gadget, array_of_consumable, rootbaru,folderbaru)
                    if len(arr_input) == 6:  # kalo addnya gadget
                        array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                        print("Item telah berhasil ditambahkan ke database")
                    elif len(arr_input) == 5: # kalo addnya consumable
                        array_of_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                        print("Item telah berhasil ditambahkan ke database")
                    print("<=============================================>")
                    print()
                ## aksi untuk menghapus item
                elif pilihan == "hapusitem":
                    print("<=============================================>")
                    id_item = str(input("Masukan ID Item: "))
                    if function.idItemIsExist(id_item, array_of_gadget, array_of_consumable) == True:
                        if id_item[0] == 'G':
                            idx = function.getIdxOfItem(id_item, array_of_gadget)
                            aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_gadget[idx][1] + " (Y/N)? "))
                            if aksi == 'Y' or aksi == 'y':
                                preparation.deleteItemFromData(id_item, array_of_gadget, rootbaru,folderbaru)
                                array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                                print("item telah berhasil dihapus dari database")
                            else:
                                print("item tidak jadi dihapus")
                        else:
                            idx = function.getIdxOfItem(id_item, array_of_consumable)
                            aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_consumable[idx][1] + " (Y/N)? "))
                            if aksi == 'Y' or aksi == 'y':
                                preparation.deleteItemFromData(id_item, array_of_consumable, rootbaru,folderbaru)
                                array_of_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                                print("item telah berhasil dihapus dari database")
                            else:
                                print("item tidak jadi dihapus")
                    else:
                        print("Tidak ada item dengan ID tersebut.")
                    print("<=============================================>")
                    print()
                ## aksi untuk mengubah jumlah item
                elif pilihan == "ubahjumlah":
                    print("<=============================================>")
                    id_item = str(input("Masukan ID Item: "))
                    if function.idItemIsExist(id_item, array_of_gadget, array_of_consumable) == True:
                        jumlah = int(input("Masukan Jumlah: "))
                        ## untuk gadget id
                        if id_item[0] == 'G':
                            idx = function.getIdxOfItem(id_item, array_of_gadget)
                            if jumlah < 0:    
                                if (jumlah*(-1)) <= int(array_of_gadget[idx][3]):
                                    preparation.updateJumlahItem(jumlah, idx, array_of_gadget, rootbaru,folderbaru)
                                    array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                                else:
                                    print(str(jumlah*(-1)) + " " + array_of_gadget[idx][1] + " gagal dibuang karena stok kurang. Stok sekarang: " 
                                    + array_of_gadget[idx][3] + " (<" + str(jumlah*(-1)) + ")")
                            else:
                                preparation.updateJumlahItem(jumlah, idx, array_of_gadget, rootbaru,folderbaru)
                                array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                        ## untuk consumable id
                        else:
                            idx = function.getIdxOfItem(id_item, array_of_consumable)
                            if jumlah < 0:    
                                if (jumlah*(-1)) <= int(array_of_consumable[idx][3]):
                                    preparation.updateJumlahItem(jumlah, idx, array_of_consumable, rootbaru,folderbaru)
                                    array_of_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                                else:
                                    print(str(jumlah*(-1)) + " " + array_of_consumable[idx][1] + " gagal dibuang karena stok kurang. Stok sekarang: " 
                                    + array_of_consumable[idx][3] + " (<" + str(jumlah*(-1)) + ")")
                            else:
                                preparation.updateJumlahItem(jumlah, idx, array_of_consumable, rootbaru,folderbaru)
                                array_of_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                    else:
                        print("Tidak ada item dengan ID tersebut.")
                    print("<=============================================>")
                    print()
                ## aksi untuk melihat riwayat peminjaman
                elif pilihan == "riwayatpinjam":
                    print("<=============================================>")
                    if len(array_of_gadget_borrow_history)==1:
                        print("tidak ada riwayat")
                    else:
                        session.showHistory(array_of_gadget_borrow_history,array_of_gadget,array_of_user)
                        print("ingin menambah entry lagi (Y/N)?")
                        aksi=str(input())
                        if aksi == 'Y' or aksi == 'y':
                            array_baru=function.delArray(array_of_gadget_borrow_history)
                            while array_baru!=[] and (aksi == 'Y' or aksi == 'y'):
                                session.showHistory(array_baru,array_of_gadget,array_of_user)
                                print("ingin menambah entry lagi (Y/N)?")
                                aksi=str(input())
                                array_baru=function.delArray(array_baru)
                            if array_baru==[] and (aksi == 'Y' or aksi == 'y'):
                                print("Data sudah habis")
                            else:
                                print("selesai")
                        else:
                            print("selesai")
                    print("<=============================================>")
                    print()
                ## aksi untuk melihat riwayat pengembalian    
                elif pilihan == "riwayatkembali":
                    print("<=============================================>")
                    if len(array_of_gadget_return_history)==1:
                        print("tidak ada riwayat")
                    else:
                        session.showReturnHistory(array_of_gadget_return_history,array_of_gadget_borrow_history,array_of_gadget,array_of_user)
                        print("ingin menambah entry lagi (Y/N)?")
                        aksi=str(input())
                        if aksi == 'Y' or aksi == 'y':
                            array_baru=function.delArray(array_of_gadget_return_history)
                            while array_baru!=[] and (aksi == 'Y' or aksi == 'y'):
                                session.showReturnHistory(array_baru,array_of_gadget_borrow_history,array_of_gadget,array_of_user)
                                print("ingin menambah entry lagi (Y/N)?")
                                aksi=str(input())
                                array_baru=function.delArray(array_baru)
                            if array_baru==[] and (aksi == 'Y' or aksi == 'y'):
                                print("data sudah habis")
                            else:
                                print("selesai")
                        else:
                            print("selesai")
                    print("<=============================================>")
                    print()
                ## aksi untuk melihat riwayat pengambilan consumable
                elif pilihan == "riwayatambil":
                    print("<=============================================>")
                    if len(array_of_consumable_history)==1:
                        print("tidak ada riwayat")
                    else:
                        session.showHistory(array_of_consumable_history,array_of_consumable,array_of_user)
                        print("ingin menambah entry lagi (Y/N)?")
                        aksi=str(input())
                        if aksi == 'Y' or aksi == 'y':
                            array_baru=function.delArray(array_of_consumable_history)
                            while array_baru!=[] and (aksi == 'Y' or aksi == 'y'):
                                session.showHistory(array_baru,array_of_consumable,array_of_user)
                                print("ingin menambah entry lagi (Y/N)?")
                                aksi=str(input())
                                array_baru=function.delArray(array_baru)
                            if array_baru==[] and (aksi == 'Y' or aksi == 'y'):
                                print("data sudah habis")
                            else:
                                print("selesai")
                        else:
                            print("selesai")
                    print("<=============================================>")
                    print()
                elif pilihan == "exit":
                    print("<=============================================>")
                    list1 = [saved_data_gadget,saved_data_consumable,saved_data_gadget_borrow_history,saved_data_gadget_return_history,saved_data_consumable_history]
                    list2 = [array_of_gadget,array_of_consumable,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_consumable_history]
                    
                    count_udah_kondisi_baru = 0
                    for i in range(len(list1)):
                        if list1[i] == list2[i]:
                            count_udah_kondisi_baru += 1
                    
                    if count_udah_kondisi_baru == 5: # kondisi kalo saved_data udah kondisi terbaru semua, bisa langsung exit
                        print("----------------------Sampai Jumpa!----------------------")
                        print("Terima kasih telah menggunakan aplikasi Kantong Ajaib >_<")
                        status_sesi = False
                        status_apps = False

                    else:
                        aksi = str(input("Data perubahan terakhir belum disave, save sekarang (Y/N)? "))
                        if aksi == 'y' or aksi == "Y":
                            session.save(array_of_user, array_of_gadget, array_of_consumable, array_of_gadget_borrow_history, array_of_gadget_return_history, array_of_consumable_history)

                            # akan tetap melakukan save di directory awal (walaupun pilihan folder save di directory lain)                         
                            saved_data_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                            saved_data_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                            saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
                            saved_data_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
                            saved_data_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
                        else: # jika tidak melakukan save, semua csv di directory awal akan kembali ke kondisi "csv saat terakhir melakukan save"
                            preparation.writeLastChangeData(list1, rootbaru,folderbaru)
                        
                        print("----------------------Sampai Jumpa!----------------------")
                        print("Terima kasih telah menggunakan aplikasi Kantong Ajaib >_<")
                        status_sesi = False
                        status_apps = False
                
                ## aksi save
                elif pilihan == "save":
                    session.save(array_of_user, array_of_gadget, array_of_consumable, array_of_gadget_borrow_history, array_of_gadget_return_history, array_of_consumable_history)
                    
                    # akan tetap melakukan save di directory awal (walaupun pilihan folder save di directory lain)
                    saved_data_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                    saved_data_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                    saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
                    saved_data_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
                    saved_data_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
        
        # jika role sebagai user
        else:
            print("Halo " + array_of_user[idx_user][1] + "! Senang bertemu dengan Anda")
            while status_sesi == True:
                ## user session (memilih aksi)
                print("*================================================================*")
                print("Silakan masukkan perintah di antara pilihan di bawah ini")
                print()
                print("                   *___________________*")
                print("                   |   _____________   |")
                print("                   |  |             |  |")
                print("                   |  | carirarity  |  |")
                print("                   |  | caritahun   |  |")
                print("                   |  | pinjam      |  |")
                print("                   |  | kembalikan  |  |")
                print("                   |  | minta       |  |")
                print("                   |  | help        |  |")
                print("                   |  | save        |  |")
                print("                   |  | exit        |  |")
                print("                   |  |_____________|  |")
                print("                   |___________________|")
                print()
                print("*================================================================*")
                print()
                pilihan = str(input("Masukkan perintah: "))   
                while pilihan!='exit' and pilihan!='carirarity' and pilihan!='caritahun' and pilihan!='pinjam' and pilihan!='help' and pilihan != 'kembalikan' and pilihan != 'minta' and pilihan != 'save':
                    print("Maaf "+pilihan+"'"+" tidak ada dalam pilihan")
                    print()
                    pilihan = str(input("Masukkan perintah: "))
                print()

                if pilihan == "help":
                    session.Help('user')

                ## aksi mencari item berdasarkan rarity
                elif pilihan == "carirarity":
                    print("<=============================================>")
                    rarity = str(input("Masukkan rarity: "))
                    print("Hasil pencarian: ")
                    session.findGadgetByRarity(rarity, array_of_gadget)
                    print("<=============================================>")
                ## aksi mencari gadget berdasarkan tahun dan operator
                elif pilihan == "caritahun":
                    print("<=============================================>")
                    year = int(input("Masukkan tahun: "))
                    operator = str(input("Masukkan kategori: "))
                    print("Hasil pencarian: ")
                    session.findGadgetByYear(year, operator, array_of_gadget)
                    print("<=============================================>")
                ## aksi 
                elif pilihan == "pinjam": 
                    print("<=============================================>")
                    n = len(array_of_gadget)
                    m = len(array_of_gadget_borrow_history)
                    id_item = input("Masukkan id item: ")
                    ada = 0
                    returned = False 
                    
                    if function.idItemIsExist(id_item, array_of_gadget, array_of_gadget):
                        for i in range (1,n):
                            if id_item == array_of_gadget[i][0]:
                                ada = ada + 1
                                posisi = i

                        for i in range (m):
                            if array_of_gadget_borrow_history[i][1] == array_of_user[idx_user][0] and array_of_gadget_borrow_history[i][2] == id_item and array_of_gadget_borrow_history[i][5] == "FALSE":
                                returned = False
                            else: 
                                returned = True
                        if ada == 1 and returned == True:
                            tanggal = input("Tanggal Peminjaman(dd/mm/yyyy): ")
                            jumlah = int(input("Jumlah: "))

                            if 0 < jumlah :
                                if jumlah <= int(array_of_gadget[posisi][3]) and int(array_of_gadget[posisi][3]) > 0:
                                    print("Item " + array_of_gadget[posisi][1] + "(x" + str(jumlah) + ") berhasil dipinjam!")
                                    array_of_gadget[posisi][3] = int(array_of_gadget[posisi][3]) -jumlah
                                    string = preparation.convertArrayToString(array_of_gadget)
                                    f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"), "w")
                                    f.write(string)
                                    f.close()
                                    data_baru = [str(m), array_of_user[idx_user][0], id_item, tanggal, str(jumlah), "FALSE"]
                                    array_of_gadget_borrow_history.append(data_baru)
                                    string_data = preparation.convertArrayToString(array_of_gadget_borrow_history)
                                    f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"), "w")
                                    f.write(string_data)
                                    f.close()
                                    array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                                    array_of_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
                                else:
                                    print("Persediaan gadget habis")  
                            else:
                                 print("Harap masukkan jumlah dengan benar")
                        else:
                            print("Anda belum mengembalikan gadget tersebut, harap dikembalikan terlebih dahulu")
                    else: 
                        print("Tidak ada item dengan ID tersebut")
                    print("<=============================================>")
                    print()
                elif pilihan == "minta":
                    print("<=============================================>")
                    session.mintaConsumable(array_of_consumable,array_of_consumable_history,array_of_user,idx_user, rootbaru,folderbaru)
                    array_of_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                    array_of_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
                    print("<=============================================>")
                    print()

                elif pilihan == "kembalikan":
                    print("<=============================================>")
                    session.returnGadget(array_of_gadget,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_user,idx_user, rootbaru,folderbaru)
                    array_of_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                    array_of_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
                    array_of_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
                    print("<=============================================>")
                    print()
                
                elif pilihan == "exit":
                    print("<=============================================>")
                    list1 = [saved_data_gadget,saved_data_consumable,saved_data_gadget_borrow_history,saved_data_gadget_return_history,saved_data_consumable_history]
                    list2 = [array_of_gadget,array_of_consumable,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_consumable_history]
                    
                    count_udah_kondisi_baru = 0
                    for i in range(len(list1)):
                        if list1[i] == list2[i]:
                            count_udah_kondisi_baru += 1
                    
                    if count_udah_kondisi_baru == 5: # kondisi kalo saved_data udah kondisi terbaru semua, bisa langsung exit
                        print("----------------------Sampai Jumpa!----------------------")
                        print("Terima kasih telah menggunakan aplikasi Kantong Ajaib >_<")
                        status_sesi = False
                        status_apps = False
                    else:
                        aksi = str(input("Data perubahan terakhir belum disave, save sekarang (Y/N)? "))
                        if aksi == 'y' or aksi == "Y":
                            session.save(array_of_user, array_of_gadget, array_of_consumable, array_of_gadget_borrow_history, array_of_gadget_return_history, array_of_consumable_history)
                            # akan tetap melakukan save di directory awal (walaupun pilihan folder save di directory lain)
                            saved_data_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                            saved_data_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                            saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
                            saved_data_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
                            saved_data_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
                        else:   # jika tidak melakukan save, semua csv di directory awal akan kembali ke kondisi "csv saat terakhir melakukan save"
                            preparation.writeLastChangeData(list1, rootbaru,folderbaru)
                        
                        print("----------------------Sampai Jumpa!----------------------")
                        print("Terima kasih telah menggunakan aplikasi Kantong Ajaib >_<")
                        status_sesi = False
                        status_apps = False

                elif pilihan == "save":
                    # ngerubah array saved ke data yang terbaru (terakhir)
                    session.save(array_of_user, array_of_gadget, array_of_consumable, array_of_gadget_borrow_history, array_of_gadget_return_history, array_of_consumable_history)
  
                     # akan tetap melakukan save di directory awal (walaupun pilihan folder save di directory lain)
                    saved_data_gadget = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"))
                    saved_data_consumable = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"))
                    saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"))
                    saved_data_gadget_return_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_return_history.csv"))
                    saved_data_consumable_history = preparation.loadAndRefreshCSV(str(rootbaru+"\\"+folderbaru+"\\"+"consumable_history.csv"))
