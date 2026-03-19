# Final report function for customer orders
from customer_database import customers
from product_database import products

# This function generates a final report summarizing the total orders, total income,
def final_report(orders):

# Check if there are any orders to report
    if len(orders) == 0:
        return "\nNO ORDERS TO REPORT!\n"
    
# Initialize summary variables
    total_orders = 0
    total_income = 0
    clients_summary = {}
    products_summary = {}

# Process each order to build the summaries
    for order in orders.values():
        total_orders += 1
        total_income += order["total"]

        customer_name = order["customer"]
        product_name  = order["product"]
        quantity      = order["quantity"]
        total         = order["total"]

        # Orders count by customer
        if customer_name not in clients_summary:
            clients_summary[customer_name] = {"total_orders": 0}
        clients_summary[customer_name]["total_orders"] += 1

        # Units summary by product
        if product_name not in products_summary:
            products_summary[product_name] = {"total_quantity": 0}
        products_summary[product_name]["total_quantity"] += quantity

    # Build the report string
    report  = "\n========== FINAL REPORT ==========\n"
    report += f"Total orders : {total_orders}\n"
    report += f"Total income : ${total_income:,} COP\n"

    report += "\n--- Orders by customer ---\n"
    for customer_name, data in clients_summary.items():
        report += f"  {customer_name}: {data['total_orders']} orders\n"

    report += "\n--- Units sold by product ---\n"
    for product_name, data in products_summary.items():
        report += f"  {product_name}: {data['total_quantity']} units\n"

    report += "==================================\n"

    return report