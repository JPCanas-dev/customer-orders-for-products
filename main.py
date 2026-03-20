from interactive_menu import menu

orders = {}

if __name__ == "__main__":
    print("")
    print("=" * 50)
    print("   WELCOME TO THE OKCO ORDER MANAGEMENT SYSTEM")
    print("=" * 50)
    end_message = menu(orders)
    print(end_message)
