class CSVFile():
    def __init__(self, name):
        self.name = name
        self.non_vuoto = True
        try:
            file = open(self.name, 'r')
            file.readline()
        except Exception as e:
            self.non_vuoto = False
            print('Errore, file vuoto: {}'.format(e))

    def get_data(self):
        if self.non_vuoto == False:
            print('Errore, dati non accessibili')
            return None
        else:
            data = []
            file = open(self.name, 'r')
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