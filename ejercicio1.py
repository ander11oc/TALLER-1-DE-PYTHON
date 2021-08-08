print("¿Cómo se llama?")
nombre = input()
edad = int(input("¿Cuál es su edad? "))
print("¿Cual es tu genero?")
genero = input()
laborar = input("¿Labora actualmente?  SI O NO").lower()


if laborar == 'no':
    print("¿Busca trabajo? SI o NO")
    respuesta = input().lower()
    if respuesta == 'si':
        print(f"Me alegro de conocerle, {nombre}")
        print(f"Veo que tiene , {edad} años")
        print(f"Genero , {genero}")
        print ("Buscaremos algo para usted.")
    else:
        print(f"Me alegro de conocerle, {nombre}")
        print(f"Veo que tiene , {edad} años")
        print(f"Genero , {genero}")
else:
    print(f"Me alegro de conocerle, {nombre}")
    print(f"Veo que tiene, {edad} años")
    print(f"Genero , {genero}")
    print("Felicitaciones actualmente labora.")