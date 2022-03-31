import sys

colecciones = {"list": list(), "tuple": tuple(), "dict": dict(), "set": set()}

print(colecciones.items())

for name, value in colecciones.items():
    print(f'{name} = {sys.getsizeof(value)} bytes')
