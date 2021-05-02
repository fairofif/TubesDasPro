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

def writeUserToUserData(nama_register, username_register, password_register, alamat_register, array_of_user, rootbaru,folderbaru):
    array_of_user.append([str(len(array_of_user)), username_register, nama_register, alamat_register, password_register, "user"])
    string_data = convertArrayToString(array_of_user)

    f = open(str(rootbaru+"\\"+folderbaru+"\\"+"user.csv"), "w")
    f.write(string_data)
    f.close()

def convertArrayToString(array_of_data):
    string_data = ""
    for array in array_of_data:
        arr_data_all_string = [str(var) for var in array]
        string_data += ";".join(arr_data_all_string)
        string_data += "\n"
    return string_data

def writeItemToData(arr_add, arr1, arr2, rootbaru,folderbaru):
    if len(arr_add) == 6:
        arr1.append(arr_add)
        string_data = convertArrayToString(arr1)
        f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"), "w")
        f.write(string_data)
        f.close()
    elif len(arr_add) == 5:
        arr2.append(arr_add)
        string_data = convertArrayToString(arr2)
        f = open(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"), "w")
        f.write(string_data)
        f.close()

def deleteItemFromData(id_item, arr, rootbaru,folderbaru):
    n = len(arr)
    i = 1
    while i != n and id_item != arr[i][0]:
        i += 1
    if i != n:
        arr.pop(i)
        string_data = convertArrayToString(arr)
        if len(arr[0]) == 6:
            f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"), "w")
            f.write(string_data)
            f.close()
        elif len(arr[0]) == 5:
            f = open(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"), "w")
            f.write(string_data)
            f.close()

def updateJumlahItem(jumlah, idx, arr, rootbaru,folderbaru):
    
    arr[idx][3] = str(int(arr[idx][3]) + jumlah)
    
    string_data = convertArrayToString(arr)
    if len(arr[0]) == 6:
        f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"), "w")
        f.write(string_data)
        f.close()
    elif len(arr[0]) == 5:
        f = open(str(rootbaru+"\\"+folderbaru+"\\"+"consumable.csv"), "w")
        f.write(string_data)
        f.close()
    if jumlah < 0:
        print(str(jumlah * (-1)) + " " + arr[idx][1] + " berhasil dibuang. Stok sekarang: " + arr[idx][3])
    elif jumlah > 0:
        print(str(jumlah) + " " + arr[idx][1] + " berhasil ditambahkan. Stok sekarang: " + arr[idx][3])
    else:
        print("Jumlah stok " + arr[idx][1] + " tidak berubah")

def updategadgetreturn(x, y, z, rootbaru,folderbaru):
    z[y][3] = str(int(z[y][3]) + int(x))
    string_data = convertArrayToString(z)
    f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget.csv"), "w")
    f.write(string_data)
    f.close()

def updateborrowhistory(x,y, rootbaru,folderbaru):
    y[x][5] = "TRUE"
    string_data = convertArrayToString(y)
    f = open(str(rootbaru+"\\"+folderbaru+"\\"+"gadget_borrow_history.csv"), "w")
    f.write(string_data)
    f.close()

def writeLastChangeData(list1, rootbaru,folderbaru):
    filename = ["gadget.csv","consumable.csv","gadget_borrow_history.csv","gadget_return_history.csv","consumable_history.csv"]
    for i in range(len(filename)):
        locate_filename = str(rootbaru+"\\"+folderbaru+"\\"+filename[i])
        string_data = convertArrayToString(list1[i])
        f = open(locate_filename, "w")
        f.write(string_data)
        f.close
