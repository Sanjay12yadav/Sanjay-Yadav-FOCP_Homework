def pizzaCost(num, isDelivery, isTuesday, isUsedApp):
    pizzaPrice = 12.00*num
    deliveryPrice = 2.50
    tuesdayDiscount = float(50/100)
    appDiscount= float(25/100)
        
    if isDelivery.lower() == "y":
        if num >=5:
            deliveryPrice=0
        else:
            pizzaPrice+=deliveryPrice
            
    if isTuesday.lower() == "y":
        pizzaPrice *=(1- tuesdayDiscount)
        
        
    if isUsedApp.lower() == "y":
        pizzaPrice *=(1- appDiscount)
        
    return pizzaPrice

def main():
    print("BPP Pizza Price Calculator")
    print("==========================\n")
    while True:
        try:
            num =int(input("How many pizzas dordered? "))
            if num<=0:
                print("Please enter a positive integer!")
                continue  
            
            isDelivery = input("Is delivery required? ")
            if isDelivery.lower() != "y" and isDelivery.lower() != "n":
                print("Please enter y or n!")
                isDelivery = input("Is delivery required? ")

            isTuesday = input("Is it Tuesday? ")
            while isTuesday.lower() != "y" and isTuesday.lower() != "n":
                print("Please enter y or n!")
                isTuesday = input("Is it Tuesday? ")
  
            isUsedApp= input("Did the customer use the app? ")
            while isUsedApp.lower() != "y" and isUsedApp.lower() != "n":
                print("Please enter y or n!")
                isUsedApp= input("Did the customer use the app? ")

                    
            total=pizzaCost(num, isDelivery, isTuesday, isUsedApp)
            print(f"Total Price: ${total:.2f}")
            break
        except ValueError:
            print("Please enter a number!")
        

if __name__ == "__main__":
    main()