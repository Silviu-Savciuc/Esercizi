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


