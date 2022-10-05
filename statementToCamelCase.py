# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).

#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text:str):
    newText = text.replace("_", " ").replace("-"," ")
    words = newText.split(" ")
    newWords = []
    newWords.append(words[0])
    for i in range(1,len(words)):
        newWords.append(words[i].title())
    newStr = ''.join(newWords)
    return newStr