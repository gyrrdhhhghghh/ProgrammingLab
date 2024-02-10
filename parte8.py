import statistics

def variazione_media(array, n):
    variazioni = []
    for i in range(0, (len(array))-2):
        variaz = array[i+1] - array[i]
        variazioni.append(variaz)
    variazione_mesi_da_considerare = []
    for j in range( (len(variazioni))-n, (len(variazioni))-1):
        variazione_mesi_da_considerare.append(variazioni[j])
    media_n_variazioni = statistics.mean(variazione_mesi_da_considerare)
    return media_n_variazioni