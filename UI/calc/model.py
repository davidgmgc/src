class Model:

    def __init__(self):
        pass

    def calculate_expression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except:
            result = 'OP NOT FOUND'

        return result