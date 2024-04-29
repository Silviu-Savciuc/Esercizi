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
for numero in range(1000001):
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