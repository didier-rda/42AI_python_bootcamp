from randon import randon


def generator(text, sep=" ", option=None):
    count = 0
    for ix, char in enumerate(text):
        if char == sep or ix == len(text) - 1:
            if(char == sep):
                sliced_char = text[count:(ix)]
                count = ix+1
                yield sliced_char
            else:
                sliced_char = text[count:(ix+1)]
                count = ix+1
                yield sliced_char


def randon_(list_):
    pass


def ft_split():
    pass
