''' A Huffman encoder program
    Copyright (C) 2026 HippoProgrammer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''

print(''' huffman-coding.py  Copyright (C) 2026  HippoProgrammer
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions.''')
try:
    import numpy as np
except ImportError:
    print('This program needs to be run with a venv activated! numpy needs to be installed.')
    exit()
finally:
    print('venv detected, numpy loaded successfully')
text = input('Text:')
def create_tree_from_text(text:str): 
    text_chars = list(text) # split text into chars
    frequency_table = dict() # create frequency table
    for char in text_chars: # count chars and store in table
        if char in list(frequency_table.keys()):
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
    indices = np.argsort(list(frequency_table.values())) # get indices to sort by values
    sorted_frequency_table = {list(frequency_table.keys())[i]: list(frequency_table.values())[i] for i in indices} # use indices to generate a sorted table
    # here a tree needs to be created.... somehow
