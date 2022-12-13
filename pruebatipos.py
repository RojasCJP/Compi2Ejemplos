def primos(maximo):
    for element in range(maximo):
        trigger = 0
        if element == 0: continue
        for i in range(element):
            if i == 0 : continue
            resultado = element%i 
            if(resultado == 0):
                trigger += 1
        if trigger < 2:
            print(element)
        

primos(100)
