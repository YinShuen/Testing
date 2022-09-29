import random

name = input('What is your name?')
print('Best of luck,', name)

nonmetal = ['helium', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 'phosphorus', 'sulphur', 'chlorine', 'argon', 'selenium', 'bromine', 'krypton', 'iodine', 'xenon', 'astatine', 'radon', 'ununseptium', 'ununoctium']

semimetal = ['boron', 'silicon', 'germanium', 'arsenic', 'antimony', 'tellurium', 'polonium']

metal = ['lithium', 'beryllium', 'sodium', 'magnesium', 'potassium', 'calcium', 'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'zinc', 'aluminium', 'gallium', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadnium', 'indium', 'tin', 'caesium', 'barium', 'lanthanium', 'hafnium',  'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury', 'thallium', 'lead', 'bismuth', 'francium', 'radium', 'actinium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadium', 'roentgenium', 'ununbium', 'ununtrium', 'flerovium', 'ununpentium', 'livermorium']

lathanoids = ['cerium','praeseodymium','neodymium','promethium','samarium','europium','gadolinium','terbium','dysprosium','holmium','erbium','thulium','ytterbium','lutetium']

actinoids =['thorium','protactinum','uranium','neptunium','plutonium','americum','curium','berkelium','californium','einsteinium','fermium','mendelevium','nobelium','lawrencium']

lists = nonmetal + semimetal + metal + lathanoids + actinoids


word1 = random.choice(lists)
print('Please guess the characters :')

if word1 in nonmetal:
    print('Your word is a non-metal')
elif word1 in semimetal:
    print('Your word is a semi-metal')
elif word1 in metal:
    print('Your word is a metal')
elif word1 in lathanoids:
    print('Your word is one of the lathanoids')
elif word1 in actinoids:
    print('Your word is one of the lathanoids')

guesses1 = ''

turns1 = 20

while turns1 > 0:
    failed1 = 0
    for char in word1:
        if char in guesses1:
            print(char)
        else:
            print('_')
            failed1 += 1
    if failed1 == 0:
        print('Congratulations! You Win!')
        print('The correct word is: ', word1)
        break
    guess1 = input('Guess another character:')
    guesses1 += guess1

    if guess1 not in word1:
        turns1 -= 1
        print('Wrong Guess')
        print ('You have ', turns1, 'more guesses')
    if turns1 == 0:
        print ('You Lose')

x = str(input('Would you like to play again? Type Y for yes and N for no'))
if x == "Y":
    return name
elif x == "N":
    print('Thank you for playing')
else:
    print('Sorry, your answer is invalid')
