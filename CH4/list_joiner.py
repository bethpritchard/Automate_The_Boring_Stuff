spam = ['apples', 'bananas', 'tofu', 'cats']

def list_joiner(lst):
    """Take a list and print it as an Oxford comma having sentence."""
    sentence = lst[0]
    for i in range(1,len(lst)-1):
        sentence = sentence + ', ' + lst[i]
    sentence = sentence + ', and ' + lst[-1]
    return sentence

print(list_joiner(spam))
