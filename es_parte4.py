class CSVFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        file = open(self.name, 'r')
        data = []
        for line in file:
            if 'Date' in line:
                continue
            stripped = line.strip('\n')
            values= stripped.split(',')
            data.append(values)
        file.close()
        return data

#shampoo = CSVFile('shampoo_sales.csv')
#print(shampoo.get_data())