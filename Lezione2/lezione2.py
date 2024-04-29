# Silviu Savciuc
# 18/04/2024

print("Hello World!")

# 2-3. Personal Message: Use a variable to represent a person’s name, 
# and print a message to that person. Your message should be simple,  
# such as, “Hello Eric, would you like to learn some Python today?”

# Versione semplice
name: str = "Mario"

print(f"Ciao {name}")

#Questa variabile contiene il messaggio
message: str = f"Ciao {name}, ti va di imparare u po di Python insime?"

print(message)

"""
 2-4. Name Cases: Use a variable to represent a person’s name,
 and then print that person’s name in lowercase, uppercase, and title case.
"""

#Questa variabile contiene il nome della persona 
name: str = "Marco"

#Questa variabile contiene sia il minuscolo che il maiuscolo 
name_lower: str = name.lower()

name_upper: str = name.upper()

print(f"{name}, {name_upper}, {name_lower}")

"""
2-5. Famous Quote: Find a quote from a famous person you admire. 
Print the quote and the name of its author. 
Your output should look something like the following,
 including the quotation marks: Albert Einstein once said,
 “A person who never made a mistake never tried anything new.” 
"""

name: str=" Caio Giulio Cesare"

print (f'{name} una volta ha detto: "Giacché se il diritto si deve violare, violarlo si deve per la conquista del regno; in tutto il resto osserva la pietà."' )

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, 
represent the famous person’s name using a variable called famous_person.
Then compose your message and represent it with a new variable called message. Print your message.
"""

famous_person: str="Caio Giulio Cesare"
message: str=(f'una volta ha detto: "Giacché se il diritto si deve violare, violarlo si deve per la conquista del regno; in tutto il resto osserva la pietà."')

print(f"{famous_person}{message}")

"""
2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.
"""
filename = "python_notes.txt"
filename_without_extension = filename.removesuffix('.txt')
print(filename_without_extension)

"""
3-1. Names: Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.
"""
names = ['andrea','marco','francesco','Phil']
for name in names:
    print(name)
    
"""
3-2. Greetings: Start with the list you used in Exercise 3-1,
but instead of just printing each person’s name, 
print a message to them. The text of each message should be the same, 
but each message should be personalized with the person’s name.
"""
for name in names:
    print(f'Ciao {name},come stai?')
    
"""
3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car,
and make a list that stores several examples. 
Use your list to print a series of statements about these items
such as “I would like to own a Honda motorcycle.”
"""


cars = ['ford', 'ferrari', 'bmw']

for car in cars:
    print(f"Mi piacerebbe avere una {car}.")
    

"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner.
"""
lista = ['Emily','Luca','Sara']

for nome in lista:
    print(f'Mi piacerebbe invitarti a cena {nome}.')
    
"""
3-5. Changing Guest List: You just heard that one of your guests can’t make to the dinner, so you need to send out a new set of invitations. 
You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.
"""
print(f'purtroppo {lista[0]} non puo venire')

lista[0]="Maria"

for nome in lista:
    print(f'Mi piacerebbe invitarti a cena {nome}.')
    
"""
3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

print("Ottime notizie! Ho trovato un tavolo piu grande.")


lista.insert(0, 'Galileo') 
lista.insert(len(lista)//2, 'Nicola')  
lista.append('Stefano')  


for nome in lista:
    print(f"Caro {nome}, mi piacerebbe invitarti a cena.")
    
"""
3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6.
Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list.
Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list.
Print your list to make sure you actually have an empty list at the end of your program.
"""


print("Purtroppo il nuovo tavolo non arrivera in tempo, posso solo invitare 2 pesrone")


while len(lista) > 2:
    removed_guest = lista.pop()
    print(f"Mi dispiace, {removed_guest}, non posso invitarti a cena.")

for nome in lista:
    print(f"Caro {nome}, mi piacerebbe invitarti a cena.")

del lista[:]
print("Ora la lista è vuota:", lista)

"""
3-9. Dinner Guests: Working with one of the programs from Exercises 3,
use len() to print a message indicating the number of people you’re inviting to dinner.
"""
lista = ['Emily','Luca','Sara']

print(f"Ho invitato {len(lista)} persone a cena.")

"""
3-10. Every Function: Think of things you could store in a list. 
For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

