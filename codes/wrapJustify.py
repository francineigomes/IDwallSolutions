# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:38:22 2018

@author: francinei
"""
import re, textwrap

def items_len(l):
    return sum([ len(x) for x in l] )

lead_re = re.compile(r'(^\s+)(.*)$')

#%%

def justify_string(s, width, last_line=0):
    '''
    align string to specified width 
    '''
    # detect and save leading whitespace
    m = lead_re.match(s) 
    if m is None:
        left, right, w = '', s, width
    else:
        left, right, w = m.group(1), m.group(2), width - len(m.group(1))

    items = right.split()

    # add required space to each words, exclude last item
    for i in range(len(items) - 1):
        items[i] += ' '

    if not last_line:
        # number of spaces to add
        left_count = w - items_len(items)
        while left_count > 0 and len(items) > 1:
            for i in range(len(items) - 1):
                items[i] += ' '
                left_count -= 1
                if left_count < 1:  
                    break

    res = left + ''.join(items)
    return res

#%%
def text_wrapper_justified(text, line_width = 40):
    justified = ''
    text_wrapper_object = textwrap.TextWrapper(width = line_width)
    wrapped_lines = text_wrapper_object.wrap(text)

    while len(wrapped_lines) > 0:
        line = wrapped_lines.pop(0)
        last_line = 0
        aligned = justify_string(line, line_width, last_line)
        justified += '\n' + aligned
        
    return text_wrapper_object.fill(text), justified


#%%
'''
s = 'Contributors whose recipes are used in the book will receive a complimentary copy of the Second Edition. A portion of all royalties will go to the non-profit Python Software Foundation. [Last words]'
texto_1 = 'In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.' 
texto_2 = 'And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'

width = 20
saida = text_wrapper_justified(texto_2, width)
print(saida[0])
print('\n'+'-'*width+'\n')
print(saida[1])

'''
#%%








