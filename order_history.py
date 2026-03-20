def view_orders(orders):

    # Initialize the result string with a header for order history
    result = "\n============================\n"
    result += "       ORDER HISTORY\n"
    result += "============================\n"

    # Check if there are no orders registered
    if len(orders) == 0:
        return "No orders registered"

    # Iterate over each order in the orders dictionary
    for order_id in orders:
        order = orders[order_id]

        # Extract order details
        customer = order["customer"]
        product = order["product"]
        quantity = order["quantity"]
        price = order["price"]

        # Calculate total price for the order
        total = price * quantity

        # Add order details to the result string
        result += f"\nOrder ID: {order_id}\n"
        result += f"Customer: {customer}\n"
        result += f"Product: {product}\n"
        result += f"Quantity: {quantity}\n"
        result += f"Unit price: {price}\n"
        result += f"Total: {total}\n"
        result += "----------------------------\n"

    # Return the complete formatted order history
    return result
    