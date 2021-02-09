from collections import deque

customers = deque(int(num) for num in input().split(", "))
taxi_drivers = deque(int(num) for num in input().split(", "))
total_time = 0
while customers and taxi_drivers:
    customer = customers.popleft()
    driver = taxi_drivers.pop()
    if customer > driver:
        customers.appendleft(customer)
        continue
    total_time += customer
if customers or taxi_drivers:
    print("Not all customers were driven to their destinations")
    print("Customers left:", end=" ")
    print(*customers, sep=", ")
else:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")