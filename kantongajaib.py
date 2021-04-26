import preparation
import session
import function

### kantongajaib.py berfungsi sebagain "MAIN SESSION" dalam program ini

# load preparation data
array_of_user = preparation.loadAndRefreshCSV("user.csv")
array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")
array_of_consumable = preparation.loadAndRefreshCSV("consumable.csv")

# home session (memilih role sebagai admin atau user)
session.introSession()
role = str(input())
while role != '1' and role != '2':
    print("Input salah! Masukan ulang...(1 atau 2)")
    session.introSession()
    role = str(input())

# jika role sebagai admin
if role == "1":
    uname_admin, pass_admin = function.loginAdmin() ## memanggil fungsi untuk menginput username dan pass admin
    ## loop untuk mengecek kebenaran username dan pass berdasarkan user.csv
    while function.loginAdminIsTrue(uname_admin, pass_admin, array_of_user) == False:
        print("Username atau password_register salah!")
        uname_admin, pass_admin = function.loginAdmin()
    print("Log in Berhasil!")

    ## sesi admin (memilih aksi yang akan dilakukan)
    session.adminSession()
    pilihan = int(input())
    ## loop untuk membenarkan inputan user
    while pilihan < 1 or pilihan > 4:
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


# role sebagai user
else:
    uname_user, pass_user = function.loginUser()
    ## loop untuk mengecek dan membenarkan username dan pass inputan user
    while function.loginUserIsTrue(uname_user, pass_user,array_of_user) == False:   # jika username dan pass salah
        print("Username atau password_register salah!")
        uname_user, pass_user = function.loginUser()
    print("Log in Berhasil!")

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