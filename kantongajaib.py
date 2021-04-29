import preparation
import session
import function

### kantongajaib.py berfungsi sebagain "MAIN SESSION" dalam program ini

# load preparation data
array_of_user = preparation.loadAndRefreshCSV("./csv_file/user.csv")
array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
array_of_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
array_of_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
array_of_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
array_of_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")

# load dibawah sebagai "Temp" untuk saved data
saved_data_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
saved_data_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
saved_data_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
saved_data_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")


session.LoadData()
session.Judul()
print()
print('Selamat Datang di "Kantong Ajaib" ')
print()

status_apps = True
while status_apps == True:
    print("Silahkan masukkan perintah di antara pilihan di bawah ini.")
    print("__________ ")
    print("          |")
    print("login     |")
    print("register  |")
    print("help      |")
    print("exit      |")
    print("__________|")
    print()
    aksi = str(input("Masukkan perintah: "))
    while aksi!='register' and aksi!='login' and aksi!='help' and aksi!='exit':
        print("'"+str(aksi)+"'"+" tidak ada dalam pilihan")
        print()
        aksi = str(input("Masukkan perintah: "))

    if aksi == "help":
        session.Help('awal')

    elif aksi == "register":
        print("Silahkan masukkan data sesuai yang diperintahkan")
        nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
        preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user)
        array_of_user = preparation.loadAndRefreshCSV("./csv_file/user.csv")
        print("User "+ nama_register +" telah berhasil register ke dalam kantong ajaib")
        print()
    
    elif aksi == "exit":
        status_apps = False

    elif aksi == "login":
        # log in dan penentuan role berdasarkan username dan pass
        uname_form, password_form = function.loginForm()
        while function.loginIsTrue(uname_form, password_form, array_of_user) == False:
            print("Username atau password salah!")
            uname_form, password_form = function.loginForm()
        role, idx_user = function.decideRoleAndGetIndex(uname_form, array_of_user)
        print("Halo " + array_of_user[idx_user][1] + "! Selamat Datang di Kantong Ajaib")
        status_sesi = True
        # jika role sebagai admin
        
        if role == "admin":
            while status_sesi == True:
                print("Silahkan masukkan perintah di antara pilihan di bawah ini")
                print("________________ ")
                print("                | ")
                print("register        |")
                print("carirarity      |")
                print("caritahun       |")
                print("tambahitem      |")
                print("hapusitem       |")
                print("ubahjumlah      |")
                print("riwayatpinjam   |")
                print("riwayatkembali  |")
                print("riwayatambil    |")
                print("help            |")
                print("save            |")
                print("exit            |")
                print("________________| ")
                print()
                ## sesi admin (memilih aksi yang akan dilakukan)
                pilihan = str(input("Masukkan perintah: "))
                while pilihan!='register' and pilihan!='carirarity' and pilihan!='caritahun' and pilihan!='tambahitem' and pilihan!='hapusitem' and pilihan!='ubahjumlah' and pilihan!='riwayatpinjam' and pilihan!='riwayatkembali' and pilihan!='riwayatambil' and pilihan!='help' and pilihan != 'save' and pilihan!='exit':
                    print("'"+str(pilihan)+"'"+" tidak ada dalam pilihan")
                    print()
                    pilihan = str(input("Masukkan perintah: "))
                
                if pilihan == "help":
                    session.Help('admin')
            
                ## aksi untuk menambahkan user baru (register)
                elif pilihan == "register":
                    nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
                    preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user)
                    array_of_user = preparation.loadAndRefreshCSV("./csv_file/user.csv")
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
                        array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                    elif len(arr_input) == 5: # kalo addnya consumable
                        array_of_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                ## aksi untuk menghapus item
                elif pilihan == "hapusitem":
                    id_item = str(input("Masukan ID Item: "))
                    if function.idItemIsExist(id_item, array_of_gadget, array_of_consumable) == True:
                        if id_item[0] == 'G':
                            idx = function.getIdxOfItem(id_item, array_of_gadget)
                            aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_gadget[idx][1] + " (Y/N)? "))
                            if aksi == 'Y' or aksi == 'y':
                                preparation.deleteItemFromData(id_item, array_of_gadget)
                                array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                        else:
                            idx = function.getIdxOfItem(id_item, array_of_consumable)
                            aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_consumable[idx][1] + " (Y/N)? "))
                            if aksi == 'Y' or aksi == 'y':
                                preparation.deleteItemFromData(id_item, array_of_consumable)
                                array_of_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
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
                                if (jumlah*(-1)) <= int(array_of_gadget[idx][3]):
                                    preparation.updateJumlahItem(jumlah, idx, array_of_gadget)
                                    array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                                else:
                                    print(str(jumlah*(-1)) + " " + array_of_gadget[idx][1] + " gagal dibuang karena stok kurang. Stok sekarang: " 
                                    + array_of_gadget[idx][3] + " (<" + str(jumlah*(-1)) + ")")
                            else:
                                preparation.updateJumlahItem(jumlah, idx, array_of_gadget)
                                array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                        ## untuk consumable id
                        else:
                            idx = function.getIdxOfItem(id_item, array_of_consumable)
                            if jumlah < 0:    
                                if (jumlah*(-1)) <= int(array_of_consumable[idx][3]):
                                    preparation.updateJumlahItem(jumlah, idx, array_of_consumable)
                                    array_of_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                                else:
                                    print(str(jumlah*(-1)) + " " + array_of_consumable[idx][1] + " gagal dibuang karena stok kurang. Stok sekarang: " 
                                    + array_of_consumable[idx][3] + " (<" + str(jumlah*(-1)) + ")")
                            else:
                                preparation.updateJumlahItem(jumlah, idx, array_of_consumable)
                                array_of_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                    else:
                        print("Tidak ada item dengan ID tersebut.")

                ## aksi untuk melihat riwayat peminjaman
                elif pilihan == "riwayatpinjam":
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
                            print("data sudah habis")
                        else:
                            print("selesai")
                    elif aksi == 'N' or aksi == 'n':
                        print("selesai")
                ## aksi untuk melihat riwayat pengembalian    
                elif pilihan == "riwayatkembali":
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
                    elif aksi == 'N' or aksi == 'n':
                        print("selesai")
                ## aksi untuk melihat riwayat pengambilan consumable
                elif pilihan == "riwayatambil":
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
                    elif aksi == 'N' or aksi == 'n':
                        print("selesai")

                elif pilihan == "exit":

                    list1 = [saved_data_gadget,saved_data_consumable,saved_data_gadget_borrow_history,saved_data_gadget_return_history,saved_data_consumable_history]
                    list2 = [array_of_gadget,array_of_consumable,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_consumable_history]
                    
                    count_udah_kondisi_baru = 0
                    for i in range(len(list1)):
                        if list1[i] == list2[i]:
                            count_udah_kondisi_baru += 1
                    
                    if count_udah_kondisi_baru == 5: # kondisi kalo saved_data udah kondisi terbaru semua, bisa langsung exit
                        status_sesi = False
                        status_apps = False

                    else:
                        aksi = str(input("Data perubahan terakhir belum disave, save sekarang (Y/N)? "))
                        if aksi == 'y' or aksi == "Y":
                            saved_data_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                            saved_data_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                            saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
                            saved_data_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
                            saved_data_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")
                            preparation.writeLastChangeData(list1)

                            print("Data terbaru saved!")
                        else:
                            preparation.writeLastChangeData(list1)
                        
                        status_sesi = False
                        status_apps = False
                
                ## aksi save
                elif pilihan == "save":
                    # ngerubah array saved ke data yang terbaru (terakhir)
                    saved_data_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                    saved_data_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                    saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
                    saved_data_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
                    saved_data_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")
                    print("Data terbaru saved!")
        # role sebagai user
        else:
            while status_sesi == True:
                ## user session (memilih aksi)
                ## =========================== BELUM DITAMBAHIN ERROR CASE ##===========================
                print("Silahkan masukkan perintah di antara pilihan di bawah ini.")
                print("____________ ")
                print("            | ")
                print("carirarity  |")
                print("caritahun   |")
                print("pinjam      |")
                print("kembalikan  |")
                print("minta       |")
                print("help        |")
                print("save        |")
                print("exit        |")
                print("____________| ")
                print()
                pilihan = str(input("Masukkan perintah: "))   
                while pilihan!='exit' and pilihan!='carirarity' and pilihan!='caritahun' and pilihan!='pinjam' and pilihan!='help' and pilihan != 'kembalikan' and pilihan != 'minta' and pilihan != 'save':
                    print("'"+str(pilihan)+"'"+" tidak ada dalam pilihan")
                    print()
                    pilihan = str(input("Masukkan perintah: "))

                if pilihan == "help":
                    session.Help('user')

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
                                    f = open("./csv_file/gadget.csv", "w")
                                    f.write(string)
                                    f.close()
                                    data_baru = [str(m), array_of_user[idx_user][0], id_item, tanggal, str(jumlah), "FALSE"]
                                    array_of_gadget_borrow_history.append(data_baru)
                                    string_data = preparation.convertArrayToString(array_of_gadget_borrow_history)
                                    f = open("./csv_file/gadget_borrow_history.csv", "w")
                                    f.write(string_data)
                                    f.close()
                                    array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                                    array_of_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
                                else:
                                    print("Persediaan gadget habis")   
                        else:
                            print("Anda belum mengembalikan gadget tersebut, harap dikembalikan terlebih dahulu")
                    else: 
                        print("ID item salah, harap masukkan id item dengan benar")
                    
                elif pilihan == "minta":
                    session.mintaConsumable(array_of_consumable,array_of_consumable_history,array_of_user,idx_user)
                    array_of_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                    array_of_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")

                elif pilihan == "kembalikan":
                    session.returnGadget(array_of_gadget,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_user,idx_user)
                    array_of_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                    array_of_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
                    array_of_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
                
                elif pilihan == "exit":

                    list1 = [saved_data_gadget,saved_data_consumable,saved_data_gadget_borrow_history,saved_data_gadget_return_history,saved_data_consumable_history]
                    list2 = [array_of_gadget,array_of_consumable,array_of_gadget_borrow_history,array_of_gadget_return_history,array_of_consumable_history]
                    
                    count_udah_kondisi_baru = 0
                    for i in range(len(list1)):
                        if list1[i] == list2[i]:
                            count_udah_kondisi_baru += 1
                    
                    if count_udah_kondisi_baru == 5: # kondisi kalo saved_data udah kondisi terbaru semua, bisa langsung exit
                        status_sesi = False
                        status_apps = False
                    else:
                        aksi = str(input("Data perubahan terakhir belum disave, save sekarang (Y/N)? "))
                        if aksi == 'y' or aksi == "Y":
                            saved_data_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                            saved_data_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                            saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
                            saved_data_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
                            saved_data_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")
                            preparation.writeLastChangeData(list1)

                            print("Data terbaru saved!")
                        else:
                            preparation.writeLastChangeData(list1)
                        
                        status_sesi = False
                        status_apps = False

                elif pilihan == "save":
                    # ngerubah array saved ke data yang terbaru (terakhir)
                    saved_data_gadget = preparation.loadAndRefreshCSV("./csv_file/gadget.csv")
                    saved_data_consumable = preparation.loadAndRefreshCSV("./csv_file/consumable.csv")
                    saved_data_gadget_borrow_history = preparation.loadAndRefreshCSV("./csv_file/gadget_borrow_history.csv")
                    saved_data_gadget_return_history = preparation.loadAndRefreshCSV("./csv_file/gadget_return_history.csv")
                    saved_data_consumable_history = preparation.loadAndRefreshCSV("./csv_file/consumable_history.csv")
                    print("Data terbaru saved!")

