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
