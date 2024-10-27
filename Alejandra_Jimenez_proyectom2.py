def solicitar_una_palabra():  #Se indica la función incial del programa

    intentos = 0 
    palabra_valida = False

    while intentos < 3 and not palabra_valida: #Se establece que solo se tendran 3 intentos
        palabra = input ("Acontinuación ingresa una palabra que debe tener entre 4 y 8 letras: ") #Solicita ingresar una palabra entre 4 a 8 letras
        longitud = len(palabra) #Se establece se validara la longitud de la palabra

        if 4 <= longitud <= 8: # Se establecen los parametros en caso de que cumpla con lo solicitado
            print(f"La palabra {palabra} es correcta, contiene {longitud} letras.") # Pide se imprima mensaje con la palabra correcta y las letras que contiene
            palabra_valida = True 
        elif longitud < 4: #Se Indica en caso de ser menor a 4 arroje el mesaje de que faltan letras
            print(f"Te hacen falta letras, la palabra {palabra} solo tiene {longitud} letras.")
        else: #Se indica en caso de que la palabra fuera mayor a lo solictado se imprima la palabra y cantidad de letras 
            print(f"Te sobran letras. Tu palabra {palabra} tiene {longitud} letras.")

        intentos += 1 #Se establece el contador de intentos se aumente

        if intentos == 3 and not palabra_valida: #Indica en caso de cometer 3 errores, se cerrara el progrema
            print ("Has cometido 3 errores el programa se cerrara.")

solicitar_una_palabra() # Se llama a la función incial
        

