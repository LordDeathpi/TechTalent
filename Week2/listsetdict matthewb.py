fruitlist = ["Grape", "Apple", "Strawberry"]
print(fruitlist)
print(fruitlist[1])

fruitset = {"Pineapple", "Plum", "Cherry"}
print(fruitset)
fruitset.add("Orange")
print(fruitset)
fruitset.add("Orange")
print(fruitset)

fruitdict = {"Lemon": "£0.50", "Lime": "£0.51", "Banana": "£0.34"}
print(fruitdict)
print(fruitdict["Lime"])
while(True):
    given = input("What fruit do you wish to know the price of? ")
    if (given in fruitdict):
        print(fruitdict[given])
    elif (given == "exit" or given == "Exit"):
        break
    else:
        print("Fruit is not in dictionary")
        addfruit = input("Do you want to add? ")
        if (addfruit == "Yes" or addfruit == "yes"):
            fruitprice = input("What's the fruit price? ")
            fruitdict[given] = fruitprice
        else:
            continue
        
        
        
    