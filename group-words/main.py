#Variables Globales
group_words = {}
#Funciones
def run(words: list) -> dict:
    # TODO
    global group_words
    #Variables locales
    for palabra in words:
        primeraLetra = palabra[0]
        if primeraLetra not in group_words:
            group_words[primeraLetra] = []
        
        group_words[primeraLetra].append(palabra)
    return group_words



#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(group_words)
