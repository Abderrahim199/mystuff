import pyperclip



# in this program , we will capitalize the first litter in every word!
def capitalize(ourString):
    return ' '.join([element[0].upper() + element[1:] for element in ourString.split()])

# we will test the code.


tests = ['abderrahim is a great man!', 'idk what i\'m doing with my life?', 'good job you are doing here', 1335, True, False]

for element in tests:
    print(capitalize(element))

    copies = pyperclip.copy(capitalize(element))
    print(copies)




