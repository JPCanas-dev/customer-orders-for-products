from order_creation import register_order
from order_history  import view_orders
from final_report   import final_report

# Display the main menu and handle user interaction.

def menu(orders):

    end_menu = 0 # Controls loop execution

    while end_menu == 0:

        print("\n1. Create order")
        print("2. Display order history")
        print("3. Generate report")
        print("4. Exit")

        option = input("\nPlease select an option: ")

        if option == "1":
            # Add a new order
            orders = register_order(orders)

        elif option == "2":
            # Display order history
            result = view_orders(orders)
            print(result)

        elif option == "3":
            # Display summary report
            print(final_report(orders))

        elif option == "4":
            # Exit While loop
            end_menu = 1

        else:
             # Any invalid input
            print("Please enter a valid value")

    return "\nTHANK YOU FOR USING OUR SERVICES!\n"