#lista di città italiane
città_italiane = ['Roma', 'Milano', 'Napoli', 'Torino', 'Palermo']

#  append() per aggiungere una nuova città alla lista
città_italiane.append('Firenze')
print("aggiunto di Firenze:", città_italiane)

#  insert() per aggiungere una nuova città a un indice specifico
città_italiane.insert(2, 'Bologna')
print("inserimento di Bologna al secondo indice:", città_italiane)

#  remove() per rimuovere una città specifica dalla lista
città_italiane.remove('Napoli')
print( città_italiane)

#  pop() per rimuovere e restituire l'ultima città dalla lista
città_rimossa = città_italiane.pop()
print("Città rimossa:", città_rimossa)
print(città_italiane)

#  sort() per ordinare le città in ordine alfabetico
città_italiane.sort()
print( città_italiane)

#  reverse() per invertire l'ordine delle città
città_italiane.reverse()
print(città_italiane)

#  len() per trovare il numero di città nella lista
num_città = len(città_italiane)
print("Numero di città nella lista:", num_città)

# clear() per rimuovere tutti gli elementi dalla lista
città_italiane.clear()
print("Dopo aver cancellato la lista:", città_italiane)

"""
6-1. Person: Use a dictionary to store information about a person you know. 
Store their first name, last name, age, and the city in which they live. 
You should have keys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.
"""

person = {'nome': 'Giuseppe','cognome': 'Rossi','eta': 30,'citta': 'Milano'}


print("nome:", person['nome'])
print("cognome:", person['cognome'])
print("eta:", person['eta'])
print("Citta:", person['citta'])

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. 
Think of a favorite number for each person, and store each as a value in your dictionary.
Print each person’s name and their favorite number. 
For even more fun, poll a few friends and get some actual data for your program.
"""
#  dizionario per memorizzare i numeri preferiti delle persone
numeri = {'Mario': 7,'Luca': 3,'Giulia': 12,'Anna': 8,'Stefano': 5}

# Stampa il nome di ogni persona e il numero preferito
for nome, numero in numeri.items():
    print(f"{nome} ha come numero preferito {numero}.")
    
"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line.
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""

#  glossario con parole e definizioni
glossario = {
    'Variabile': 'Un contenitore per immagazzinare dati in un programma.',
    'Funzione': 'Un blocco di codice riutilizzabile che esegue una specifica azione.',
    'Condizione': 'Una struttura di controllo che permette di eseguire azioni diverse in base a una condizione.',
    'Lista': 'Una collezione ordinata di elementi, modificabile e indicizzata.',
    'Dizionario': 'Una collezione di coppie chiave-valore, non ordinata e modificabile.'
}

# Stampa ogni parola e la sua definizione 
for parola, definizione in glossario.items():
    print(f"{parola}:\n{definizione}\n")
    
"""
6-7. People: Start with the program you wrote for Exercise 6-1. 
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

persona1 = {'nome': 'Giuseppe','cognome': 'Rossi','età': 30,'città': 'Milano'}


persona2 = {'nome': 'Maria','cognome': 'Bianchi','età': 25,'città': 'Roma'}

persona3 = {'nome': 'Luca','cognome': 'Verdi','età': 35,'città': 'Napoli'}

# Lista che contiene tutti i dizionari delle persone
persone = [persona1, persona2, persona3]

# Loop attraverso la lista di persone e stampa tutte le informazioni su ciascuna persona
for persona in persone:
    print("Informazioni:")
    for chiave, valore in persona.items():
        print(f"{chiave}: {valore}")
        
"""
6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 
"""


animale1 = {'tipo': 'cane', 'proprietario': 'Mario'}
animale2 = {'tipo': 'gatto', 'proprietario': 'Luca'}
animale3 = {'tipo': 'pappagallo', 'proprietario': 'Giulia'}
animale4 = {'tipo': 'coniglio', 'proprietario': 'Anna'}

# Lista che contiene tutti i dizionari degli animali 
animali = [animale1, animale2, animale3, animale4]

