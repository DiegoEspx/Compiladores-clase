from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser

class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    try:
        tree = parser.prog()
        print("✅ Entrada válida.")
    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

if __name__ == "__main__":
    print("=== Entrada válida ===")
    parse_input("class A { int x; }")

    print("\n=== Entrada con error 1 ===")
    parse_input("class B { int f(x) { a = 3 + 4 + 5; } }")

    print("\n=== Entrada con error 2 ===")
    parse_input("class C { int f(x) { a = 3 + 5; } }")

    print('Entradas mal formadas para práctica de reporte y recuperación de errores')
    print("\n===  primer error ===")
    parse_input("class A { int x; }")

    print("\n===  segundo error ===")
    parse_input("class Z{ int x; }")

    print("\n===  tercero error ===")
    parse_input("class B { int f() { x = 3; } }")

    print("\n===  cuarto error ===")
    parse_input("class C { int f(a) { x = 3; } }")

    print("\n===  quinto error ===")
    parse_input("class D { int f(a) { f = 3; } }")

    print("\n===  sexto error ===")
    parse_input("class E { int f(a) { x = 3 + 4 + 5; } }")

    print("\n===  septimo error ===")
    parse_input("class F { int f(a) { x = 1; }}")

    print("\n===  octavo error ===")
    parse_input("class G { int f(a) {x = 1;} }")

    print("\n===  noveno error ===")
    parse_input("class H {int f(a) {x = 1;} }")

    print("\n===  decimo error ===")
    parse_input("class I { int f(x) { } }")




    