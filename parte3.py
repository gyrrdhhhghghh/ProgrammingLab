#list = [1,2,3]
#print(list[0:1])



file = open('shampoo_sales.csv', 'r')
file_content= file.read()
if len(file_content) > 50:
    print(file_content[0:50] + '...')
else:
    print(file_content)
file.close()

file = open('shampoo_sales.csv', 'r')
print(file.readline())
print(file.readline())
file.close()

file = open('shampoo_sales.csv', 'r')
for line in file:
    print(line)
file.close()

my_file = open('saluti.text', 'w')
my_file.write('hello world')
my_file.close()