end_menu = 0

def menu (end_menu):
    print("1. Create order")
    print("2. Display order history")
    print("3. Generate report")
    print("4. Exit")

    option = input("Please select an option")

    while end_menu == 0:

        if opcion == "1":
                create

        elif opcion == "2":
            retirar(obtener_valor_saldo())

        elif opcion == "3":
            depositar(obtener_valor_saldo())

        elif opcion == "4":
            mostrar_historial()

        else:
            print("Opción no válida")