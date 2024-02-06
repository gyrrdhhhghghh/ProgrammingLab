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

class NumericalCSVFile(CSVFile):
    def get_data(self):
        dati_string = super().get_data()
        dati_float = []
        #split() ritorna un array che contiene string
        #in questo caso, la prima stringa è la data, la seconda i sales
        #quindi l'elemento 0 posso buttarlo
        #l'elemento 1 lo trasformo in float e append al data_int
        for line in dati_string:
            try:
                sales_numerico = float(line[1])
                new_line = []
                new_line.append(line[0])
                new_line.append(sales_numerico)
                dati_float.append(new_line)
            except Exception as e:
                print('Errore: {}'.format(e))
        return dati_float