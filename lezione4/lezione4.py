"""
8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter.
Call the function, and make sure the message displays correctly.
"""
def messaggio():
    #Stampa un messaggio.
    message = " impariamo le funzioni in Python."
    print(message)

# Chiamata della funzione per visualizzare il messaggio
messaggio()

"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland". 
Call the function, making sure to include a book title as an argument in the function call.
"""


#def favorite_book (title):
    ##Stampa un messaggio con il titolo del libro preferito.
    #print(f"uno dei miei libri preferiti è {title}.")

##Inserire il titolo del libro
#title = input(" titolo del tuo libro preferito: ")


#favorite_book (title)


"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size,message):
    print(f"taglia: {size}, messaggio {message}")
make_shirt('Large','Mela')
make_shirt(size = 'Small', message= 'Pera')

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
"""

def make_shirt(size="large", message="I love Python"):
    print(f"\n taglia: {size} messaggio: '{message}'.")

make_shirt()

# maglietta media
make_shirt("medium")

#  maglietta piccola con un messaggio personalizzato
make_shirt("small", "I love Java")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
The function should print a simple sentence, such as Reykjavik is in Iceland. 
Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
"""


def describe_city(citta, paese="Italy"):
    print(f"{citta} is in {paese}.")

# funzione per tre città diverse
describe_city("Rome")
describe_city("Venice")
describe_city("New York", "USA")

"""
8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this:
"Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
"""

def city_country(citta, paese):
    print(f"{citta},{paese}.")

city_country("Rome", "Italy")
city_country("Venice", "Italy")
city_country("New York", "USA")

"""

8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the  dictionaries are storing the album information correctly. 
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.

"""

def make_album(artist_name, album_title, number_of_songs):
    """Costruisce un dizionario che descrive un album musicale."""
    album = {
        'artist': artist_name,
        'title': album_title,
        'number': number_of_songs
    }

    return album

# Creazione di tre dizionari 
album1 = make_album("Kanye West", "Yeezus", 13)
album2 = make_album("Tupac", "All Eyez on Me", 27)
album3 = make_album("AC/DC", "Back in Black",10)

# Stampare i valori 
print(album1)
print(album2)
print(album3)

"""
8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album’s artist and title.
Once you have that information, 
call make_album() with the user’s input and print the dictionary that’s created.
Be sure to include a quit value in the while loop.

"""


"""
def make_album(artist_name, album_title, number_of_songs):
    return {'artist': artist_name, 'title': album_title, 'number': number_of_songs}

while True:
    artista = input(" nome dell'artista dell'album (o 'quit' per uscire): ")
    if artista == 'quit':
        break
    
    titolo = input(" titolo dell'album (o 'quit' per uscire): ")
    if titolo == 'quit':
        break
    
    songs = int(input(" numero di canzoni nell'album: "))

    print(make_album(artista, titolo, songs))
    
"""





"""
8-9. Messages: Make a list containing a series of short text messages. 
Pass the list to a function called show_messages(), which prints each text message.
"""

def show_messages(messaggi):
    for messaggio in messaggi:
        print(messaggio)

# Lista di messaggi 
messaggi = [
    "Ciao",
    "Come va",
    "Hey "
]

# funzione show_messages() con la lista di messaggi
show_messages(messaggi)


"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
After calling the function, print both of your lists to make sure the messages were moved correctly.

"""

def show_messages(messaggi):
    for messaggio in messaggi:
        print(messaggio)

def send_messages(messaggi, messaggi_inviati):
    while messaggi:
        messaggio = messaggi.pop(0)
        print(f" messaggio inviato: {messaggio}")
        messaggi_inviati.append(messaggio)

# Lista di messaggi 
messaggi = [
    "Ciao",
    "Come va",
    "Hey"
]

# Lista vuota per i messaggi inviati
sent_messages = []

send_messages(messaggi, sent_messages)

# Stampa le liste per vedere se i messaggi sono stati spostati 
print("Messaggi:", messaggi)
print("Messaggi Inviati:", sent_messages)


"""
8-11. Archived Messages: Start with your work from Exercise 8-10. 
Call the function send_messages() with a copy of the list of messages. 
After calling the function, print both of your lists to show that the original list has retained its messages.

"""

def show_messages(messaggi):
    for messaggio in messaggi:
        print(messaggio)

def send_messages(messaggi, messaggi_inviati):
    while messaggi:
        messaggio = messaggi.pop(0)
        print(f" messaggio inviato: {messaggio}")
        messaggi_inviati.append(messaggio)

# Lista di messaggi 
messaggi = [
    "Ciao",
    "Come va",
    "Hey"
]

# Lista vuota per i messaggi inviati
sent_messages = []

send_messages(messaggi[:], sent_messages)

# Stampa le liste per vedere se i messaggi sono stati spostati 
print("Messaggi:", messaggi)
print("Messaggi Inviati:", sent_messages)

"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered. 
Call the function three times, using a different number of arguments each time.
"""

def ordina_sandwich(ingredienti):
    print("\nSandwich:")
    for ingrediente in ingredienti:
        print(ingrediente)

# Chiamate alla funzione con liste di ingredienti
ordina_sandwich(['Salame', 'Formaggio'])
ordina_sandwich(['Pollo', 'Lattuga', 'Pomodoro'])
ordina_sandwich(['Salsiccia', 'Maionese', 'Lattuga', 'Pomodoro'])


"""
8-13. User Profile:  Build a profile of yourself by calling build_profile(), 
using your first and last names and three other key-value pairs that describe you. 
All the values must be passed to the function as parameters. 
The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

"""

def build_profile(nome, cognome, age, hair_color, weight):
    profile = f"{nome} {cognome}, età {age}, capelli {hair_color}, peso {weight}"
    return profile

# profilo
profile = build_profile("Giulio", "Rossi", 60 ,"castani", 70)


print(profile)


"""
8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary 
that’s returned to make sure all the information was stored correctly. 
"""

def crea_auto(costruttore, modello, color, tow_package):
    info_auto = {'costruttore': costruttore, 'modello': modello, 'colore': color, 'tow_package': tow_package}
    return info_auto

auto = crea_auto('subaru', 'outback', color='blu', tow_package=True)
print(auto)

"""
8-15. Printing Models: Put the funzion for the example printing_models.py in a separate file called printing_functions.py. 
Write an import statement at the top of printing_models.py, and modify the file to use the imported funzion.
"""
"""
from lezione4 import city_country
print(city_country("Rome", "Italy"))
"""

"""
8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
Import the function into your main program file, and call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *

"""
import lezione4
from lezione4 import  build_profile 
from lezione4 import build_profile as x
import lezione4 as mn
from lezione4 import *

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
"""

