numero = 0 

while numero < 10:
    if numero == 0:
        print("O numero", numero , " é zero" )
        print("-------------------------------")
    elif numero  % 2 == 0:
        print("o numero", numero , "é par")
        print("-------------------------------")
    else: 
        print("o numero ", numero , "é impar")
        print("-------------------------------")
    numero += 1