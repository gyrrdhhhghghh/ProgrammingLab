class ExamException(Exception):
    pass

#ricordarsi di scrivere tutti gli errori o in ita o in ing, non entrambi 

class CSVTimeSeriesFile():
    def __init__(self, file):
        self.file = file

    def get_data(self):
        
        # controllo se il file è leggibile
        try:
            file = open(self.file, 'r')
        except Exception:
            raise ExamException('Errore, file illeggibile')
        
        # creo un array dove mettere gli altri array
        data = []
        for line in file:
            if('date,passengers' in line):
                continue
            arr = []
            
            # pulisco la riga e separo date e passeggeri
            stripped = line.strip('\n')
            values = stripped.split(',')

            # qui controllo la bontà dei dati
            #        if int_mese not in range(1, 13):
            # rai
            # per esempio che i mese sia compreso tra 1 e

            
            # inserisco i valori nel nested array
            arr.append(values[0])
            arr.append(int(values[1]))
            data.append(arr)
        
        # inserisco qui quando devo continuare (vedi esame2.py)
        file.close()
        return data

def compute_increments(time_series, first_year, last_year):
    
    # se gli anni sono n, il dizionario ha n-1 valori
        #controllo se ci sono errori negli input
    if isinstance(time_series, list) is False:
        raise ExamException('Errore, time_series non è una lista')
    
    if isinstance(first_year, str) is False:
        raise ExamException('Errore, first_year non è una str')
    
    if isinstance(last_year, str) is False:
        raise ExamException('Errore, last_year non è una str')
    
    try:
        int_first_year = int(first_year)
        int_last_year = int(last_year)
    except:
        raise ExamException('Errore, conversione a int fallita')

    if int_first_year is None  or int_last_year is None:
        raise ExamException('Errore, first_year or last_year is None')

    if int_first_year > int_last_year:
        raise ExamException('Errore, first_year > last_year')
    
    if int_first_year < 0 or int_last_year < 0:
        raise ExamException('Errore, first_year or last_year is less than zero')

    # (?) non controllo i duplicati perchè poi userò un dizionario
    # che li elimina automaticamente (?)

    # ora divido in anni e mesi
    valori_per_anno = {}
    for element in time_series:
        date = element[0]
        anno_e_mese = date.split('-')
        int_anno = int(anno_e_mese[0])
        int_mese = int(anno_e_mese[1])

        if not int_anno in valori_per_anno:
            valori_per_anno[int_anno] = [element[1]]
        else:
            valori_per_anno[int_anno].append(element[1])
        # esempio:
        # valori_per_anno = {1990: [44, 432, 344, 34], 1991: [200, 340, 120]}
        # la key è l'anno, il valore sono i passeggeri
            
    media_per_anni = {}
    for key in valori_per_anno:
        m = valori_per_anno[key]
        media_per_anni[key] = sum(m)/len(m)
        # esempio:
        # media_per_anni = {1990: 120.666, 1991: [200.0]}
        # la key è l'anno, il valore è la media
    
    result = {}
    previous_key = 0
    for key in media_per_anni:
        if key< int_first_year:
            continue
        if key > int_last_year:
            break
        if key > int_first_year:
            result['{}-{}'.format(previous_key, key)] = media_per_anni[key]-media_per_anni[previous_key]
        previous_key = key

    return result


x = CSVTimeSeriesFile('voli_noerrori.csv')
y = x.get_data()
print(compute_increments(y, "1949", "1952"))