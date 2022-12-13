bikeprice = 2000
while (bikeprice > 1001):
    bikedec = bikeprice * 10 / 100
    bikeprice = bikeprice - bikedec
    print(round(bikeprice, 2))
    
def bikedrop (price, perc, min):
    while (price > min):
        dec = price * perc / 100
        price = price - dec
        print(round(price, 2))
        
bikedrop(1000, 5, 200)

    
