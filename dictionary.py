import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data  = json.load(open("data.json"))
keys = data.keys()

def translate(w):
    w = w.lower()
    if w in data:
        for item in data[w]:
            print (item)
    elif w.title() in data:
        for item in data[w.title()]:
            print (item)
    elif w.upper() in data:
        for item in data[w.upper()]:
            print (item)

    elif get_close_matches(w , keys, cutoff = 0.7) != []:
        print("Did you mean %s instead ?" % get_close_matches(w , keys )[0] )
        cword = input("y/n ?")
        if cword.lower() == 'y':
            for item in data[get_close_matches(w , keys )[0]]:
                print(item)
        elif cword.lower() == 'n':
            print("Sorry no word found! ")
        else:
            print("Please enter y or n : ")
    else:
        print("PLease enter valid word")

word = input("Enter word: ")
print(translate(word))
