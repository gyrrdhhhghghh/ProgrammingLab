file = open('shampoo_sales.csv', 'r')
sales = []
for line in file:
    value = line.split(',')[1]
    clean_values = value.strip('\n')
    if clean_values == 'Sales':
        continue
    num_values= float(clean_values)
    sales.append(num_values)

print(sales)
file.close()
