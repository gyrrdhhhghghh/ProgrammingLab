class MovingAverage():
    def __init__(self, window_size):
        is_float = isinstance(window_size, float)
        if is_float is True:
            raise ExamException('window non può essere numero decimale')
        x = isinstance(window_size, str)
        if x is True:
            raise ExamException('window non puo essere una string')
        if window_size == None:
            raise ExamException('window non può essere none')
        if window_size <=0:
            raise ExamException('window non può essere 0 o negativa')
        self.window_size = window_size

    def compute(self, array):
        is_list = isinstance(array, list)
        if is_list is False:
            raise ExamException('string dentro array')
        for i in array:
            x = isinstance(i, str)
            if x is True:
                raise ExamException('array contiene strings')
        if self.window_size>len(array):
            raise ExamException('array troppo corto')
        if len(array) == 1:
            return array
        list_moving_averages = []
        i = 0
        while len(array)>= i+self.window_size:
            window = array[i:i+self.window_size]
            print(window)
            i=i+1
            average_window_x = sum(window)/self.window_size
            list_moving_averages.append(average_window_x)
        return list_moving_averages

class ExamException(Exception):
    pass