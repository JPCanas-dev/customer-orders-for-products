def register_products():

    client_name = str (input("Enter your name: "))
    product_name=str(input("Enter the product name: "))

    correct_quantity = 0
    while correct_quantity == 0:
        try:
            quantity=int(input("Enter the amount: "))
            correct_quantity = 1
        except ValueError:
            print("_"*40)
            print("Please enter only integers numbers")
            print("_"*40)
    total= unit_price*quantity        

    return client_name, product_name, total, quantity
    


   
  



