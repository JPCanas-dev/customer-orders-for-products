def view_orders(orders):
    result = "\n============================\n"
    result += "       ORDER HISTORY\n"
    result += "============================\n"

    if len(orders) == 0:
        return "No orders registered"

    for order_id in orders:
        order = orders[order_id]

        customer = order["customer"]
        product = order["product"]
        quantity = order["quantity"]
        price = order["price"]

        total = price * quantity

        result += f"\nOrder ID: {order_id}\n"
        result += f"Customer: {customer}\n"
        result += f"Product: {product}\n"
        result += f"Quantity: {quantity}\n"
        result += f"Unit price: {price}\n"
        result += f"Total: {total}\n"
        result += "----------------------------\n"

    return result
    