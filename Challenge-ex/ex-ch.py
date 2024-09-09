
with open('fruit_transactions.txt', 'r') as file:
    
    lines = file.readlines()
processed_data = []
for line in lines:
    
    name, action, quantity, item, price = line.strip().split(',')
    quantity = int(quantity)
    price = float(price)
    processed_data.append((name, action, quantity, item, price))
total_sales = 0
for entry in processed_data:
    name, action, quantity, item, price = entry
    if action == 'sold':
        total_sales += quantity * price
print(f"Total sales: ${total_sales:.2f}")
fruit_counts = {}
for entry in processed_data:
    item = entry[3]
    
   
    if item in fruit_counts:
        fruit_counts[item] += 1
    else:
        fruit_counts[item] = 1
most_popular_fruit = max(fruit_counts, key=fruit_counts.get)
print(f"Most popular fruit: {most_popular_fruit} with {fruit_counts[most_popular_fruit]} transactions")
total_value = 0
total_transactions = 0
for entry in processed_data:
    quantity, price = entry[2], entry[4]
    total_value += quantity * price
    total_transactions += 1
average_value = total_value / total_transactions
print(f"Average transaction value: ${average_value:.2f}")
spender_totals = {}
for entry in processed_data:
    name, action, quantity, price = entry[0], entry[1], entry[2], entry[4]
    
    if action == 'bought':
        if name in spender_totals:
            spender_totals[name] += quantity * price
        else:
            spender_totals[name] = quantity * price

biggest_spender = max(spender_totals, key=spender_totals.get)
print(f"Biggest spender: {biggest_spender} with a total of ${spender_totals[biggest_spender]:.2f}")
with open('transaction_summary.txt', 'w') as summary_file:
  
    summary_file.write(f"Total sales: ${total_sales:.2f}\n")
    summary_file.write(f"Most popular fruit: {most_popular_fruit} with {fruit_counts[most_popular_fruit]} transactions\n")
    summary_file.write(f"Average transaction value: ${average_value:.2f}\n")
    summary_file.write(f"Biggest spender: {biggest_spender} with a total of ${spender_totals[biggest_spender]:.2f}\n")

