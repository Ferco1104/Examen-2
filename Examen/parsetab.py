_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMILLA CORCHETE_APERTURA CORCHETE_CIERRE DOS_PUNTOS IGUAL INCREMENTO MAS MENOR_QUE NUMERO PALABRA_i PARENTESIS_APERTURA PARENTESIS_CIERRE PUNTO PUNTO_Y_COMA RESERVADA TOKEN_NO_VALIDOciclo_for : RESERVADA PARENTESIS_APERTURA RESERVADA PALABRA_i IGUAL NUMERO PUNTO_Y_COMA PALABRA_i MENOR_QUE IGUAL NUMERO PUNTO_Y_COMA PALABRA_i INCREMENTO PARENTESIS_CIERRE CORCHETE_APERTURA instrucciones CORCHETE_CIERREinstrucciones : RESERVADA PUNTO RESERVADA PUNTO RESERVADA PARENTESIS_APERTURA COMILLA RESERVADA DOS_PUNTOS COMILLA MAS PALABRA_i PARENTESIS_CIERRE PUNTO_Y_COMA'
    
_lr_action_items = {'RESERVADA':([0,3,17,20,23,26,],[2,4,18,22,24,27,]),'$end':([1,21,],[0,-1,]),'PARENTESIS_APERTURA':([2,24,],[3,25,]),'PALABRA_i':([4,8,13,30,],[5,9,14,31,]),'IGUAL':([5,10,],[6,11,]),'NUMERO':([6,11,],[7,12,]),'PUNTO_Y_COMA':([7,12,32,],[8,13,33,]),'MENOR_QUE':([9,],[10,]),'INCREMENTO':([14,],[15,]),'PARENTESIS_CIERRE':([15,31,],[16,32,]),'CORCHETE_APERTURA':([16,],[17,]),'PUNTO':([18,22,],[20,23,]),'CORCHETE_CIERRE':([19,33,],[21,-2,]),'COMILLA':([25,28,],[26,29,]),'DOS_PUNTOS':([27,],[28,]),'MAS':([29,],[30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ciclo_for':([0,],[1,]),'instrucciones':([17,],[19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> ciclo_for","S'",1,None,None,None),
  ('ciclo_for -> RESERVADA PARENTESIS_APERTURA RESERVADA PALABRA_i IGUAL NUMERO PUNTO_Y_COMA PALABRA_i MENOR_QUE IGUAL NUMERO PUNTO_Y_COMA PALABRA_i INCREMENTO PARENTESIS_CIERRE CORCHETE_APERTURA instrucciones CORCHETE_CIERRE','ciclo_for',18,'p_ciclo_for','Sintactico.py',6),
  ('instrucciones -> RESERVADA PUNTO RESERVADA PUNTO RESERVADA PARENTESIS_APERTURA COMILLA RESERVADA DOS_PUNTOS COMILLA MAS PALABRA_i PARENTESIS_CIERRE PUNTO_Y_COMA','instrucciones',14,'p_instrucciones','Sintactico.py',11),
]
