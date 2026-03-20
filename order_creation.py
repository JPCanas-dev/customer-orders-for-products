from customer_database import customers
from product_database import products


def register_order(orders):

        # ===== CUSTOMER =====

        print("\n=== CUSTOMER DATABASE ===\n")
        for customer_id, customer in customers.items():
            # customer is a tuple: (name, email)
            print(f"ID: {customer_id}")
            print(f"Name: {customer[0]}")
            print(f"Email: {customer[1]}")
            print("----------------------")

        customer_exists = 0

        while customer_exists == 0:
            try:
                customer_id = int(input("\nEnter customer ID: "))

                if customer_id in customers:
                    customer_exists = 1
                else:
                    print("Customer not found. Please try again.")

            except ValueError:
                print("Please enter a valid number with no spaces.")

        customer_name = customers[customer_id][0]  # index 0 = name

        # ===== PRODUCT =====

        print("\n=== PRODUCT DATABASE ===\n")
        for product_id, product in products.items():
            # product is a tuple: (name, price)
            print(f"ID: {product_id}")
            print(f"Name: {product[0]}")
            print(f"Price: ${product[1]:,}")
            print("----------------------")

        product_exists = 0

        while product_exists == 0:
            try:
                product_id = int(input("\nEnter product ID: "))

                if product_id in products:
                    product_exists = 1
                else:
                    print("Product not found. Please try again.")

            except ValueError:
                print("Please enter a valid number with no spaces.")

        product_name = products[product_id][0]  # index 0 = name
        unit_price   = products[product_id][1]  # index 1 = price

        # ===== QUANTITY =====

        correct_quantity = 0
        while correct_quantity == 0:
            try:
                quantity = int(input("Enter the amount: "))
                if quantity <= 0:
                    print("\nPlease enter only postive numbers")
                else:
                    correct_quantity = 1
            except ValueError:
                print("\nPlease enter only integer numbers")

        # ===== TOTAL =====

        total = unit_price * quantity

        order_id = len(orders) + 1
        orders[order_id] = {
            "customer": customer_name,
            "product":  product_name,
            "quantity": quantity,
            "price":    unit_price,
            "total":    total
        }

        print(f"\nOrder registered!\nTotal: ${total:,} COP")
        return orders

   
  



