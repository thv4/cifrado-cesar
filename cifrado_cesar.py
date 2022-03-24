
def cifradoCesar():
    a = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    b = str(input("dime la palabra a encriptar: "))
    c = int(input("dime la clave: "))
    mensaje = ""
    for i in b.upper():
        if i in a:
            indice = a.find(i)
            indice += c
            if indice >= 27:
                indice -= 27
            mensaje += a[indice]
        else:
            mensaje += i
    print(mensaje)
print("Bienvenido al cifrado cesar")
cifradoCesar()
