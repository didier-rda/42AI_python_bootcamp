import sys


def calc(num1, num2):
    print(num1 + num2)
    print('Sum:             {}'.format(num1 + num2))
    print('Difference:      {}'.format(num1 - num2))
    print('Product          {}'.format(num1 * num2))
    try:
        print('Quotient         {}'.format(num1 / num2))
        print('Remainder        {}'.format(num1 % num2))
    except ZeroDivisionError:
        print('Quotient         ERROR (div by zero)')
        print('Remainder        ERROR (modulo by zero)')


def validate(args):
    error = False
    if len(args) > 2:
        print("InputError: too many arguments")
        error = True
    if not type(eval(args[0])) == int or not type(eval(args[1])) == int:
        print("InputError: only numbers")
        error = True
    if error:
        print("\nUsage: python operations.py < number1 > <number2 >")
        print("Example:\npython operations.py 10 3")
        return
    calc(int(args[0]), int(args[1]))


if __name__ == "__main__":
    args = sys.argv[1:]
    validate(args)
