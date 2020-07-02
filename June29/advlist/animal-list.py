#!/usr/bin/python3
'''
Author: itsOrD
Description: learning more about Python lists
'''

# OPTIONAL CHALLENGE
# three letter named animals
def main():
    '''
    Step 33:  make a list of animals with three letter names
    '''

    # define list
    animalList = ['fox', 'cat']
    # add to list
    animalList.append('dog')
    # add more to list with extension
    animalListExtension = ['bee', 'cow']
    animalList.extend(animalListExtension)
    # print list
    print(animalList, end="\n")
    
    # print list wihout 'list' symbols
    print("I went to the zoo and I saw....")
    for animal in animalList:
        print(animal, end=" ")
    print()

#   below doesn't work, but thought it should..?
#   print(" ".join(map(str, animalList)))
#   for animal in  animalList:
#       print(animal)
#   print inline

# make it executable (a 'script')
if __name__  == "__main__":
    main()

