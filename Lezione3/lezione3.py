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




