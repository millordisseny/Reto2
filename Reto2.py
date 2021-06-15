lista = ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana","Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo","Elegir opción de menú favorita","Cerrar sesión"]
cont=0

while True:
    
    try:
        # import os
        # os.system('cls')
        print ("1. ", lista [0])
        print ("2. ", lista [1])
        print ("3. ", lista [2])
        print ("4. ", lista [3])
        print ("5. ", lista [4])
        print ("6. ", lista [5])
        print ("7. ", lista [6])
        
        opcion = int(input("Elija una opción "))

        if opcion in range(8):

            if opcion == 7:
                print("Hasta pronto")
                break

            if opcion == 6:
                favorita = int (input("Seleccione opción favorita "))
                
                if favorita in range (6):
                    adivinanza_1 = int (input("Para confirmar por favor responda: Me separaron de mi hermano siamés, antes era un ocho y ahora soy un ... la respuesta es "))
                    if adivinanza_1==3:
                        adivinanza_2 = int(input("Para confirmar por favor responda: Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es "))
                        if adivinanza_2==9:
                            temporal = lista[favorita-1]
                            lista.remove(temporal)
                            lista.insert(0,temporal)
                        else:
                            print ("Error")
                    else:
                        print ("Error")
                else:
                    print ("Error Opción")
                    cont=cont+1
                    if cont==3:
                        break

            if opcion <= 5:
                print(f"Usted ha elegido la opción número {opcion}")
                break
            
    except ValueError:
        print("Error, ingrese solamente numeros")

