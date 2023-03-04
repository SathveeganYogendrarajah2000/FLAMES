name1 = (input("HE: ")).lower()
name2 = (input("SHE: ")).lower()
while name1 != '':
    n1 = list(name1)
    n2 = list(name2)

#Remove same letters in each given names.
    for i in name1:
        if i in n2:
            n1.remove(i)
            n2.remove(i)

    count = len(n2) + len(n1)       #Find how many remainig words in two names.
    word = list("FLAMES")

#Find which letter is remaing after doing the flames thing.
    while len(word) != 1:
        count = len(n2) + len(n1)
        while count > len(word):count -= len(word)
        word.remove(word[count-1])
        word = word[(count-1):]+word[:(count-1)]
        
#Final results for remaining letter in 'FLAMES'.
    if word == ['F']:result = 'Friends'
    elif word == ['L']:result = 'Love'
    elif word == ['A']:result = 'Affection'
    elif word == ['M']:result = 'Marriage'
    elif word == ['E']:result = 'Enemy'
    elif word == ['S']:result = 'Sister'

#Print result.
    print("❤",result.upper(),"❤")
    print()
    name1 = (input("HE: ")).lower()
    name2 = (input("SHE: ")).lower()

##ACA Link
    #https://drive.google.com/folderview?id=1BtZwPcRAKXiLui5aAGV1R0LPXOrtTYr3
