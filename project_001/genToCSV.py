import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Number of orders 
n_rows = 10

# Example products and price
products = [
    ('Wireless Mouse', 25.99),
    ('USB-C Hub', 45.50),
    ('Mechanical Keyboard', 89.90),
    ('Gaming Monitor', 249.99),
    ('Laptop Stand', 19.99),
    ('Noise-Cancelling Headphones', 129.50),
    ('Webcam', 39.95),
    ('HDMI Cable', 7.99),
    ('Smartphone Holder', 12.49),
    ('Portable SSD', 99.99)
]

rows = []

for i in range(0, n_rows + 1):
    customer_name = fake.name()
    product, price = random.choice(products)   # Random product choice 
    price = round(85 * price, 2)               # Сonversion to local currency
    quantity = random.randint(1, 4)            # Quantity of product purchased
    total = round(price * quantity, 2)         # Totally of product purchased
    order_date = fake.date_between(start_date='-90d', end_date='today')
    
    rows.append([0 + i, customer_name, product, quantity, price, total, order_date])

# Create DataFrame
columns = ['order_id', 'customer_name', 'product', 'quantity', 'price', 'total', 'order_date']
df = pd.DataFrame(rows, columns=columns)

# Save to CSV
df.to_csv('D:\MyVSProjects\python\data_analist\Task_day\sales.csv', index=False)
print("(+) Random sales.csv generated!")
