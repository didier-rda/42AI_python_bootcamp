def generator(text, sep=" ", option=None):
    if (option == "ordered"):
        words = text.split(sep)
        words.sort(key = lambda k : k.lower())
        for word in words:
            yield word
    if (option == "shuffle"):
        words = text.split(sep)
        shuffled_words = shuffle_(words)
        for word in shuffled_words:
            yield word
    if (option == None):
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


def lcg(modulus, a, c, seed):
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

def random_(end):
    x = lcg(2**32, 134775813, 1, 100)
    while True:
        yield next(x) % end
    
def shuffle_(list_):
    """Shuffles a list"""
    def look_for_None_space(list_):
        """Return the index of the first None element in a list"""
        for (idx, element) in enumerate(list_):
            if (element == None):
                return idx

    response = [None] * len(list_)
    r_gen = random_(len(list_))
    for element in list_:
        r = next(r_gen)
        if (response[r] == None):
            response[r] = element
        else:
            r = look_for_None_space(response)
            response[r] = element
    return response
            

# -----------------------------------
#     -- first iter:  r: 2
#                     element: "a"
#                     response: [None, None, "a", None]
#     -- second iter: r: 0
#                     element: "b"
#                     response: ["b", None, "a", None]
#     -- third iter:  r: 2
#                     element: "c"
#                     response: ["b", "c", "a", None]
#     -- fourth iter: r: 2
#                     element: "d"
#                     response: ["b", "c", "a", "d"]




def ft_split():
    pass
