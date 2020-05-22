#!/usr/bin/python3
"""
this text_indentation module contains only text_indentation()
"""


def text_indentation(text):
    """
    Print a text with 2 newlines after the characters: .?:
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    cont = False
    for x in text.strip(' '):
        if cont:
            cont = False
            continue
        if x in '.?:':
            print('{}\n\n'.format(x), end='')
            cont = True
        else:
            print(x, end='')

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
