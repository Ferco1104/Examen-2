import ply.yacc as yacc
from lexico import tokens

# Regla de producción para el ciclo for
def p_ciclo_for(p):
    '''ciclo_for : RESERVADA PARENTESIS_APERTURA RESERVADA PALABRA_i IGUAL NUMERO PUNTO_Y_COMA PALABRA_i MENOR_QUE IGUAL NUMERO PUNTO_Y_COMA PALABRA_i INCREMENTO PARENTESIS_CIERRE CORCHETE_APERTURA instrucciones CORCHETE_CIERRE'''
    p[0] = 'Ciclo For'

# Regla de producción para las instrucciones dentro del ciclo for
def p_instrucciones(p):
    '''instrucciones : RESERVADA PUNTO RESERVADA PUNTO RESERVADA PARENTESIS_APERTURA COMILLA RESERVADA DOS_PUNTOS COMILLA MAS PALABRA_i PARENTESIS_CIERRE PUNTO_Y_COMA'''
    p[0] = 'Instrucción dentro del ciclo For'


error_sintactico = None

# Regla de producción para manejar errores sintácticos
def p_error(p):
    global error_sintactico
    if p:
        error_sintactico = p.value
        print(f"Error sintáctico de tipo '{p.value}' en la línea {p.lineno}")

# Construir el parser
parser = yacc.yacc()

# Función para analizar el código

def analizar_codigo(codigo):
    global error_sintactico
    error_sintactico = None  # Reiniciar el error sintáctico
    resultado = parser.parse(codigo)
    if resultado is not None:
        return "Análisis sintáctico exitoso: Ciclo For"
    else:
        if error_sintactico:
            return f"Error sintáctico de tipo '{error_sintactico}'"
        else:
            return "Error sintáctico desconocido"
















