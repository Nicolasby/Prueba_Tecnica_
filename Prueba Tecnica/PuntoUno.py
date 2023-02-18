"""
Lo que hize fue crear una funcion que al ingresar una palabra me identificara 
la primera y la ultima letra de esta si las dos coinciden aumenta ala siguiente y disminuye la otra
aqui vuelve a identificar si coinciden  es true, si no es false.

en la funcion principal utilizamos "%s" esta convierte un valor en cadena y alli llamamos 
la palabra que digitamos para que la imprima

nota: "indague un poco en el tema palidromos y funciones
pero aun asi entiendo muy bien el codigo, utilice python" 
"""
def log(palabra):
    primera = 0
    ultima = len(palabra) - 1 
    while palabra[primera] == palabra[ultima]:
        if primera >= ultima:
            return True
        primera += 1
        ultima -= 1
    return False

def principal():
    poli=str(input("Digite la palabra: "))
    if log(poli):
        print("La palabra %s es un polindromo" %poli)
    else:
        print("La palabra %s no es un polindromo" %poli)
principal()
