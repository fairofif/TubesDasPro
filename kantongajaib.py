import preparation
import session
import function

### kantongajaib.py berfungsi sebagain "MAIN SESSION" dalam program ini

# load preparation data
array_of_user = preparation.loadAndRefreshCSV("user.csv")
array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")

# log in dan penentuan role berdasarkan username dan pass
uname_form, password_form = function.loginForm()
while function.loginIsTrue(uname_form, password_form, array_of_user) == False:
    print("Username atau password salah!")
    uname_form, password_form = function.loginForm()
role, idx = function.decideRoleAndGetIndex(uname_form, array_of_user)
print("Halo " + array_of_user[idx][1] + "! Selamat Datang di Kantong Ajaib")

# jika role sebagai admin
if role == "admin":
    ## sesi admin (memilih aksi yang akan dilakukan)
    session.adminSession()
    pilihan = int(input())
    ## loop untuk membenarkan inputan user
    while pilihan < 1 or pilihan > 5:
        print("Input salah! Ulangi...")
        session.adminSession()
        pilihan = int(input())
    ## aksi untuk menambahkan user baru (register)
    if pilihan == 1:
        nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
        preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user)
        array_of_user = preparation.loadAndRefreshCSV("user.csv")
    ## aksi untuk mencari item berdasarkan raritynya
    elif pilihan == 2:
        rarity = str(input())
        session.findGadgetByRarity(rarity, array_of_gadget)
        session.findGadgetByRarity(rarity, array_of_consumable)
    ## aksi untuk mencari gadget berdasarkan tahun dan operator
    elif pilihan == 3:
        year = int(input("Tahun: "))
        operator = str(input("Operator: "))
        session.findGadgetByYear(year, operator, array_of_gadget)
    ## aksi untuk menamahkan item baru ke dalam data
    elif pilihan == 4:
        arr_input = function.addItemForm(array_of_gadget, array_of_consumable)
        preparation.writeItemToData(arr_input, array_of_gadget, array_of_consumable)
        if len(arr_input) == 6:  # kalo addnya gadget
            array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
        elif len(arr_input) == 5: # kalo addnya consumable
            array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")
    ## aksi untuk menghapus item
    elif pilihan == 5:
        id_item = str(input("Masukan ID Item: "))
        if function.idItemIsExist(id_item, array_of_gadget, array_of_consumable) == True:
            if id_item[0] == 'G':
                idx = function.getIdxOfItem(id_item, array_of_gadget)
                aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_gadget[idx][1] + " (Y/N)? "))
                if aksi == 'Y' or aksi == 'y':
                    preparation.deleteItemFromData(id_item, array_of_gadget)
            else:
                idx = function.getIdxOfItem(id_item, array_of_consumable)
                aksi = str(input("Apakah anda yakin ingin menghapus " + array_of_consumable[idx][1] + " (Y/N)? "))
                if aksi == 'Y' or aksi == 'y':
                    preparation.deleteItemFromData(id_item, array_of_consumable)
        else:
            print("Tidak ada item dengan ID tersebut.")    


# role sebagai user
else:
    ## user session (memilih aksi)
    session.userSession()
    pilihan = int(input())          ## =========================== BELUM DITAMBAHIN ERROR CASE ##===========================
    
    ## aksi mencari item berdasarkan rarity
    if pilihan == 1:
        rarity = str(input())
        session.findGadgetByRarity(rarity, array_of_gadget)
        session.findGadgetByRarity(rarity, array_of_consumable)
    ## aksi mencari gadget berdasarkan tahun dan operator
    elif pilihan == 2:
        year = int(input("Tahun: "))
        operator = str(input("Operator: "))
        session.findGadgetByYear(year, operator, array_of_gadget)