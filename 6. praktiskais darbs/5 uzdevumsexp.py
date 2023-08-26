import random
def NegativeNumber():
    array = random.sample(range(-10,10+1), 10)
    print(f'{array}')
    # set defaults
    GreatestNegative = array[0]
    # finding greatest negative
    for i in range(1,len(array)):
        CompareTo = array[i]
        # assing new GreatestNegative if:
        # new one is negative and greater than current 
        # or
        # current is non negative and new one is
        if(GreatestNegative < CompareTo and CompareTo < 0 or GreatestNegative >= 0 and CompareTo < 0):
            GreatestNegative = CompareTo
    # display result
    # check if there are no negatives in the array
    if(GreatestNegative >= 0):
        print(f'Nav negativus skaitļus!')
        return
    print(f'Lielakais negatīvais masīva skaitļis ir {GreatestNegative} un vina index ir [{array.index(GreatestNegative)}].')
NegativeNumber()
