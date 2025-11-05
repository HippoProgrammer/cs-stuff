from math import ceil
def strArrayBuilder(prompt:str, loops:int):
    array = []
    for i in range(loops):
        array.append(str(input(prompt)))
    return array
def arrayOppositeIndexFinder(array:list,index:int):
    return len(array) - 1 - index # subtract one to get final index, then subtract starting index
def palindromeChecker(word:str):
    wordChars = list(word)
    isPalindrome = True
    for charIndex in range(ceil(len(wordChars) / 2)):
        if wordChars[charIndex] != wordChars[arrayOppositeIndexFinder(wordChars,charIndex)]:
            isPalindrome = False
            break
    return isPalindrome
items = int(input('Number of words: '))
words = strArrayBuilder('Word: ',items)
palindromes = []
for word in words:
    if palindromeChecker(word):
        palindromes.append(word)
print(palindromes)