#Variables globales
fitems = {}

#Funciones
def run(items: dict) -> dict:
    # TODO
    global fitems
    #Variables locales
    for letra, value in items.items():
        nuevaClave = letra.replace(" ", "")
        fitems[nuevaClave] = value

    return fitems

#Funciones
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(fitems)