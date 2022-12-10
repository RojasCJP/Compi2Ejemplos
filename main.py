from grammar import grammar
from sym.Environment import *
from sym.Generator import *

def main():
    s = ''
    with open('tabulaciones.txt', 'r') as f:
        contenido = f.readlines()
        for element in contenido:
            s += element
    gen_aux = Generator()
    gen_aux.clean_all()
    generator = gen_aux.get_instance()
    new_env = Environment(None)
    ast = grammar.parse(s)
    try:
        for inst in ast:
            inst.compile(new_env)
        C3D = generator.get_code()
        f = open("salida.go", 'w')
        f.write(C3D)
        f.close()
        generator.clean_all()
        return C3D
    except Exception as e:
        print("no se puede compilar", e)
        error = {}
        error['type'] = 'no contemplado'
        error['text'] =  'no se puede compilar'
        Environment.errores.append(error)
    return 'error'


main()
