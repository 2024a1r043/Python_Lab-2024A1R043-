#with lambda
orders= [
    ("Order-A", 45),
    ("Order-B", 20),
    ("Order-C", 35),
    ("Order-D", 15)
]

sorted_orders = sorted(
    orders,
    key=lambda order:order[1]
)

print("Orders by delivery time:")

for order_name,minutes in sorted_orders:
    print(order_name, "-", minutes, "minutes")