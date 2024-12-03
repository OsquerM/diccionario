#Variables globales
citems = {}
#Funciones
def run(items: dict) -> dict:
    # TODO
    global citems
    #Variables locales 
    for letra in items:
        citems[letra] = []
    return citems

#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(citems)