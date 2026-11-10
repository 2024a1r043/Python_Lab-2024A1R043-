orders = [
    ("Order-A", 45),
    ("Order-B", 20),
    ("Order-C", 35),
    ("Order-D", 15)
]

def get_delivery_time(order):
    return order[1]

sorted_orders = sorted(
    orders,
    key=get_delivery_time
)

print("Orders by delivery time:")

for order_name, minutes in sorted_orders:
    print(order_name, ":", minutes, "minutes")