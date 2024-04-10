import ply.lex as lex

# Definición de tokens
tokens = (
    'RESERVADA',
    'IGUAL',
    'NUMERO',
    'PUNTO_Y_COMA',
    'MENOR_QUE',
    'INCREMENTO',
    'PARENTESIS_APERTURA',
    'PARENTESIS_CIERRE',
    'CORCHETE_APERTURA',
    'CORCHETE_CIERRE',
    'PUNTO',
    'COMILLA',
    'DOS_PUNTOS',
    'PALABRA_i',
    'MAS',
    'TOKEN_NO_VALIDO',
)

# Expresiones regulares para tokens simples
t_PUNTO = r'\.'
t_IGUAL = r'='
t_PUNTO_Y_COMA = r';'
t_INCREMENTO = r'\+\+'
t_PARENTESIS_APERTURA = r'\('
t_PARENTESIS_CIERRE = r'\)'
t_CORCHETE_APERTURA = r'{'
t_CORCHETE_CIERRE = r'}'
t_MENOR_QUE = r'<'
t_COMILLA = r'"'
t_DOS_PUNTOS = r':'
t_MAS = r'\+'
t_TOKEN_NO_VALIDO = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Expresión regular para números
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_RESERVADA(t):
    r'\b(for|int|System|out|println|Numero|using|namespace|class|prints|static|main|System)\b'
    t.type = 'RESERVADA'
    return t

def t_PALABRA_i(t):
    r'\bi\b'
    t.type = 'PALABRA_i'
    return t

# Ignorar espacios y saltos de línea
t_ignore = ' \t'

# Contador de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para manejar errores
def t_error(t):
    print(f"Token no válido '{t.value}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

def analizar_codigo(codigo):
    lexer.lineno = 1  
    lexer.input(codigo)
    tokens = []  
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)  
    return tokens  







