def sum_csv(file_name):
    file = open(file_name, 'r')
    sales = []
    any = False
    for line in file:
        value = line.split(',')[1]
        clean_values = value.strip('\n')
        if clean_values == 'Sales':
            continue
        try:
            num_values= float(clean_values)
            sales.append(num_values)
            any = True
        except Exception as e:
            print('c''è un errore: {}'.format(e))
    file.close()
    if any == False:
        return None
    else:
        return sum(sales)

#print(sum_csv('ciao.txt'))