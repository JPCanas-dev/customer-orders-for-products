def calculate_daily_income(orders):
    total_income = 0

    for order_id in orders:
        order = orders[order_id]
        total_income += order["total"]

    return total_income