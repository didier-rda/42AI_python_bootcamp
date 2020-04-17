class Vector:
    def __init__(self, values):
        self.values = values
        self.size = len(values)

    
    def __mul__(self, number):
        return Vector(list(map(lambda x: x * number, self.values)))

    
    def __str__(self):
        return '(Vector {})'.format(self.values)

    
    def __add__(self, vector):
        if not self.size == vector.size:
            raise Exception('AAAA')
        # sum_values = []
        # x = self.size if self.size < vector.size else vector.size
        # for i in range(x):
        #     sum_values.append(self.values[i] + vector.values[i])
        # return Vector(sum_values)

            
    # def __radd__(self, value):
    #     pass

    # def __sub__(self, value):
    #     pass

    # def __rsub__(self, value):
    #     pass

    # def __truediv__(self, value):
    #     pass

    # def __rtruediv__(self, value):
    #     pass

    # def __rmul__(self, value):
    #     pass

    # def __repr__(self):
    #     pass
