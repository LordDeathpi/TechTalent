def main():
    print("This is a monthly payment loan calculator")
    print("")
    
    principal = float(input("Input amount: "))
    apr = float(input("Input apr: "))
    years = int(input("Input years: "))
    
    monthlyrate = apr / 1200
    months = years * 12
    monthlypay = principal * monthlyrate / (1 -(1 + monthlyrate) ** (- months) )
   
    print("Monthly payment:", round(monthlypay, 2))
   
main()
    