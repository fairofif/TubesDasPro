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

def writeUserToUserData(nama_register, username_register, password_register, alamat_register, array_of_user):
    array_of_user.append([str(len(array_of_user)), username_register, nama_register, alamat_register, password_register, "user"])
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

def writeItemToData(arr_add, arr1, arr2):
    if len(arr_add) == 6:
        arr1.append(arr_add)
        string_data = convertArrayToString(arr1)
        f = open("gadget.csv", "w")
        f.write(string_data)
        f.close()
    elif len(arr_add) == 5:
        arr2.append(arr_add)
        string_data = convertArrayToString(arr2)
        f = open("consumable.csv", "w")
        f.write(string_data)
        f.close()

def deleteItemFromData(id_item, arr):
    n = len(arr)
    i = 1
    while i != n and id_item != arr[i][0]:
        i += 1
    if i != n:
        arr.pop(i)
        string_data = convertArrayToString(arr)
        if len(arr[0]) == 6:
            f = open("gadget.csv", "w")
            f.write(string_data)
            f.close()
        elif len(arr[0]) == 5:
            f = open("consumable.csv", "w")
            f.write(string_data)
            f.close()