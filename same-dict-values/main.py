#Variables globales
all_same = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
#Funciones
def run(items: dict) -> bool:
    # TODO
    global all_same
    valores = list(items.values())
    #Values lo que hace es obtener los valores del diccionario

    # Comprobar si todos los valores son iguales
    return len(set(valores)) == 1
    #El set lo que hace es borrar los valores duplicados
#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(run(all_same))