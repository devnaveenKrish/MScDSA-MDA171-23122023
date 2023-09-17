
import random

Orders = [] 
Menu = [["Chicken", 70], ["Pasta", 115], ["Juice", 30], ["Mojito", 50]] 

def insert_orders():
    elements = int(input("Please Enter the Number of Items You Would Like to Order: "))    
    order = {}
    r1 = random.randint(1, 9)
    r2 = random.randint(0, 9)
    r3 = random.randint(0, 9)
    r4 = random.randint(0, 9)
    r5 = random.randint(0, 9)
    orderid = str(r1) + str(r2) + str(r3) + str(r4) + str(r5)
    order["OrderID"] = orderid 

    order["Items"] = []
    
    for i in range(elements):
        print(Menu)
        i_no = input("Enter the Item Number from the provided list for Order Collection[Chicken-0, Pasta-1, Juice-2, Mojito-3]:\n ")
        q_no = input("Enter the Quantity for the Placed Item:\n ")
        order["Items"].append({"Item_Number": i_no, "Quantity": q_no})
    
    Orders.append(order)

def TotalBill():
    for order in Orders:
        total = 0
        for items in order['Items']:
            total += int(items["Quantity"])*Menu[int(items['Item_Number'])][1]
        print(order)
        print("*"*60)
        print("The total Price for the Order is: \n",total)
        print("*"*90)
    

while True:
    print("*"*90)
    print("\nThe Restaurant Management\n")
    print("*"*90)
    print("1. Select this option to create a New Order\n")
    print("2. Select this option to View Orders\n")
    print("3. Select this option to Exit\n")
    print("*"*90)
    
    u_input = int(input("Enter the Option:"))
    
    if u_input == 1:
        print("*"*60)
        print("-------------------------The Menu Card----------------------\n\n",Menu,"\n")
        print("*"*60)
        insert_orders()
    elif u_input == 2:
        TotalBill()
    elif u_input == 3:
        exit()
    else:
        print("Please Enter a Valid Input!!!\n")

