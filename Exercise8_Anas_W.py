print("Create a new account")
CreatUser = input("CreatUser : ")
Creatpassword = input("CreatPass : ")
print("Creat a new account Complete")
print("------------------------------")
print("Please Login")
UsernameInput = input("Username : ")
PasswordInput = input("Password : ")
if UsernameInput == CreatUser:
    if PasswordInput == Creatpassword:
        print("----------------------")
        print("  Welcome! To L-SHOP"  )
        print("------รายการสินค้า------")
        beg = 400
        shoe = 350
        shirt = 200
        print(f"Option 1 beg   x 1 : {beg} THB")
        print(f"Option 2 shoe  x 1 : {shoe} THB")
        print(f"Option 3 shirt x 1 : {shirt} THB")    
        select = int(input("Option : "))
        if select == 1:
            object = beg
            amount = int(input("How much do you want : "))
        
        elif select == 2:
            object = shoe
            amount = int(input("How much do you want : "))
            
        elif select ==3:
            object = shirt
            amount = int(input("How much do you want : "))
        
        else:
            print("I don't know what you want?")
            object = 0
            amount = 0
        
        total = object * amount

        print("----------------------")
        
        print(f"{object} x {amount} = {total} THB")
    else:
        print("Wrong password !")
else:
    print("Wrong User !")



    
    
    
