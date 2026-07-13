def var1():
    var_input = input("kala: ")
    var1_input = int(input("price: "))
    var_final = f'{var_input}, {var1_input}'
    print(var_final)
    with open("kalaha.txt" , "a")as file:
        file.write(var_final)
        file.write("\n")



var1()
