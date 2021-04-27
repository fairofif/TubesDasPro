import preparation
import session
import function

### kantongajaib.py berfungsi sebagain "MAIN SESSION" dalam program ini

# load preparation data
array_of_user = preparation.loadAndRefreshCSV("user.csv")
array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")
array_of_gadget_borrow_history = preparation.loadAndRefreshCSV("gadget_borrow_history.csv")
array_of_gadget_return_history = preparation.loadAndRefreshCSV("gadget_return_history.csv")
array_of_consumable_history = preparation.loadAndRefreshCSV("consumable_history.csv")

status_apps = True
while status_apps == True:
    aksi = str(input("Masukan perintah (ketik 'help' untuk bantuan): "))
    if aksi == "help":
        print("isi pake prosedur help")

    elif aksi == "register":
        nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
        preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user)
        array_of_user = preparation.loadAndRefreshCSV("user.csv")

    elif aksi == "exit":
        status_apps = False

    elif aksi == "login":
        # log in dan penentuan role berdasarkan username dan pass
        uname_form, password_form = function.loginForm()
        while function.loginIsTrue(uname_form, password_form, array_of_user) == False:
            print("Username atau password salah!")
            uname_form, password_form = function.loginForm()
        role, idx = function.decideRoleAndGetIndex(uname_form, array_of_user)
        print("Halo " + array_of_user[idx][1] + "! Selamat Datang di Kantong Ajaib")

        status_sesi = True
        # jika role sebagai admin
        
        if role == "admin":
            while status_sesi == True:
                ## sesi admin (memilih aksi yang akan dilakukan)
                pilihan = str(input("Masukan command aksi (ketik 'help' untuk bantuan): "))
                
                if pilihan == "help":
                    print("tolong isiin prosedur help ya")
                
                elif pilihan == "exit":
                    status_sesi = False
                    status_apps = False

                ## aksi untuk menambahkan user baru (register)
                elif pilihan == "register":
                    nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
                    preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user)
                    array_of_user = preparation.loadAndRefreshCSV("user.csv")
                ## aksi untuk mencari item berdasarkan raritynya
                elif pilihan == "carirarity":
                    rarity = str(input())
                    session.findGadgetByRarity(rarity, array_of_gadget)
                    session.findGadgetByRarity(rarity, array_of_consumable)
                ## aksi untuk mencari gadget berdasarkan tahun dan operator
                elif pilihan == "caritahun":
                    year = int(input("Tahun: "))
                    operator = str(input("Operator: "))
                    session.findGadgetByYear(year, operator, array_of_gadget)
                ## aksi untuk menamahkan item baru ke dalam data
                elif pilihan == "tambahitem":
                    arr_input = function.addItemForm(array_of_gadget, array_of_consumable)
                    preparation.writeItemToData(arr_input, array_of_gadget, array_of_consumable)
                    if len(arr_input) == 6:  # kalo addnya gadget
                        array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
                    elif len(arr_input) == 5: # kalo addnya consumable
                        array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")
                ## aksi untuk menghapus item
                elif pilihan == "hapusitem":
                    id_item = str(input("Masukan ID Item: "))
                    if function.idItemIsExist(id_item, array_of_gadget, array_of_consumable) == True:
                        if id_item[0] == 'G':
                            idx = function.getIdxOfItem(id_item, array_of_gadget)
                            aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_gadget[idx][1] + " (Y/N)? "))
                            if aksi == 'Y' or aksi == 'y':
                                preparation.deleteItemFromData(id_item, array_of_gadget)
                                array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
                        else:
                            idx = function.getIdxOfItem(id_item, array_of_consumable)
                            aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_consumable[idx][1] + " (Y/N)? "))
                            if aksi == 'Y' or aksi == 'y':
                                preparation.deleteItemFromData(id_item, array_of_consumable)
                                array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")
                    else:
                        print("Tidak ada item dengan ID tersebut.")
                ## aksi untuk mengubah jumlah item
                elif pilihan == "ubahjumlah":
                    id_item = str(input("Masukan ID Item: "))
                    if function.idItemIsExist(id_item, array_of_gadget, array_of_consumable) == True:
                        jumlah = int(input("Masukan Jumlah: "))
                        ## untuk gadget id
                        if id_item[0] == 'G':
                            idx = function.getIdxOfItem(id_item, array_of_gadget)
                            if jumlah < 0:    
                                if jumlah >= int(array_of_gadget[idx][3]):
                                    preparation.updateJumlahItem(jumlah, idx, array_of_gadget)
                                    array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
                                else:
                                    print(str(jumlah*(-1)) + " " + array_of_gadget[idx][1] + " gagal dibuang karena stok kurang. Stok sekarang: " 
                                    + array_of_gadget[idx][3] + " (<" + str(jumlah*(-1)) + ")")
                            else:
                                preparation.updateJumlahItem(jumlah, idx, array_of_gadget)
                                array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
                        ## untuk consumable id
                        else:
                            idx = function.getIdxOfItem(id_item, array_of_consumable)
                            if jumlah < 0:    
                                if jumlah >= int(array_of_consumable[idx][3]):
                                    preparation.updateJumlahItem(jumlah, idx, array_of_consumable)
                                    array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")
                                else:
                                    print(str(jumlah*(-1)) + " " + array_of_consumable[idx][1] + " gagal dibuang karena stok kurang. Stok sekarang: " 
                                    + array_of_consumable[idx][3] + " (<" + str(jumlah*(-1)) + ")")
                            else:
                                preparation.updateJumlahItem(jumlah, idx, array_of_consumable)
                                array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")
                    else:
                        print("Tidak ada item dengan ID tersebut.")

                ## aksi untuk melihat riwayat peminjaman
                elif pilihan == "riwayatpinjam":
                    session.showHistory(array_of_gadget_borrow_history)
                    print("ingin menambah entry lagi?\n1. Ya\n2. Tidak")
                    jawaban=int(input())
                    if jawaban==1:
                        array_baru=function.DelArray(array_of_gadget_borrow_history)
                        while array_baru!=[] and jawaban==1:
                            session.showHistory(array_baru)
                            print("ingin menambah entry lagi?\n1 1. Ya\n2. 2.Tidak")
                            jawaban=int(input())
                            array_baru=function.DelArray(array_baru)
                        if array_baru==[] and jawaban==1:
                            print("data sudah habis")
                        else:
                            print("selesai")
                    elif jawaban==2:
                        print("selesai")
                ## aksi untuk melihat riwayat pengembalian    
                elif pilihan == "riwayatkembali":
                    session.showHistory(array_of_gadget_return_history)
                    print("ingin menambah entry lagi?\n1. Ya\n2. Tidak")
                    jawaban=int(input())
                    if jawaban==1:
                        array_baru=function.DelArray(array_of_gadget_return_history)
                        while array_baru!=[] and jawaban==1:
                            session.showHistory(array_baru)
                            print("ingin menambah entry lagi?\n1 1. Ya\n2. 2.Tidak")
                            jawaban=int(input())
                            array_baru=function.DelArray(array_baru)
                        if array_baru==[] and jawaban==1:
                            print("data sudah habis")
                        else:
                            print("selesai")
                    elif jawaban==2:
                        print("selesai")
                ## aksi untuk melihat riwayat pengambilan consumable
                elif pilihan == "riwayatambil":
                    session.showHistory(array_of_consumable_history)
                    print("ingin menambah entry lagi?\n1. Ya\n2. Tidak")
                    jawaban=int(input())
                    if jawaban==1:
                        array_baru=function.DelArray(array_of_consumable_history)
                        while array_baru!=[] and jawaban==1:
                            session.showHistory(array_baru)
                            print("ingin menambah entry lagi?\n1 1. Ya\n2. 2.Tidak")
                            jawaban=int(input())
                            array_baru=function.DelArray(array_baru)
                        if array_baru==[] and jawaban==1:
                            print("data sudah habis")
                        else:
                            print("selesai")
                    elif jawaban==2:
                        print("selesai")


        # role sebagai user
        else:
            while status_sesi == True:
                ## user session (memilih aksi)
                ## =========================== BELUM DITAMBAHIN ERROR CASE ##===========================
                pilihan = str(input("Masukan command aksi (ketik 'help' untuk bantuan): "))   
                
                if pilihan == "help":
                    print("tambahin help")
                elif pilihan == "exit":
                    status_sesi = False
                    status_apps = False

                ## aksi mencari item berdasarkan rarity
                elif pilihan == "carirarity":
                    rarity = str(input())
                    session.findGadgetByRarity(rarity, array_of_gadget)
                    session.findGadgetByRarity(rarity, array_of_consumable)
                ## aksi mencari gadget berdasarkan tahun dan operator
                elif pilihan == "caritahun":
                    year = int(input("Tahun: "))
                    operator = str(input("Operator: "))
                    session.findGadgetByYear(year, operator, array_of_gadget)
                ## aksi 
                elif pilihan == "pinjam": 
                    n = len(array_of_gadget)
                    m = len(array_of_gadget_borrow_history)
                    id_item = input("Masukkan id item: ")
                    ada = 0
                    returned = False 
                    
                    if function.idItemIsValid(id_item):
                        for i in range (1,n,1):
                            if id_item == array_of_gadget[i][0]:
                                ada = ada + 1
                                posisi = i
                                break

                        for i in range (1,m,1):
                            if array_of_gadget_borrow_history[i][1] == array_of_user[idx][0] and array_of_gadget_borrow_history[i][2] == id_item and array_of_gadget_borrow_history[i][5] == "FALSE":
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
                                else:
                                    print("Persediaan gadget habis") 
                                data_baru = [str(len(array_of_gadget_borrow_history)), array_of_user[idx][0], id_item, tanggal, str(jumlah), "FALSE"]
                                array_of_gadget_borrow_history.append(data_baru)
                                string_data = preparation.convertArrayToString(array_of_gadget_borrow_history)
                                f = open("gadget_borrow_history.csv", "w")
                                f.write(string_data)
                                f.close()
                        else:
                            print("Anda belum mengembalikan gadget tersebut, harap dikembalikan terlebih dahulu")
                    else: 
                        print("ID item salah, harap masukkan id item dengan benar")