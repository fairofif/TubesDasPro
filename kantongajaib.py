import preparation
import session
import function
import preparation

### kantongajaib.py berfungsi sebagain "MAIN SESSION" dalam program ini

array_of_user = preparation.loadAndRefreshCSV("user.csv")
array_of_gadget = preparation.loadAndRefreshCSV("gadget.csv")

session.introSession()
role = str(input())
while role != '1' and role != '2':
    print("Input salah! Masukan ulang...(1 atau 2)")
    session.introSession()
    role = str(input())

if role == "1":
    uname_admin, pass_admin = function.loginAdmin()
    while function.loginAdminIsTrue(uname_admin, pass_admin, array_of_user) == False:
        print("Username atau password_register salah!")
        uname_admin, pass_admin = function.loginAdmin()
    print("Log in Berhasil!")
    session.adminSession()
    pilihan = int(input())
    while pilihan != 1:
        print("Input salah! Ulangi...")
        session.adminSession()
        pilihan = int(input())
    if pilihan == 1:
        nama_register, username_register, password_register, alamat_register = function.registerUserForm(array_of_user)
        preparation.writeUserToUserData(nama_register,username_register,password_register,alamat_register,array_of_user)
        array_of_user = preparation.loadAndRefreshCSV("user.csv")

else:
    uname_user, pass_user = function.loginUser()
    while function.loginUserIsTrue(uname_user, pass_user,array_of_user) == False:
        print("Username atau password_register salah!")
        uname_user, pass_user = function.loginUser()
    print("Log in Berhasil!")
    session.userSession()
    pilihan = int(input())
    if pilihan == 1:
        rarity = str(input())
        session.findGadgetByRarity(rarity, array_of_gadget)