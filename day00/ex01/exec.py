def ft_exec(*args):
    import sys
    args_join = ' '.join(sys.argv[1:])
    reverse = args_join[::-1]
    ix = 0
    uplow = []

    for i in list(map(lambda letter: letter.isupper(), reverse)):
        if(i):
            uplow.append(reverse[ix].lower())
        else:
            uplow.append(reverse[ix].upper())
        ix += 1
    print(''.join(uplow))


if __name__ == '__main__':
    ft_exec()
