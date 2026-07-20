import ast
def test():
    list1_active = []
    with open("customers (5).txt", "r")as file1:
        with open("plans.txt", "r")as file2:
            with open("payments (1).txt", "r")as file3:
                with open("tickets.txt", "r")as file4:
                    with open("usage.txt", "r")as file5:
                     var1=ast.literal_eval(file1.read())
                     var2=ast.literal_eval(file2.read())
                     var3=ast.literal_eval(file3.read())
                     var4=ast.literal_eval(file4.read())
                     var5=ast.literal_eval(file5.read())
                     for i in var1:
                         if i["status"] == "ACTIVE":
                             if i["plans"] == "Gold" or i["plans"] == "Silver":
                                 if i["down"]


        # print(var1)
