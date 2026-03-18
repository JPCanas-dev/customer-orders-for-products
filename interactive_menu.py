end_menu = 0

def menu (end_menu):

    while end_menu == 0:

        print("1. Create order")
        print("2. Display order history")
        print("3. Generate report")
        print("4. Exit")

        option = input("Please select an option: ").strip()

        if option == "1":
            create_order()

        elif option == "2":
            view_orders = order_history()
            print(view_orders)
             
        elif option == "3":
            generate_report = final_report()
            print(generate_report)

        elif option == "4":
            end_menu = 1
            print("Thank you for using our services!")

        else:
            print("Please enter a valid value")