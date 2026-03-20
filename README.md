##  OKCO ORDER MANAGEMENT SYSTEM

### DESCRIPTION

This project implements an Order Management System for the company OKCO. 

It allows users to enter customer orders, displays order history, and generate final reports summarizing sales and units sold by product. 

The interface is a console-based system designed to facilitate terminal-level operations without depending on external databases.

### SYSTEM ARCHITECTURE

The system follows a modular structure divided into different Python files, each one responsible for a specific aspect:

**• main.py:** Runs the program and calls the interactive menu.

**• interactive_menu.py:** Displays the menu options and handles user interaction.

**• order_creation.py:** Requests customer, product, and quantity data; calculates totals and stores orders.

**• order_history.py:** Generates a history of all recorded orders.

**• final_report.py:** Summarizes order information: total orders, total income, orders by customer and units sold by product.

**• customer_database and product_database.py:** Contain customer and product information using dictionaries that store tuples.

### INSTRUCTIONS FOR RUNNING THE PROGRAM

**1.** Make sure you have Python, VS Code, and the necessary extensions installed on your computer.

**2.** Download or clone all the project files into a folder.

**3.** Open the terminal, navigate to the project directory, and run *code .* to open VS Code.

**4.** Run the programm.

**5.** Navigate the menu by entering the corresponding numbers:

    1: Create order
    2: View order history
    3: Generate report
    4: Exit

### EXPLANATION OF THE DATA STRUCTURES USED

**Dictionaries (dict):** These are used as “databases” for customers and products, with IDs as keys and tuples as values.

    Customers: {customer_id: (name, email)}
    Products: {product_id: (name, price)}

**Tuples:** Store fixed information about customers and products (name, email/price).

**Nested dictionaries:** Orders are stored in a dictionary where the key is the order_id and the value is another dictionary containing order information, for example:

    orders = {
        order_id: {
            "customer": "Customer name",
            "product": "Product name",
            "quantity": 2,
            "price": 1200000,
            "total": 2400000
        }
    }

These structures allow for quick access by ID and make it easier to calculate totals and summaries.

### DESCRIPTION OF THE IMPLEMENTED MODULES

**order_creation.py**

+ Requests the user to select a customer and product using ID.
+ Validates that the inputs are correct.
+ Calculates the order total (unit_price × quantity).
+ Returns the updated order dictionary.

**order_history.py**

+ Iterates through all recorded orders.
+ Returns a formatted string displaying ID, customer, product, quantity, unit price, and total.

**final_report.py**

+ Generates a summary report of all orders:

  + Total orders.
  + Total revenue.
  + Number of orders per customer.
  + Units sold per product.

+ Returns a formatted string ready for printing.

**interactive_menu.py**

+ Displays an interactive menu with options to create an order, display history, generate a report, and exit.

+ Calls the corresponding functions according to the selected option.

**main.py**

+ Main file that initializes the orders dictionary and calls the interactive menu.

**customer_database.py and product_database.py**

+ Dictionaries containing static information about customers and products.

+ They serve as local “databases” for the system.