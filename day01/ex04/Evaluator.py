class Evaluator:
    '''''has two static functions named: zip_evaluate and enumerate_evaluate.'''

    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        sum_zip = 0 
        for word, coef in zip(words, coefs):
            sum_zip += len(word)*coef
        return sum_zip


    @staticmethod
    def enumerate_evaluate(coefs, words): 
        if len(coefs) != len(words):
            return -1
        sum_enum = 0
        for ix, values in enumerate(zip(words, coefs)):
            sum_enum += len(values[0])*values[1]
        return sum_enum
