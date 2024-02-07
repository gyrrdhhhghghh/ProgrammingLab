#calcolo variazione media
import statistics

#dati = [3,7,4,22,6,8,9,3,33,33,6]
dati = [1,1,1,1,1,1,1]

def variazione_media(array, n):
    variazioni = []
    for i in range(0, (len(array))-2):
        variaz = array[i+1] - array[i]
        variazioni.append(variaz)
    print(variazioni)
    variazione_mesi_da_considerare = []
    for j in range( (len(variazioni))-n, (len(variazioni))-1):
        variazione_mesi_da_considerare.append(variazioni[j])
    print(variazione_mesi_da_considerare)
    media_n_variazioni = statistics.mean(variazione_mesi_da_considerare)
    return media_n_variazioni

#variazione_media(dati, 3)