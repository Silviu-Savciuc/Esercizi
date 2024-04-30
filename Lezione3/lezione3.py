"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. 
Store these pizza names in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza,
instead of printing just the name of the pizza. For each pizza, 
you should have one line of output containing a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, 
that states how much you like pizza.
The output should consist of three or more lines about the kinds of pizza you like
and then an additional sentence, such as I really love pizza!
"""

pizzas=["Diavola","Marinara","4 Formaggi"]

#for pizza in pizzas:
#    print(pizza)
    
for pizza in pizzas:
    print(f'Mi piace la {pizza}')
    
print('I love Pizza!')


"""
4-2. Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, 
and then use a for loop to print out the name of each animal.
• Modify your program to print a statement about each animal, 
such as A dog would make a great pet.
• Add a line at the end of your program, stating what these animals have in common.
You could print a sentence, such as Any of these animals would make a great pet!
"""

animals=['Tigre','Leone','Orso']
#Lista di animali
for animal in animals:
    print(animal)
    
#lista di animali con frasi
for animal in animals:
    if animal=='Tigre':
        print(f'La {animals[0]} è un animale maestoso')
    elif animal=='Leone':
        print(f'Il {animals[1]} è abbstanza pigro')
    elif animal=='Orso':
        print(f"L'{animals[2]} è molto veloce in brevi distanze")
        
print(f'{animals} sono tutti animali molto pericolosi')

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
"""
# Stampare i numeri da 1 a 20 incluso
print("Numeri da 1 a 20:")
for numero in range(1, 21):
    print(numero)

"""
4-4. One Million: Make a list of the numbers from one to one million,
and then use a for loop to print the numbers. (If the output is taking too long, 
stop it by pressing CTRL-C or by closing the output window.)
"""
numeri: list=[]
for numero in range(1,1000001):
    numeri.append(numero)
#print(numeri)

"""
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max()
to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
"""

minimo= min(numeri)
massimo= max(numeri)
somma= sum(numeri)

print('il minimo della lista è', minimo)
print('il massimo della lista è', massimo)
print('la somma della lista è', somma)

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a list 
of the odd numbers from 1 to 20.
Use a for loop to print each number.
"""
#lista numeri dispari da uno a 20
numeri_dispari= list(range(1,21,2))

#print di ogni numero usando il for
for numero in numeri_dispari:
    print(numero)
    
"""
4-7. Threes: Make a list of the multiples of 3, from 3 to 30.
Use a for loop to print the numbers in your list
"""

#lista di multipi di 3
tabellina=list(range(3,31,3))

#print di ogni numero usand il for
for numero in tabellina:
    print(numero)
    
"""
4-8. Cubes: A number raised to the third power is called a cube. 
For example, the cube of 2 is written as 2**3 in Python. 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), 
and use a for loop to print out the value of each cube. 
"""
#lista dei primi 10 cubi
primi_10_cubi=[]
for numeri in range(1,11):
    cubo = numeri**3
    primi_10_cubi.append(cubo)

# Stampa dei primi 10 cubi
print("I primi 10 cubi sono:")
for cubo in primi_10_cubi:
    print(cubo)    
    
"""
4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
"""
# list comprehension per generare una lista dei primi 10 cubi
primi_10_cubi = [numero ** 3 for numero in range(1, 11)]

# Print dei primi 10 cubi
print("I primi 10 cubi sono:", primi_10_cubi)

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

"""
# list comprehension per generare una lista dei primi 10 cubi
primi_10_cubi = [numero ** 3 for numero in range(1, 11)]

# stampa dei primi 3 elementi della lista 
print("i primi 3 elementi:", primi_10_cubi[:3])

# stampa dei primi 3 elementi nel mezzo 
mezzo = len(primi_10_cubi) // 2
print("i primi 3 elementi:", primi_10_cubi[mezzo:mezzo+3])

