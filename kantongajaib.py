def loadAndRefreshCSV(csv):
    f = open(csv, "r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_lines.replace("\n", "") for raw_lines in raw_lines]

    array_of_data = []
    for line in lines:
        split_value = []
        tmp = ''
        for c in line:
            if c == ';':
                split_value.append(tmp)
                tmp = ''
            else:
                tmp += c
        if tmp:
            split_value.append(tmp)
        array_of_data.append(split_value)
    return array_of_data 

def introSession():
    print("Pilih role:\n1. Admin\n2. User")
        
def loginAdmin():
    uname_admin = str(input("Username Admin: "))
    pass_admin = str(input("Password Admin: "))
    return uname_admin, pass_admin

def loginUser():
    uname_user = str(input("Username: "))
    pass_user = str(input("Password: "))
    return uname_user, pass_user

def loginAdminIsTrue(uname_admin, pass_admin, array_of_user):
    if uname_admin == array_of_user[1][2] or uname_admin == array_of_user[2][2]:
        if uname_admin == array_of_user[1][2] and pass_admin == array_of_user[1][3]:
            return True
        elif uname_admin == array_of_user[2][2] and pass_admin == array_of_user[2][3]:
            return True
        else:
            return False
    else:
        return False

def loginUserIsTrue(uname_user, pass_user, array_of_user):
    n = len(array_of_user)
    i = 3
    count = 0
    while i != n:
        if uname_user == array_of_user[i][2] and pass_user == array_of_user[i][3]:
            count += 1
        i += 1
    if count > 0:
        return True
    else:
        return False

def adminSession():
    print("1. Daftarkan User")

def registerUserForm():
    nama_register = str(input("Nama : "))
    username_register = str(input("Username : "))
    while usernameIsExist(username_register, array_of_user) == True:
        print("Username tersebut telah digunakan orang lain!")
        username_register = str(input("Username : "))
    password_register = str(input("Password : "))
    while len(password_register) > 16 and len(password_register) < 6:
        print("Password minimal 6 karakter dan maksimal 16 karakter!")
        password_register = str(input("Password : "))
    alamat_register = str(input("Alamat : "))
    return nama_register, username_register, password_register, alamat_register

def usernameIsExist(username_register, array_of_user):
    n = len(array_of_user)
    count = 0
    i = 3
    while i != n:
        if array_of_user[i][2] == username_register:
            count += 1
        i += 1
    if count == 1:
        return True
    else:
        return False

def writeUserToUserData(nama_register, username_register, password_register, alamat_register):
    array_of_user.append([str(len(array_of_user)), nama_register, username_register, password_register, alamat_register])
    string_data = convertArrayToString(array_of_user)

    f = open("user.csv", "w")
    f.write(string_data)
    f.close()

def convertArrayToString(array_of_data):
    string_data = ""
    for array in array_of_data:
        arr_data_all_string = [str(var) for var in array]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

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

# MAIN
array_of_user = loadAndRefreshCSV("user.csv")
array_of_gadget = loadAndRefreshCSV("gadget.csv")

introSession()
role = str(input())
while role != '1' and role != '2':
    print("Input salah! Masukan ulang...(1 atau 2)")
    introSession()
    role = str(input())


if role == "1":
    uname_admin, pass_admin = loginAdmin()
    while loginAdminIsTrue(uname_admin, pass_admin, array_of_user) == False:
        print("Username atau password_register salah!")
        uname_admin, pass_admin = loginAdmin()
    print("Log in Berhasil!")
    adminSession()
    pilihan = int(input())
    while pilihan != 1:
        print("Input salah! Ulangi...")
        adminSession()
        pilihan = int(input())
    if pilihan == 1:
        nama_register, username_register, password_register, alamat_register = registerUserForm()
        writeUserToUserData(nama_register,username_register,password_register,alamat_register)
        array_of_user = loadAndRefreshCSV("user.csv")

else:
    uname_user, pass_user = loginUser()
    while loginUserIsTrue(uname_user, pass_user,array_of_user) == False:
        print("Username atau password_register salah!")
        uname_user, pass_user = loginUser()
    print("Log in Berhasil!")
    userSession()
    pilihan = int(input())
    if pilihan == 1:
        rarity = str(input())
        findGadgetByRarity(rarity, array_of_gadget)