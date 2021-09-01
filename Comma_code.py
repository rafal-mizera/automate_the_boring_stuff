def comma_code(l):
    x = ""
    for slowo in lista:
        if lista.index(slowo) < len(lista) - 1:
            x += slowo + ", "
        else:
            x += "and " + slowo
    return x

lista = ["kupa","lustro","kibel","podłoga"]

print(comma_code(lista))

