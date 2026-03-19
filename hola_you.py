def main():
    nombre=input("Cual es tu nombre? ")
    appater=input("Cual es tu apellido paterno? ")
    apmater=input("Cual es tu apellido materno? ")
    nacimiento=input("Cual es tu año de nacimiento? ")
    edad=2022-int(nacimiento)
    print("\nNombre completo: ",nombre,appater,apmater,"\nEdad: ",edad,"años")
    print("¡Buen dia ",nombre,"!")
main()