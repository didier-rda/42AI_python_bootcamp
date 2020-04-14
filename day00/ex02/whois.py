import sys


def ft_odd_even_zero(num):
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def ft_whois(*args):

    if (len(sys.argv) == 2 and sys.argv[1].isnumeric()):
        ft_odd_even_zero(int(sys.argv[1]))
    elif(len(sys.argv) == 1):
        pass
    else:
        print('ERROR')


if __name__ == '__main__':
    ft_whois()
