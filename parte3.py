#list = [1,2,3]
#print(list[0:1])


file = open('shampoo_sales.csv', 'r')
print(file.read()[0:3])
file.close()