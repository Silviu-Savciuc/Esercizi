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
    