# stampa degli ultimi 3 elementi della lista 
print("i primi 3 elementi:", primi_10_cubi[-3:])

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. 
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas are:, 
and then use a for loop to print the first list. Print the message 
My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.

"""
#lista friend basata su pizz es.4-1
friend_pizzas = pizzas[:]

#pizza aggiunta nella lista originale
pizzas.append("Margherita")

#pizza aggiunta nella friend_pizzas
friend_pizzas.append("Boscaiola")

#lista le mie pizze preferite 
print("le mie pizze preferite sono:")
for pizza in pizzas:
    print(pizza)
    
#lista friend_pizzas
print("le sue pizze preferite sono:")
for pizza in friend_pizzas:
    print(pizza)


"""    
4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, 
to save space. 
Choose a version of foods.py, 
and write two for loops to print each list of foods.
"""

cibi={
    'italiano':['pizza','pasta','gnocchi'],
    'Giapponese':['sushi', 'ramen', 'tempura'],
    'Moldavo':['mămăligă', 'sarmale', 'plăcinte']
}

#stampa della lista cibi

# Stampa della lista di cibi
print("\nCibi italiani:")
for food in cibi['italiano']:
    print(food)

print("\nCibi Giapponesi:")
for food in cibi['Giapponese']:
    print(food)

print("\nCibi Moldavi :")
for food in cibi['Moldavo']:
    print(food)

"""
4-14. PEP 8: Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/. 
You won’t use much of it now, but it might be interesting to skim through it.
"""

"""
4-15. Code Review: 
Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.
"""

#4-2
# Definizione di una lista di animali
animali = ['Tigre', 'Leone', 'Orso']

# Stampa dei nomi degli animali
print("Nomi degli animali:")
for animale in animali:
    print(animale)

# Stampa di una frase su ogni animale
print("\nCaratteristiche degli animali:")
for animale in animali:
    if animale == 'Tigre':
        print(f"La {animale} è un animale maestoso e potente.")
    elif animale == 'Leone':
        print(f"Il {animale} è noto per la sua forza e maestosità.")
    elif animale == 'Orso':
        print(f"L'{animale} è un animale potente e imponente.")

# Stampa della caratteristica comune degli animali
print("\nTutti questi animali hanno in comune la loro imponenza e potenza.")

#4-9
# list comprehension per generare una lista dei primi 10 cubi
primi_10_cubi = [numero ** 3 for numero in range(1, 11)]

# Stampa dei primi 10 cubi
print("I primi 10 cubi sono:")
for cubo in primi_10_cubi:
    print(cubo)
    
    
#4-4
# Creazione di una lista di 1 milione
numeri = []
for numero in range(1,1000001):
    numeri.append(numero)
# Stampa dei numeri

#  for numero in numeri:
#     print(numero)


"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
"""
# Test 1: 5 maggiore di 2? (True)
print("\n 5 maggiore di 2? Mi aspetto True.")
print(5 > 2)

# Test 2: È 8 minore o uguale a 10? (True)
print("\nÈ 8 minore o uguale a 10? Mi aspetto True.")
print(8 <= 10)

# Test 3: 'Luca' uguale a 'Luca'? (True)
print("\nÈ 'Luca' uguale a 'Luca'? Mi aspetto True.")
print('Luca' == 'Luca')

# Test 4: È 'giallo' diverso da 'verde'? (True)
print("\nÈ 'giallo' diverso da 'verde'? Mi aspetto True.")
print('giallo' != 'verde')

# Test 5: 8 maggiore di 2? (True)
print("\n 8 è maggiore di 2? Mi aspetto True.")
print(8 > 2)

# Test 6: È 7 uguale a 8? (False)
print("\n 7 uguale a 8? Mi aspetto False.")
print(7 == 8)

# Test 7: 15 minore di 10? (False)
print("\n 15 minore di 10? Mi aspetto False.")
print(15 < 10)

# Test 8:È cane diverso da cane ? (False)
print("\n 'cane' è diverso da 'cane'? Mi aspetto False.")
print('cane' != 'cane')

