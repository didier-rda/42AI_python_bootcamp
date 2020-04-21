import re

def text_analyzer(*args):  
    """This function counts the number of upper characters, lower characters,punctuation and spaces in a given text."""
    if not len(args):
        print('What is the text to analyse?')
        return
    if not len(args) == 1:
        print('ERROR')
        return
    text = args[0]
    n_char = len(text)
    n_up = len(re.findall(r"[A-Z]", text))
    n_low = len(re.findall(r"[a-z]", text))
    n_punc = len(re.findall(r"[.,\/#!$%\^&\*;:{}=\-_`~()']", text))
    n_spaces = len(re.findall(r"\s", text))
    ft_print_summary(n_char, n_up, n_low, n_punc, n_spaces)


def ft_print_summary(n_char, n_up, n_low, n_punc, n_spaces):
    text = f'The text contains {n_char} characters:\n'
    text += f'- {n_up} upper letters\n'
    text += f'- {n_low} lower letters\n'
    text += f'- {n_punc} punctuation marks\n'
    text += f'- {n_spaces} spaces'
    print(text)
