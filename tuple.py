# Sales data tuple for different products
sales_data = (
    ("ProductA", 100, 25.50),  # Product, Quantity Sold, Price per Unit
    ("ProductB", 50, 30.75),
    ("ProductC", 75, 15.90),
    ("ProductD", 120, 10.25),
)

# Displaying the sales data
print("Sales Data:")
for product in sales_data:
    print(f"Product: {product[0]}, Quantity Sold: {product[1]}, Price per Unit: ${product[2]:.2f}")

# Calculating total sales
total_sales = sum(quantity * price for _, quantity, price in sales_data)
print("\nTotal Sales: ${:.2f}".format(total_sales))

# Finding the product with the highest price per unit
max_price_product = max(sales_data, key=lambda x: x[2])
print("\nProduct with the Highest Price per Unit:", max_price_product[0])