# Test 9: 15 è maggiore di 20? (False)
print("\n 15 è maggiore di 20? Mi aspetto False.")
print(15 > 20)

# Test 10: È 20 maggiore o uguale a 25? (False)
print("\nÈ 20 maggiore o uguale a 25? Mi aspetto False.")
print(20 >= 25)


"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

# Uguaglianza e disuguaglianza con stringhe
print("Uguaglianza e disuguaglianza con stringhe:")
print('mela' == 'mela') 
print('mela' == 'pesca') 

# Uso il metodo lower()
print("\n metodo lower():")
print('MELA'.lower() == 'ciao') 
print('PERA'.lower() == 'pera') 

# Test numerici 
print("\nTest numerici:")
print("12 == 12:", 12 == 12) 
print("8 != 5:", 8 != 5) 
print("10 > 5:", 10 > 5)
print("1 < 2:", 1 < 2)

print("10 == 12:", 10 == 12) 
print("5 != 5:", 5 != 5) 
print("1 > 5:", 1 > 5)
print("4 < 2:", 4 < 2)

# Parole chiave 'and' e 'or'
print("\nTest usando le parole chiave 'and' e 'or':")
print("5==5 and 3<5:",5 == 5 and 3 < 5)
print("6==5 and 3<5:",6 == 5 and 3 < 5)
print("5==5 and 7<5:",5 == 5 and 7 < 5)
print("6==5 and 7<5:",6 == 5 and 7 < 5)

print("5 < 3 or 10 < 15:",5 < 3 or 10 < 15)  
print("5 < 3 or 10 > 15:",5 < 3 or 10 > 15)  

# Se un elemento è presente in una lista
frutta = ['mela', 'pesca', 'melone']
print("\n se un elemento è presente in una lista:")
print("'pesca' in frutta:", 'pesca' in frutta) 
print("'cocco' in frutta:", 'cocco' in frutta) 

# Se un elemento non è presente in una lista
print("\n elemento non presente in una lista:")
print("'melograno' not in frutta:", 'melograno' not in frutta)  # True
print("'pesca' not in frutta:", 'pesca' not in frutta)  # False

"""
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, 
print a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that fails. 
(The version that fails will have no output.)
"""

# supera l'istruzione if
alien_color = 'green'

if alien_color == 'green':
    print(" hai guadagnato 5 punti.")

# non supera l'istruzione if
alien_color = 'yellow'

if alien_color == 'green':
    print(" hai guadagnato 5 punti.")

    
"""
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned 10 points.
• Write one version of this program that runs the if block and another that runs the else block.
"""

# blocco if
alien_color = 'green'

if alien_color == 'green':
    print("hai guadagnato 5 punti .")
else:
    print(" hai guadagnato 10 punt.")
    
# blocco else
alien_color = 'red'

if alien_color == 'green':
    print("hai guadagnato 5 punti.")
else:
    print("hai guadagnato 10 punti.")
    
"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed for the appropriate color alien.
"""
# Definizione del colore dell'alieno
alien_color = input("Inserisci il colore dell'alieno (green/yellow/red): ")

# Controllo del colore dell'alieno e assegnazione dei punti
if alien_color == 'green':
    print("hai guadagnato 5 punti.")
elif alien_color == 'yellow':
    print("hai guadagnato 10 punti.")
elif alien_color == 'red':
    print("hai guadagnato 15 punti.")
else:
    print("Colore dell'alieno non riconosciuto.")

"""

5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is a baby.
• If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that the person is an adult.
• If the person is age 65 or older, print a message that the person is an elder.
"""


età = int(input("Inserisci l'età della persona: "))

# Determina lo stadio della vita in base all'età inserita
if età < 2:
    print("Neonato.")
elif età < 4:
    print("Bambino.")
elif età < 13:
    print("Ragazzo.")
elif età < 20:
    print("Adolescente.")
elif età < 65:
    print("Adulto.")
else:
    print("Anziano.")
    

