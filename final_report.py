def final_report(orders):
    total_orders = 0
    total_income = 0
    clients = {}
    products = {}
    for order_id, order in orders.item():
        total_orders += 1
        total_income += order["total"]

        client = order["client"]
        product = order["product"]
        quantity = order["quantity"]

        if client not in clients:
            clients[client] = 0
            clients[client] += order["total"]

        if product not in products:
            products[product] = 0
            products[product] += quantity

    report = (
        total_orders,
        total_income,
        clients,
        products
        
    )
    return report