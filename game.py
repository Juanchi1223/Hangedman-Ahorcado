#   ------  Ahorcado  ------
import random

#        -- Funciones --
def mostrar(m, e):    # Muestra el dibujo y la cantidad de errores    
    for fila in m:
        for elemento in fila:
            print(elemento, end="")
        print()
    print()
    if e != 0:
        if e < 7:
          print(f"Te quedan {7-e} intento(s)")
        else:
          print("Perdiste: No te quedan mas intentos")
    print()

def agregar_errores(n, a):  #Agregar los errores a la figura
    if a >= 1: #Cabeza
        n[2][5] = '0' 
        if a >= 2: #Cuerpo Superior
          n[3][5] = '|'
          if a >= 3: #Brazo Derecho
            n[3][4] = '/'
            if a >= 4: #Brazo Izquierdo
              n[3][6] = r'\ '
              if a >= 5: #Cuerpo Inferior
                n[4][5] = '|'
                if a >= 6: #Pierna Derecha
                    n[5][4] = '/'
                    if a >= 7: #Pierna Izquierda
                        n[5][6] = r'\ '

def eliminar_l_rep(l):      # Elimina repeticiones de las letras a encotrar
    l_corr = list(set(l))
    while l_corr.count(' ') > 0:
        l_corr.remove(' ') 
    return l_corr

def mostrar_pista(pista):   # Muestra en consola la pista
    pista_lista = pista.split(" ")

    print("Pista: ", end="")
    for i in range(len(pista_lista)):
        if (i % 10) == 0 and i != 1:
          print()
        if i == 0:
          print(pista_lista[i].capitalize(), end=" ")
        else:
          print(pista_lista[i], end=" ")
    print()


def mostrar_letras_faltante(letras, l_encontradas): # Muesta en consola las letras restantes
    for l in letras:
        if l in l_encontradas:
            print('%2s' %l, end='')
        elif l == ' ':
            print('%2s' %' ', end='')
        else:
            print('%2s' %'_', end='')
    print()

def ver_entradas(a):        # Hace que el ingreso sea valido 
  if len(a) == 1:
    if a.isalpha():
        a = a.lower()
    else:
      print("ERROR: Ingrese un valor valido")
      a = -1 
  elif len(a) == 0:
    print("ERROR: Ingrese un valor valido")
    a = -1
  else: 
    a = a.lower()
  return a 
          
def si_o_no():            # Devuelve booelano de la pregunta Si o No          
  a = input("Si o No?: ")
  a = a.lower()
  if a == "si":
    x = True
  elif a == "no":
    x = False
  else:
    x = si_o_no()
  return x

#       Programa Principal
try:
    entrada = open("PalabrasProgramacion.txt", "rt") #Archivo de Palabras
    print('Comienza el juego :)')
    
    numero_palabras_tot = 0
    puntos_totales = 0
    
    for l in entrada:
        numero_palabras_tot += 1
    entrada.seek(0)
    
    palabra_usadas = []
    us = True
    while us:
        palabra_no_encontrada = True
        errores_us = 0  
        figura = [  ["╔","═","═","═", "═","╦","",""],
                    ["╬"," "," "," "," ","╩","",""],
                    ["╬"," "," "," "," ","","",""],
                    ["╬"," "," "," "," ",""," ",""],
                    ["╬"," "," "," "," ","","",""],
                    ["╩"," "," "," ",""," "," ",""]]
        
        indice = random.randint(1, numero_palabras_tot)  # Tomamos palabra y pista de archivo  
        
        while indice in palabra_usadas:
            indice = random.randint(1, numero_palabras_tot)
        
        palabra_usadas.append(indice)
        
        for i in range(indice):
            linea = entrada.readline()
        
        registros = linea.split("#")
        
        palabra = registros[0]
        pista = registros[1]
        
        letras_palabra = list(palabra)
        
        l_sin_rep = eliminar_l_rep(letras_palabra) # Crea un lista de letras a encontrar
        
        l_encontradas_us = []
        
        mostrar(figura, errores_us)
        
        while palabra_no_encontrada:
            mostrar_pista(pista)
            mostrar_letras_faltante(letras_palabra, l_encontradas_us)
            
            ingreso = input('Ingresar la letra(Ingresar "quit" para terminar el juego): ')
            
            ingreso = ver_entradas(ingreso)
            
            if ingreso == -1:
              continue
            if ingreso == 'quit':
              break
            
            if len(ingreso) > 1:    #Ingresa una palabra de solucion
                ingreso_grande = ingreso.upper()
                print(f" '{ingreso_grande}' va a ser tu respuesta final")
                rta_final = si_o_no()
                if rta_final:
                    if ingreso == palabra:
                        print(f"Correcto '{ingreso}' es la palabra secreta")
                        palabra_no_encontrada = False
                    else:
                        print(f"Incorrecto la palabra no es '{ingreso}'")
                        for i in range(len(ingreso)):
                            errores_us += 1
                else:
                    continue
                
            else:                   #Ingresa una letra de la palabra
                if ingreso in palabra:
                    if ingreso not in l_encontradas_us:
                        print()
                        print(f"La letra {ingreso} esta dentro de la palabra")
                        l_encontradas_us.append(ingreso)
                    else:
                        print(f"La letra {ingreso} ya fue encotrada")
                        print("Porfavor ingrese una nueva letra")
                else:
                     errores_us += 1
                     print(f"La letra {ingreso} no esta en en la palabra :(")
            
            agregar_errores(figura, errores_us)
            mostrar(figura, errores_us)
            if errores_us >= 7:
                break
            if len(l_encontradas_us) == len(l_sin_rep):
                palabra_no_encontrada = False
        
        if palabra_no_encontrada:
            print("No encontraste la palabra :(")
            print(f"La palabra secreta es '{palabra}'")
        else:
            print()
            print(f"Felicidades: has completado la palabra '{palabra}' y ganaste el juego :)")
            puntos = len(palabra)*12 - errores_us*10
            puntos_totales += puntos
            print("PUNTOS: ", puntos)
        if len(palabra_usadas) < numero_palabras_tot:  
          print("Queres seguir jugando?: ")
          us = si_o_no()
        else:
          print("Terminaste el juego, no quedan mas palabras para adivinar")
          us = False
        entrada.seek(0)


except FileNotFoundError as mensaje:
    print("Error no se encuantra en archivo: ", mensaje)
except OSError as mensaje:
    print("Error no se puede abrir el archivo: ", mensaje)
except KeyboardInterrupt:
    pass
finally:
    print()
    if puntos_totales > 0:
      print(f'Puntos totales: {puntos_totales}')
    print('Gracias por jugar :)')
    try:
        entrada.close()
    except NameError:
        pass
