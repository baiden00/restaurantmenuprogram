import time
import cmath

    
    
print("Welcome to my restaurant!")
print("Please follow instructions carefully you place your order. ***Inputs are case sensitive.*** ")
print("Here is the menu: ")
print("")
print("SANDWICHES:                                       BEVERAGES:  ")
print("")
print("1. Chicken sandwich: $5.25                           1. Small drink: $1.00")
print("2. Beef sandwich: $6.25                              2. Medium drink: $1.75")
print("3. Fish sandwich: $5.75                              3. Large drink: $2.25")
print("")
print("Our only side dish is french fries.")
print("Small fry: $1.00     Medium fry:  $1.50    Large fry: $2.00")
print("")
print("Ketchup is $0.25 per packet")
print("")

time.sleep(1)
sandwich = input("Enter the number for the sandwich you want ") #asking the user what type of sandwich they want
s = 0
sandwich2 = str(sandwich)
sandwich_order = ""
while sandwich > 3 or sandwich < 0:
    print("Wrong input, please start again ")
    print("")
    sandwich = input("Enter the number for the sandwich you want ")
if sandwich == 1:
        print("You've selected Chicken Sandwich, it costs $5.25 ")
        print("")
        s = 5.25
        sandwich_order = "Chicken Sandwich"
elif sandwich == 2:
        print("You've selected Beef Sandwich, it costs $6.25 ")
        print("")
        s = 6.25
        sandwich_order = "Beef Sandwich"
elif sandwich == 3:
        print("You've selected Fish Sandwich, it costs $5.75 ")
        print("")
        s = 5.75
        sandwich_order = "Fish Sandwich"

    


time.sleep(1)

bev_order = ""
b = 0
askbev = raw_input("Do you want a beverage? (Type in Yes or No)  ")
if (str.isdigit(askbev) == True):
    print("Wrong input, Enter Yes or No ")
    askbev = raw_input("Do you want a beverage? (Type in Yes or No)  ")
    
if askbev == "No" or askbev == "No" or askbev == "Yes" or askbev == "Yes": #asking the user if they wanted a beverage and if they answer yes they are allowed to choose the size of beverage they wanted
    
    if askbev == "Yes" or askbev == "yes" :
        beverage = input("Enter the number for the size of beverage you want ")
        while beverage > 3 or beverage < 0:
            print("Wrong input, please start again ")
            print("")
            beverage = input("Enter the number for the size of beverage you want ")
        
        if beverage == 1:
            
            print("You've selected small, it costs $1.00 ")
            print("")
            b = 1.00
            bev_order = "Small Beverage"
        elif beverage == 2:
            
            print("You've selected medium, it costs $1.75 ")
            print("")
            b = 1.75
            bev_order = "Medium Beverage"
        elif beverage == 3:
            
            print("You've selected large, it costs $2.25 ")
            print("")
            b = 2.25
            bev_order = "Large Beverage"
    
else:
    print("Wrong input start again")
    askbev = raw_input("Do you want a beverage? (Type in Yes or No)  ")


    
time.sleep(1)

f = 0
fries_order = ""
askfries = raw_input("Would you like some fries? (Type in Yes or No) ") # asking the usser if they wanted fries and if they answer yes they'll be able to choose the size the want but if they choose no they just carry on to the next thing.
if str.isdigit(askfries) == True: 
    print("Wrong input, Enter Yes or No ")
    askfries = raw_input("Do you want a beverage? (Type in Yes or No)  ")
if askfries == "Yes" or askfries == "yes":
    fries = input("Enter the number for the size of fries you want ")
    while fries > 3 or fries < 0:
         print("Wrong input, please start again ")
         print("")
         fries = input("Enter the number for the size of fries you want ")
    if fries == 1:
        print("You've selected small, it costs $1.00 ")
        print("")
        askmegasize = raw_input("Do you want to Mega-size your fries? (Type in Yes or No) ") 
        if askmegasize == "Yes" or askmegasize == "yes":
            f = 2.00
            fries_order = "Large Fries"
        else:
            f = 1.00
            fries_order = "Small Fries"
    elif fries == 2:
        print("You've selected medium, it costs $1.50 ")
        print("")
        f = 1.50
        fries_order = "Medium Fries"
    elif fries == 3:
        print("You've selected large, it costs $2.00 ")
        print("")
        f = 2.00
        fries_order = "Large Fries"
elif askfries == "No" or askfries == "no" :
    f = 0

    
    
ketchup = input("A packet of ketchup costs $0.25, how many do you want? ")
k = ketchup*0.25


time.sleep(1)


print("Calculating total price... ")
time.sleep(1)

totalorder = k + f + b + s

while s > 0 and f > 0 and b > 0:
    totalorder = totalorder - 1
    totalorder = (totalorder*0.07)+totalorder
    finaltotal = round(totalorder, 2)
    print("You have a $1.00 discount!" )
    break

totalorder = k + f + b + s
totalorder = (totalorder*0.07)+totalorder
finaltotal = round(totalorder, 2)

    
   
def receipt():
    print("")
    print("You order is : ")
    print("")
    print(sandwich_order  +  " "  + "$" + str(s)  )
    if b > 0:
        print(bev_order       +  " "  + "$" + str(b)  )
    if f > 0:
        print(fries_order     +  " "  + "$" +  str(f)  )
    if k > 0:
        print(str(ketchup) + " " + "ketchup packets"  +  " "  + "$" +  str(k))
    print("7% tax has been deducted")
    print("")
    print("The total is cost" +  " "  + "$" + str(finaltotal))
    
receipt()    
   

