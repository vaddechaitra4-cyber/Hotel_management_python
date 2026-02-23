menu={"Tea":30,"Burgur":50,"Pizza":80,"Biriyani":250,"Fruits_Slat":60 }
print("i wish you good morning")
print("well come to the hotal")
print("menu",menu)
order_item1=input("please select the food item name: ")
order_total=0
if order_item1 in  menu:
    order_total+=menu[order_item1]
    print("item added")
    order_item2=input("do you want any food item :(Yes/No)")
    print("thank you dear customer do you want any food item?")
    if order_item2=="yes":
        order_item3=input("enter second food item name:")
        
        print("thank you dear customer do you want any food item!")
        if order_item3 in  menu:
            order_total+=menu[order_item3]
            print("item added")
        else:
            print("invalid food item in menu")
else:
    print("please select the  correct order (mam/sir)")
print("total_bill=",order_total)