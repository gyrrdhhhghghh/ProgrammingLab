class CSVFile():
    def __init__(self, name):
        #codice aggiunto qui
        self.name = name
        bool_str = isinstance(name, str)
        if bool_str == False:
            raise Exception ('Errore, nome del file non valido')
        #fine codice aggiunto
        self.non_vuoto = True
        try:
            file = open(self.name, 'r')
            file.readline()
        except Exception as e:
            self.non_vuoto = False
            print('Errore, file vuoto: {}'.format(e))

    def get_data(self, start = None, end = None):
        if self.non_vuoto == False:
            print('Errore, dati non accessibili')
            return None
        else:
            data = []
            file = open(self.name, 'r')
            #codice aggiunto
            start_good = start is None or isinstance(start, int)
            end_good  = end is None or isinstance(end, int)
            if start_good == False or end_good == False:
                raise Exception('Errore, valore di start / end non valido')
            if end is None and start<=0:
                raise Exception('Errore, start non valido')
            if start is None and end <=0:
                raise Exception('Errore, end non valido')
            if start > end:
                raise Exception('Errore, start maggiore di end, non valido')
            file_range = end-start
            for line in file_range:
                #fine codice aggiunto
                if 'Date' in range(start, end):
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