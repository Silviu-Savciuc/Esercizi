"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, 
contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
"""

def remove_duplicates(lista) -> list:
    unici=[]
    visti=set()
    for oggetto in lista:
      if oggetto not in visti:
        unici.append(oggetto)
        visti.add(oggetto)
    return unici
    
    
"""

Scrivi una funzione che accetti tre parametri: username,
password e status di attivazione dell'account (attivo/non attivo).
L'accesso è consentito solo se il nome utente è "admin", 
la password corrisponde a "12345" e l'account è attivo.
La funzione ritorna "Accesso consentito" oppure "Accesso negato".

For example:

print(check_access("admin", "12345", True))

Accesso consentito

print(check_access("admin", "54321", True))

Accesso negato

"""

def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    
    
"""

Scrivi una funzione che somma tutti i numeri interi di una lista
che sono maggiori di un dato valore intero definito threshold.

For example:

print(sum_above_threshold([15, 5, 25], 20))


"""

def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    totale = 0 
    for numero in numbers:
        if numero > threshold:
                    totale += numero
    return totale


"""

Scrivi una funzione che ritorna il valore massimo,
minimo e la media di una lista di numeri interi.

For example:

print(list_statistics([1, 2, 3, 4, 5]))
 
result:
(5, 1, 3.0)

"""    
def list_statistics(numbers: list[int]):
    
    massimo=max(numbers)
    minimo= min(numbers)
    media = sum(numbers) / len(numbers)
    
    return massimo, minimo, media 

"""
Scrivi una funzione che unisce due dizionari. 
Se una chiave è presente in entrambi, somma i loro valori.

For example:

print(merge_dictionaries({'x': 5}, {'x': -5}))

risultato:
{'x': 0} 
    
"""
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    dict_unito= {}
    for key in dict1.keys():
        if key in dict2:
            dict_unito[key]= dict1[key] + dict2[key]
        else:
            dict_unito[key]= dict1[key]
            
    for key in dict2.keys():
        if key not in dict1:
            dict_unito[key]= dict2[key]
            
    return dict_unito

"""

Scrivi una funzione che verifica
se in una stringa le parentesi '(' e ')' sono bilanciate,
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.

For example:

print(check_parentheses("()()"))

True

print(check_parentheses("(()))("))

False

"""
def check_parentheses(expression: str) -> bool:
    count = 0
    for i in expression:
        if i =="(":
            count += 1
        elif i ==")":
            count -= 1
        if count < 0:
            return False
            
    return count == 0

"""
Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere,
ritorni un nuovo insieme senza i numeri specificati nella lista.

For example:

print(remove_elements({5, 6, 7}, [7, 8, 9]))

risultato:
{5, 6}
"""

def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    nuovo_set = original_set.copy()
    for i in elements_to_remove:
        nuovo_set.discard(i)
    return nuovo_set



"""
Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit
e viceversa a seconda del parametro to_fahrenheit.
Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.
"""
def convert_temperature(temp, to_fahrenheit=True) -> float:
    if to_fahrenheit == True:
        return (temp * 9/5) + 32
    else:
        return (temp - 32) * 5/9


"""

Scrivi una funzione che conta e ritorna quante volte
un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato
sia a destra che a sinistra da elementi uguali.
"""
def count_isolated(numeri) -> int:
    isolati = 0
    
    for i in range(len(numeri)):
        if i == 0 and numeri[i] != numeri[i+1]:
            isolati += 1
        elif i == len(numeri) - 1 and numeri[i] != numeri[i-1]:
            isolati += 1
        elif numeri[i] != numeri[i-1] and numeri[i] != numeri[i+1]:
            isolati += 1
    
    return isolati


"""
3. Personal Info:

Write a build_profile() function that accepts
the name , surname,  occupation, location, and age  of a person.
Make occupation, location, and age optional parameters.
Use this function to create profiles for different people,
demonstrating how it handles these optional parameters.

Example: build_profile("John", "Doe", occupation="Developer", location="USA", age=30)


"""

def build_profile(nome, cognome, professione=None, ubicazione=None, eta=None):
    profilo = {
        'nome': nome,
        'cognome': cognome
    }
    if professione is not None:
        profilo['professione'] = professione
    if ubicazione is not None:
        profilo['ubicazione'] = ubicazione
    if eta is not None:
        profilo['età'] = eta
    return profilo

# Esempi:
profilo1 = build_profile("Mario", "Rossi", ubicazione="Italia", eta=35)
print(profilo1)

profilo2 = build_profile("Anna", "Bianchi", professione="Designer")
print(profilo2)

profilo3 = build_profile("Luca", "Verdi", ubicazione="Francia")
print(profilo3)

