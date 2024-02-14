class ExamException(Exception):
    pass

#ricordarsi di scrivere tutti gli errori o in ita o in ing, non entrambi 

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name

    def get_data(self):
        
        # controllo se il file è leggibile
        try:
            file = open(self.name, 'r')
        except Exception:
            raise ExamException('Errore, file illeggibile')
        
        # creo un array dove mettere gli altri array
        data = []

        # metto anno e mese precedente che poi servono per
        # controllare se i timestamp sono ordinati
        anno_precedente = 0
        mese_precedente = 0
        for line in file:
            if('date,passengers' in line):
                continue
           
            arr = []
            
            # pulisco la riga e separo date e passeggeri
            stripped = line.strip('\n')
            values = stripped.split(',')
            
            # se manca o la data o i passeggeri, continuo senza alzare eccezioni
            if len(values) < 2:
                print("len(values) < 2")
                continue

            # se manca l'anno o il mese, continuo senza alzare eccezioni
            date_part = values[0] # e.g. '1900-02'
            date_array = date_part.split('-') #['1900', '02']
            if len(date_array) < 2:
                print("len(date_array) < 2")
                continue

            # controllo che il mese sia un int
            try:
                mese = int(date_array[1])
            except:
                continue

            # controllo che l'anno sia un int
            try:
                anno = int(date_array[0])
            except:
                continue

            # se si volesse, si potrebbe anche limitare l'anno
            # che sia > 0 oppure > dell'anno in cui hanno inventato l'aereo

            # se il mese non è compreso tra 1 e 12, continuo
            if mese not in range(1, 13):
                continue

            # controllo che la timestamp sia ordinata
            if anno < anno_precedente:
                raise ExamException('Errore, timestamp non ordinato')
            
            # in questo caso, devo anche dire che anno == anno_precedente perchè
            # se ho 1950-12 e poi 1951-01 scatterebbe l'errore,
            # mentre invece non è un errore
            if mese < mese_precedente and anno == anno_precedente:
                raise ExamException('Errore, timestamp non ordinato')
            
            if anno == anno_precedente and mese == mese_precedente:
                raise ExamException('Errore, timestamp duplicato')
            
            # avrei anche potuto scrivere:
            # if mese <= mese_precedente and anno == anno_precedente:
            # raise ExamException('Errore, timestamp non ordinato o duplicato')

            # controllo che il numero dei passeggeri sia un intero
            # così vengono ignorati float, string e vuoti
            passengers_part = values[1]
            try:
                int_passengers = int(passengers_part)
            except:
                print("int_passengers = int({})".format(passengers_part))
                continue

            # controllo che il numero dei passeggeri sia positivo
            if int_passengers < 0:
                print('{} < 0'.format(int_passengers))
                continue

            # inserisco i valori nel nested array
            arr.append(values[0])
            arr.append(int(values[1]))
            data.append(arr)

            anno_precedente = anno
            mese_precedente = mese
        
        # inserisco qui quando devo continuare (vedi esame2.py)
        file.close()
        return data

def compute_increments(time_series, first_year, last_year):
    
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
        # Se invece l’intervallo considerato è di soli 
    # due anni e per uno dei due anni non abbiamo misurazioni,
    # l’output sarà una lista vuota. 
    
    if int_last_year == int_first_year+1:
        if int_last_year not in valori_per_anno or int_first_year not in valori_per_anno:
            print("int_last_year == int_first_year+1")
            return []
            
    print(valori_per_anno)

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


x = CSVTimeSeriesFile('voli_anno_duplicato.csv')
y = x.get_data()
print(compute_increments(y, "1949", "1950"))