class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    
    def predict(self):
        raise NotImplementedError('Metodo non implementato')

class FitTrendModel(Model):
    
    def fit(self, array):
        self.array = array
        is_list = isinstance(array, list)
        if is_list is False:
            raise TypeError('Errore: string dentro array')
        if len(array) < 2:
            raise Exception('Errore: array troppo corto')
        lunghezza = len(array)
        variazioni = []
        for i in range(1, lunghezza):
            x = isinstance(i, int)
            if x is False:
                raise Exception('Errore: i non è int')
            variazioni.append(array[i]-array[i-1])
        media_variazioni = sum(variazioni)/(lunghezza-1)
        self.historical_avg_variation = media_variazioni

    def predict(self):
        return self.array[-1]+self.historical_avg_variation