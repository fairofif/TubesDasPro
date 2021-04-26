def loginForm():
    uname_user = str(input("Username: "))
    pass_user = str(input("Password: "))
    return uname_user, pass_user

def loginIsTrue(uname, password, arr):
    n = len(arr)
    i = 1
    count = 0
    while i != n:
        if uname == arr[i][1] and password == arr[i][4]:
            count += 1
        i += 1
    if count > 0:
        return True
    else:
        return False

def decideRoleAndGetIndex(uname, arr):
    i = 1
    while uname != arr[i][1]:
        i += 1
    role = arr[i][5]
    return role, i

def usernameIsExist(username_register, array_of_user):
    n = len(array_of_user)
    count = 0
    i = 1
    while i != n:
        if array_of_user[i][2] == username_register:
            count += 1
        i += 1
    if count == 1:
        return True
    else:
        return False

def registerUserForm(array_of_user):
    nama_register = str(input("Nama : "))
    username_register = str(input("Username : "))
    while usernameIsExist(username_register, array_of_user) == True:
        print("Username tersebut telah digunakan orang lain!")
        username_register = str(input("Username : "))
    password_register = str(input("Password : "))
    while len(password_register) > 16 or len(password_register) < 6:
        print("Password minimal 6 karakter dan maksimal 16 karakter!")
        password_register = str(input("Password : "))
    alamat_register = str(input("Alamat : "))
    return nama_register, username_register, password_register, alamat_register

def idItemIsValid(id):
    first_char = False
    if id[0] == 'C' or id[0] == 'G':
        first_char = True

    next_char = False
    n = len(id)
    char_not_valid = 0
    if n < 2:
        return False
    elif int(id[1]) == 0:
        return False
    else:
        for i in range(1,n):
            if ord(id[i]) < 48 or ord(id[i]) > 57:
                char_not_valid += 1
    if char_not_valid == 0:
        next_char = True
    
    if first_char == True and next_char == True:
        return True
    else:
        return False

def idItemIsExist(id, arr1, arr2):
    count = 0
    n = len(arr1)
    for i in range(1,n):
        if arr1[i][0] == id:
            count += 1
    n = len(arr2)
    for i in range(1,n):
        if arr2[i][0] == id:
            count += 1
    if count == 0:
        return False
    else:
        return True

def addItemForm(arr1,arr2):
    id = str(input("Masukan ID: "))
    if idItemIsValid(id) == True:
        if idItemIsExist(id, arr1, arr2) == False:
            nama = str(input("Masukan Nama: "))
            desc = str(input("Masukan Deskripsi: "))
            jumlah = int(input("Masukan Jumlah: "))
            rarity = str(input("Masukan Rarity: "))
            if id[0] == 'G': 
                tahun = int(input("Masukan Tahun: "))
                return [id, nama, desc, str(jumlah), rarity, str(tahun)]
            else:
                return [id, nama, desc, str(jumlah), rarity]
        else:
            print("Gagal menambahkan item karena ID sudah ada")
            return []
    else:
        print("Gagal menambahkan item karena ID tidak valid")
        return []    



