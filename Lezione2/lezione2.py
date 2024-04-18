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