# Loop attraverso la lista di animali domestici e stampa tutte le informazioni
for animale in animali:
    print("Informazioni sull'animale domestico:")
    for chiave, valore in animale.items():
        print(f"{chiave}: {valore}")
        
"""
6-9. Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
Loop through the dictionary, and print each person’s name and their favorite places.
"""


favorite_places = {
    'Mario': ['Roma', 'Firenze', 'Venezia'],
    'Anna': ['Barcellona', 'New York'],
    'Giulia': ['Parigi', 'Londra', 'Praga']
}

# stampa i nomi delle persone e i loro luoghi preferiti
for persona, luoghi in favorite_places.items():
    print(f"{persona} ama :")
    for luogo in luoghi:
        print(f"- {luogo}")
        
"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number. 
Then print each person’s name along with their favorite numbers.
"""


preferiti_numeri = {'Mario': [7, 13, 22],'Luca': [3, 11],'Giulia': [12, 5, 8], 'Anna': [6, 9]}

# stampa i nomi delle persone e i loro numeri preferiti
for persona, numeri in preferiti_numeri.items():
    print(f"{persona} ha come numeri preferiti:")
    for numero in numeri:
        print(f"- {numero}")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and include the country that the city is in, its approximate population,
and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. 
Print the name of each city and all of the information you have stored about it.
"""

# Creare un dizionario chiamato città
città = {
    'Tokyo': {
        'paese': 'Giappone',
        'popolazione': '37 milioni',
        'curiosità': "Tokyo è l'area metropolitana più grande del mondo."
    },
    'Roma': {
        'paese': 'Italia',
        'popolazione': '2.8 milioni',
        'curiosità': "Roma è una delle città più antiche del mondo, con una storia che risale a quasi 3.000 anni fa."
    },
    'Milano': {
        'paese': 'Italia',
        'popolazione': '1.4 milioni',
        'curiosità': "Milano è conosciuta per la sua grande scena culturale e artistica"
    }
}

# Stampare il nome di ogni città e le sue informazioni
for città, info in città.items():
    print(f"\nCittà: {città}")
    print(f"Paese: {info['paese']}")
    print(f"Popolazione: {info['popolazione']}")
    print(f"Curiosità: {info['curiosità']}")
    
    
"""
6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways. 
Use one of the example programs from this chapter, 
and extend it by adding new keys and values, changing the context of the program, or improving the formatting of the output.

"""    
# Dizionario delle città con informazioni aggiuntive
città = {
    'Tokyo': {
        'paese': 'Giappone',
        'popolazione': '37 milioni',
        'fatto': "Tokyo è l'area metropolitana più grande del mondo.",
        'monumento_famoso': 'Torre di Tokyo',
        'lingua': 'Giapponese',
        'valuta': 'Yen'
    },
    'Roma': {
        'paese': 'Italia',
        'popolazione': '2.8 milioni',
        'fatto': "Roma è una delle città più antiche del mondo, con una storia che risale a quasi 3.000 anni.",
        'monumento_famoso': 'Colosseo',
        'lingua': 'Italiano',
        'valuta': 'Euro'
    },
    'Milano': {
        'paese': 'Italia',
        'popolazione': '1.4 milioni',
        'fatto': "Milano è nota per la sua fiorente scena culturale e artistica.",
        'monumento_famoso': 'Duomo di Milano',
        'lingua': 'Italiano',
        'valuta': 'Euro'
    },
    'New York': {
        'paese': 'Stati Uniti',
        'popolazione': '8.4 milioni',
        'fatto': "New York City è spesso indicata come la capitale culturale, finanziaria e mediatica del mondo.",
        'monumento_famoso': 'Statua della Libertà',
        'lingua': 'Inglese',
        'valuta': 'Dollaro'
    }
}

# Stampare le informazioni per ogni città
for città, info in città.items():
    print(f"\n{città.upper()}")
    print("           ")
    print(f"Paese: {info['paese']}")
    print(f"Popolazione: {info['popolazione']}")
    print(f"Fatto: {info['fatto']}")
    print(f"Monumento Famoso: {info['monumento_famoso']}")
    print(f"Lingua: {info['lingua']}")
    print(f"Valuta: {info['valuta']}")


