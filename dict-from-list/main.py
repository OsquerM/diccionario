#Variables globales
unpack_items = {}
#Funciones
def run(items: list) -> dict:
    # TODO
    global unpack_items
    #Variables locales
    for objeto in items:
        unpack_items[objeto[0]] = objeto[1:]

    return unpack_items

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(unpack_items)