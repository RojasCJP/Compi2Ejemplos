from grammar import grammar


def main():
    s = ''
    with open('tabulaciones.txt', 'r') as f:
        contenido = f.readlines()
        for element in contenido:
            s += element
    grammar.parse(s)

main()
