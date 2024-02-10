class Model():
    pass

class TrendModel(Model):
    def predict(self, array):
        is_list = isinstance(array, list)
        if is_list is False:
            raise TypeError('Errore: string dentro array')
        if len(array) < 2:
            raise Exception('Errore: array troppo corto')
        n=3
        lunghezza = len(array)
        variazioni = []
        for i in range(lunghezza-n+1, lunghezza):
            x = isinstance(i, int)
            if x is False:
                raise Exception('Errore: i non è int')
            variazioni.append(array[i]-array[i-1])
        media_variazioni = sum(variazioni)/(n-1)
        return array[-1]+media_variazioni