
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftIGUALQUENIGUALQUEleftMAYQUEMENQUEMAYIGUALQUEMENIGUALQUEleftMASMENOSleftPORDIVIDIDOMODULOleftPOTENCIArightUMENOSAND BOOL BREAK CADENA COMA CONTINUE CORCHETEDER CORCHETEIZQ DECIMAL DEF DIVIDIDO DOSP ELIF ELSE END ENTERO FALSE FLOAT FOR ID IF IGUAL IGUALQUE IN INT LEN LINEANUEVA LLAVDER LLAVIZQ LOWER MAS MAYIGUALQUE MAYQUE MENIGUALQUE MENOS MENQUE MODULO NIGUALQUE NONE NOT OR PARDER PARIZQ POR POTENCIA PRINT PRINTLN PUNTO RETURN STR TRUE UPPER WHILEinit            : instruccionesinstrucciones    : instrucciones instruccion\n                        | instruccioninstruccion      : print_instr LINEANUEVA\n                        | println_instr LINEANUEVA\n                        | asignacion_instr LINEANUEVA\n                        | asignacion_arreglo_instr LINEANUEVA\n                        | definicion_asignacion_instr LINEANUEVA\n                        | call_function LINEANUEVA\n                        | declare_function LINEANUEVA\n                        | return_state LINEANUEVA\n                        | break_state LINEANUEVA\n                        | continue_state LINEANUEVA\n                        | if_state LINEANUEVA\n                        | while_state LINEANUEVA\n                        | for_state LINEANUEVA\n                        | nativas LINEANUEVA\nexpression       : MENOS expression %prec UMENOS\n                        | NOT expression %prec UMENOS\n                        | expression MAS expression\n                        | expression MENOS expression\n                        | expression POR expression\n                        | expression DIVIDIDO expression\n                        | expression POTENCIA expression\n                        | expression MODULO expression\n                        | expression MAYQUE expression\n                        | expression MENQUE expression\n                        | expression MENIGUALQUE expression\n                        | expression MAYIGUALQUE expression\n                        | expression IGUALQUE expression\n                        | expression NIGUALQUE expression\n                        | expression OR expression\n                        | expression AND expression\n                        | final_expressionfinal_expression     : PARIZQ expression PARDER\n                            | CORCHETEIZQ exp_list CORCHETEDER\n                            | DECIMAL\n                            | ENTERO\n                            | CADENA\n                            | ID\n                            | ID index_list  \n                            | TRUE\n                            | FALSE\n                            | call_function\n                            | nativasnativas          : UPPER PARIZQ expression PARDER\n                        | LOWER PARIZQ expression PARDER\n                        | STR PARIZQ expression PARDER\n                        | FLOAT PARIZQ expression PARDER\n                        | LEN PARIZQ expression PARDER\n                        print_instr    : PRINT PARIZQ exp_list PARDERprintln_instr  : PRINTLN PARIZQ exp_list PARDERtipo     : INT\n                | FLOAT\n                | BOOL\n                | STR\n                | NONE\n    asignacion_instr     : ID IGUAL expressiondefinicion_asignacion_instr  : ID  DOSP tipo IGUAL expressionasignacion_arreglo_instr     : ID index_list IGUAL expressioncall_function    : ID PARIZQ PARDER\n                        | ID PARIZQ exp_list PARDERexp_list         : exp_list COMA expression\n                        | expressionindex_list       : index_list CORCHETEIZQ expression CORCHETEDER\n                        | CORCHETEIZQ expression CORCHETEDERstatement        : instruccionesdeclare_function     : DEF ID PARIZQ dec_params PARDER DOSP statement END\n                            | DEF ID PARIZQ PARDER DOSP statement ENDdec_params :   dec_params COMA ID DOSP tipo\n                    | dec_params COMA ID\n                    | ID DOSP tipo\n                    | IDif_state     : IF expression DOSP statement END\n                    | IF expression DOSP statement ELSE DOSP statement END\n                    | IF expression DOSP statement else_if_list ENDelse_if_list     : ELIF expression DOSP statement\n                        | ELIF expression DOSP statement ELSE statement\n                        | ELIF expression DOSP statement else_if_listwhile_state      : WHILE expression DOSP statement ENDfor_state        : FOR ID IN expression DOSP expression DOSP statement END\n                        | FOR ID IN expression DOSP statement ENDbreak_state      : BREAKcontinue_state      : CONTINUEreturn_state     : RETURN\n                        | RETURN expression'
    
_lr_action_items = {'PRINT':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[18,18,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,18,18,18,18,18,18,18,18,18,18,]),'PRINTLN':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[19,19,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,19,19,19,19,19,19,19,19,19,19,]),'ID':([0,2,3,21,22,25,26,27,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,162,163,167,169,171,174,186,188,195,],[20,20,-3,55,65,65,65,72,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,129,65,65,65,65,65,65,65,65,65,65,65,65,65,65,20,20,65,65,65,20,172,20,65,177,20,20,20,20,20,]),'DEF':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[21,21,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,21,21,21,21,21,21,21,21,21,21,]),'RETURN':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[22,22,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,22,22,22,22,22,22,22,22,22,22,]),'BREAK':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[23,23,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,23,23,23,23,23,23,23,23,23,23,]),'CONTINUE':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[24,24,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,24,24,24,24,24,24,24,24,24,24,]),'IF':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[25,25,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,25,25,25,25,25,25,25,25,25,25,]),'WHILE':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[26,26,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,26,26,26,26,26,26,26,26,26,26,]),'FOR':([0,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,113,114,149,163,169,171,174,186,188,195,],[27,27,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,27,27,27,27,27,27,27,27,27,27,]),'UPPER':([0,2,3,22,25,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,163,167,169,171,174,186,188,195,],[28,28,-3,28,28,28,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'LOWER':([0,2,3,22,25,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,163,167,169,171,174,186,188,195,],[29,29,-3,29,29,29,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'STR':([0,2,3,22,25,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,160,163,167,169,171,174,183,186,188,195,],[30,30,-3,30,30,30,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,30,30,30,88,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,88,30,30,30,30,30,88,30,30,30,]),'FLOAT':([0,2,3,22,25,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,160,163,167,169,171,174,183,186,188,195,],[31,31,-3,31,31,31,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,31,31,31,86,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,86,31,31,31,31,31,86,31,31,31,]),'LEN':([0,2,3,22,25,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,163,167,169,171,174,186,188,195,],[32,32,-3,32,32,32,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'$end':([1,2,3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[0,-1,-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,]),'END':([3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,148,149,150,166,173,179,182,185,193,194,196,198,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,164,-67,168,175,184,189,190,192,-77,197,-79,-78,]),'ELSE':([3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,148,149,193,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,165,-67,195,]),'ELIF':([3,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,148,149,193,],[-3,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,167,-67,167,]),'LINEANUEVA':([4,5,6,7,8,9,10,11,12,13,14,15,16,17,22,23,24,56,59,62,63,64,65,66,67,68,69,81,90,108,109,112,121,123,124,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,152,153,154,155,156,158,159,164,168,175,180,181,184,189,190,192,197,],[34,35,36,37,38,39,40,41,42,43,44,45,46,47,-85,-83,-84,-86,-34,-37,-38,-39,-40,-42,-43,-44,-45,-58,-61,-18,-19,-41,-51,-52,-60,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,-46,-47,-48,-49,-50,-65,-59,-74,-80,-76,39,47,-69,-82,-68,-75,-81,]),'PARIZQ':([18,19,20,22,25,26,28,29,30,31,32,48,49,50,53,54,55,57,58,60,61,65,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,177,],[48,49,53,60,60,60,73,74,75,76,77,60,60,60,60,60,93,60,60,60,60,53,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,53,]),'IGUAL':([20,51,84,85,86,87,88,89,128,158,177,187,],[50,82,126,-53,-54,-55,-56,-57,-66,-65,50,82,]),'DOSP':([20,59,62,63,64,65,66,67,68,69,70,71,90,108,109,112,127,128,129,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,158,161,165,172,176,177,178,180,181,187,],[52,-34,-37,-38,-39,-40,-42,-43,-44,-45,113,114,-61,-18,-19,-41,-62,-66,160,163,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,169,-46,-47,-48,-49,-50,-65,171,174,183,186,52,188,-44,-45,-41,]),'CORCHETEIZQ':([20,22,25,26,48,49,50,51,53,54,57,58,60,61,65,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,112,115,122,126,128,158,167,169,177,187,],[54,61,61,61,61,61,61,83,61,61,61,61,61,61,54,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,83,61,61,61,-66,-65,61,61,54,83,]),'MENOS':([22,25,26,48,49,50,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,73,74,75,76,77,79,81,82,83,90,92,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,112,115,116,117,118,119,120,122,124,125,126,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,167,169,176,177,178,180,181,187,],[57,57,57,57,57,57,57,57,95,57,57,-34,57,57,-37,-38,-39,-40,-42,-43,-44,-45,95,95,57,57,57,57,57,95,95,57,57,-61,95,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-18,-19,95,-41,57,95,95,95,95,95,57,95,95,57,-62,-66,-20,-21,-22,-23,-24,-25,95,95,95,95,95,95,95,95,-35,-36,95,-46,-47,-48,-49,-50,95,-65,95,57,57,95,-40,95,-44,-45,-41,]),'NOT':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'DECIMAL':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'ENTERO':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'CADENA':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'TRUE':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'FALSE':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'INT':([52,160,183,],[85,85,85,]),'BOOL':([52,160,183,],[87,87,87,]),'NONE':([52,160,183,],[89,89,89,]),'PARDER':([53,59,62,63,64,65,66,67,68,69,78,79,80,85,86,87,88,89,90,91,93,108,109,110,112,116,117,118,119,120,127,128,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,152,153,154,155,156,157,158,170,172,191,],[90,-34,-37,-38,-39,-40,-42,-43,-44,-45,121,-64,123,-53,-54,-55,-56,-57,-61,127,131,-18,-19,146,-41,152,153,154,155,156,-62,-66,-73,161,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,-46,-47,-48,-49,-50,-63,-65,-72,-71,-70,]),'MAS':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[94,-34,-37,-38,-39,-40,-42,-43,-44,-45,94,94,94,94,-61,94,-18,-19,94,-41,94,94,94,94,94,94,94,-62,-66,-20,-21,-22,-23,-24,-25,94,94,94,94,94,94,94,94,-35,-36,94,-46,-47,-48,-49,-50,94,-65,94,94,-40,94,-44,-45,-41,]),'POR':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[96,-34,-37,-38,-39,-40,-42,-43,-44,-45,96,96,96,96,-61,96,-18,-19,96,-41,96,96,96,96,96,96,96,-62,-66,96,96,-22,-23,-24,-25,96,96,96,96,96,96,96,96,-35,-36,96,-46,-47,-48,-49,-50,96,-65,96,96,-40,96,-44,-45,-41,]),'DIVIDIDO':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[97,-34,-37,-38,-39,-40,-42,-43,-44,-45,97,97,97,97,-61,97,-18,-19,97,-41,97,97,97,97,97,97,97,-62,-66,97,97,-22,-23,-24,-25,97,97,97,97,97,97,97,97,-35,-36,97,-46,-47,-48,-49,-50,97,-65,97,97,-40,97,-44,-45,-41,]),'POTENCIA':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[98,-34,-37,-38,-39,-40,-42,-43,-44,-45,98,98,98,98,-61,98,-18,-19,98,-41,98,98,98,98,98,98,98,-62,-66,98,98,98,98,-24,98,98,98,98,98,98,98,98,98,-35,-36,98,-46,-47,-48,-49,-50,98,-65,98,98,-40,98,-44,-45,-41,]),'MODULO':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[99,-34,-37,-38,-39,-40,-42,-43,-44,-45,99,99,99,99,-61,99,-18,-19,99,-41,99,99,99,99,99,99,99,-62,-66,99,99,-22,-23,-24,-25,99,99,99,99,99,99,99,99,-35,-36,99,-46,-47,-48,-49,-50,99,-65,99,99,-40,99,-44,-45,-41,]),'MAYQUE':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[100,-34,-37,-38,-39,-40,-42,-43,-44,-45,100,100,100,100,-61,100,-18,-19,100,-41,100,100,100,100,100,100,100,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,100,100,100,100,-35,-36,100,-46,-47,-48,-49,-50,100,-65,100,100,-40,100,-44,-45,-41,]),'MENQUE':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[101,-34,-37,-38,-39,-40,-42,-43,-44,-45,101,101,101,101,-61,101,-18,-19,101,-41,101,101,101,101,101,101,101,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,101,101,101,101,-35,-36,101,-46,-47,-48,-49,-50,101,-65,101,101,-40,101,-44,-45,-41,]),'MENIGUALQUE':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[102,-34,-37,-38,-39,-40,-42,-43,-44,-45,102,102,102,102,-61,102,-18,-19,102,-41,102,102,102,102,102,102,102,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,102,102,102,102,-35,-36,102,-46,-47,-48,-49,-50,102,-65,102,102,-40,102,-44,-45,-41,]),'MAYIGUALQUE':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[103,-34,-37,-38,-39,-40,-42,-43,-44,-45,103,103,103,103,-61,103,-18,-19,103,-41,103,103,103,103,103,103,103,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,103,103,103,103,-35,-36,103,-46,-47,-48,-49,-50,103,-65,103,103,-40,103,-44,-45,-41,]),'IGUALQUE':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[104,-34,-37,-38,-39,-40,-42,-43,-44,-45,104,104,104,104,-61,104,-18,-19,104,-41,104,104,104,104,104,104,104,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,104,104,-35,-36,104,-46,-47,-48,-49,-50,104,-65,104,104,-40,104,-44,-45,-41,]),'NIGUALQUE':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[105,-34,-37,-38,-39,-40,-42,-43,-44,-45,105,105,105,105,-61,105,-18,-19,105,-41,105,105,105,105,105,105,105,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,105,105,-35,-36,105,-46,-47,-48,-49,-50,105,-65,105,105,-40,105,-44,-45,-41,]),'OR':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[106,-34,-37,-38,-39,-40,-42,-43,-44,-45,106,106,106,106,-61,106,-18,-19,106,-41,106,106,106,106,106,106,106,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,106,-46,-47,-48,-49,-50,106,-65,106,106,-40,106,-44,-45,-41,]),'AND':([56,59,62,63,64,65,66,67,68,69,70,71,79,81,90,92,108,109,110,112,116,117,118,119,120,124,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,151,152,153,154,155,156,157,158,159,176,177,178,180,181,187,],[107,-34,-37,-38,-39,-40,-42,-43,-44,-45,107,107,107,107,-61,107,-18,-19,107,-41,107,107,107,107,107,107,107,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,107,-33,-35,-36,107,-46,-47,-48,-49,-50,107,-65,107,107,-40,107,-44,-45,-41,]),'COMA':([59,62,63,64,65,66,67,68,69,78,79,80,85,86,87,88,89,90,91,108,109,111,112,127,128,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,152,153,154,155,156,157,158,170,172,191,],[-34,-37,-38,-39,-40,-42,-43,-44,-45,122,-64,122,-53,-54,-55,-56,-57,-61,122,-18,-19,122,-41,-62,-66,-73,162,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,-46,-47,-48,-49,-50,-63,-65,-72,-71,-70,]),'CORCHETEDER':([59,62,63,64,65,66,67,68,69,79,90,92,108,109,111,112,125,127,128,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,152,153,154,155,156,157,158,],[-34,-37,-38,-39,-40,-42,-43,-44,-45,-64,-61,128,-18,-19,147,-41,158,-62,-66,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-35,-36,-46,-47,-48,-49,-50,-63,-65,]),'IN':([72,],[115,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,113,114,163,169,171,174,186,188,195,],[2,149,149,149,149,149,149,149,149,149,]),'instruccion':([0,2,113,114,149,163,169,171,174,186,188,195,],[3,33,3,3,33,3,3,3,3,3,3,3,]),'print_instr':([0,2,113,114,149,163,169,171,174,186,188,195,],[4,4,4,4,4,4,4,4,4,4,4,4,]),'println_instr':([0,2,113,114,149,163,169,171,174,186,188,195,],[5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,113,114,149,163,169,171,174,186,188,195,],[6,6,6,6,6,6,6,6,6,6,6,6,]),'asignacion_arreglo_instr':([0,2,113,114,149,163,169,171,174,186,188,195,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'definicion_asignacion_instr':([0,2,113,114,149,163,169,171,174,186,188,195,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'call_function':([0,2,22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,163,167,169,171,174,186,188,195,],[9,9,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,9,9,68,68,68,9,9,68,180,9,9,9,9,9,]),'declare_function':([0,2,113,114,149,163,169,171,174,186,188,195,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'return_state':([0,2,113,114,149,163,169,171,174,186,188,195,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'break_state':([0,2,113,114,149,163,169,171,174,186,188,195,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'continue_state':([0,2,113,114,149,163,169,171,174,186,188,195,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'if_state':([0,2,113,114,149,163,169,171,174,186,188,195,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'while_state':([0,2,113,114,149,163,169,171,174,186,188,195,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'for_state':([0,2,113,114,149,163,169,171,174,186,188,195,],[16,16,16,16,16,16,16,16,16,16,16,16,]),'nativas':([0,2,22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,113,114,115,122,126,149,163,167,169,171,174,186,188,195,],[17,17,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,17,17,69,69,69,17,17,69,181,17,17,17,17,17,]),'index_list':([20,65,177,],[51,112,187,]),'expression':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[56,70,71,79,79,81,79,92,108,109,110,79,116,117,118,119,120,124,125,132,133,134,135,136,137,138,139,140,141,142,143,144,145,151,157,159,176,178,]),'final_expression':([22,25,26,48,49,50,53,54,57,58,60,61,73,74,75,76,77,82,83,94,95,96,97,98,99,100,101,102,103,104,105,106,107,115,122,126,167,169,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'exp_list':([48,49,53,61,],[78,80,91,111,]),'tipo':([52,160,183,],[84,170,191,]),'dec_params':([93,],[130,]),'statement':([113,114,163,169,171,174,186,188,195,],[148,150,173,179,182,185,193,194,198,]),'else_if_list':([148,193,],[166,196,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','main.py',163),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_lista','main.py',166),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_lista','main.py',167),
  ('instruccion -> print_instr LINEANUEVA','instruccion',2,'p_instruccion','main.py',170),
  ('instruccion -> println_instr LINEANUEVA','instruccion',2,'p_instruccion','main.py',171),
  ('instruccion -> asignacion_instr LINEANUEVA','instruccion',2,'p_instruccion','main.py',172),
  ('instruccion -> asignacion_arreglo_instr LINEANUEVA','instruccion',2,'p_instruccion','main.py',173),
  ('instruccion -> definicion_asignacion_instr LINEANUEVA','instruccion',2,'p_instruccion','main.py',174),
  ('instruccion -> call_function LINEANUEVA','instruccion',2,'p_instruccion','main.py',175),
  ('instruccion -> declare_function LINEANUEVA','instruccion',2,'p_instruccion','main.py',176),
  ('instruccion -> return_state LINEANUEVA','instruccion',2,'p_instruccion','main.py',177),
  ('instruccion -> break_state LINEANUEVA','instruccion',2,'p_instruccion','main.py',178),
  ('instruccion -> continue_state LINEANUEVA','instruccion',2,'p_instruccion','main.py',179),
  ('instruccion -> if_state LINEANUEVA','instruccion',2,'p_instruccion','main.py',180),
  ('instruccion -> while_state LINEANUEVA','instruccion',2,'p_instruccion','main.py',181),
  ('instruccion -> for_state LINEANUEVA','instruccion',2,'p_instruccion','main.py',182),
  ('instruccion -> nativas LINEANUEVA','instruccion',2,'p_instruccion','main.py',183),
  ('expression -> MENOS expression','expression',2,'p_expression','main.py',188),
  ('expression -> NOT expression','expression',2,'p_expression','main.py',189),
  ('expression -> expression MAS expression','expression',3,'p_expression','main.py',190),
  ('expression -> expression MENOS expression','expression',3,'p_expression','main.py',191),
  ('expression -> expression POR expression','expression',3,'p_expression','main.py',192),
  ('expression -> expression DIVIDIDO expression','expression',3,'p_expression','main.py',193),
  ('expression -> expression POTENCIA expression','expression',3,'p_expression','main.py',194),
  ('expression -> expression MODULO expression','expression',3,'p_expression','main.py',195),
  ('expression -> expression MAYQUE expression','expression',3,'p_expression','main.py',196),
  ('expression -> expression MENQUE expression','expression',3,'p_expression','main.py',197),
  ('expression -> expression MENIGUALQUE expression','expression',3,'p_expression','main.py',198),
  ('expression -> expression MAYIGUALQUE expression','expression',3,'p_expression','main.py',199),
  ('expression -> expression IGUALQUE expression','expression',3,'p_expression','main.py',200),
  ('expression -> expression NIGUALQUE expression','expression',3,'p_expression','main.py',201),
  ('expression -> expression OR expression','expression',3,'p_expression','main.py',202),
  ('expression -> expression AND expression','expression',3,'p_expression','main.py',203),
  ('expression -> final_expression','expression',1,'p_expression','main.py',204),
  ('final_expression -> PARIZQ expression PARDER','final_expression',3,'p_final_expression','main.py',207),
  ('final_expression -> CORCHETEIZQ exp_list CORCHETEDER','final_expression',3,'p_final_expression','main.py',208),
  ('final_expression -> DECIMAL','final_expression',1,'p_final_expression','main.py',209),
  ('final_expression -> ENTERO','final_expression',1,'p_final_expression','main.py',210),
  ('final_expression -> CADENA','final_expression',1,'p_final_expression','main.py',211),
  ('final_expression -> ID','final_expression',1,'p_final_expression','main.py',212),
  ('final_expression -> ID index_list','final_expression',2,'p_final_expression','main.py',213),
  ('final_expression -> TRUE','final_expression',1,'p_final_expression','main.py',214),
  ('final_expression -> FALSE','final_expression',1,'p_final_expression','main.py',215),
  ('final_expression -> call_function','final_expression',1,'p_final_expression','main.py',216),
  ('final_expression -> nativas','final_expression',1,'p_final_expression','main.py',217),
  ('nativas -> UPPER PARIZQ expression PARDER','nativas',4,'p_nativas','main.py',220),
  ('nativas -> LOWER PARIZQ expression PARDER','nativas',4,'p_nativas','main.py',221),
  ('nativas -> STR PARIZQ expression PARDER','nativas',4,'p_nativas','main.py',222),
  ('nativas -> FLOAT PARIZQ expression PARDER','nativas',4,'p_nativas','main.py',223),
  ('nativas -> LEN PARIZQ expression PARDER','nativas',4,'p_nativas','main.py',224),
  ('print_instr -> PRINT PARIZQ exp_list PARDER','print_instr',4,'p_print_instr','main.py',228),
  ('println_instr -> PRINTLN PARIZQ exp_list PARDER','println_instr',4,'p_println_instr','main.py',231),
  ('tipo -> INT','tipo',1,'p_tipo','main.py',234),
  ('tipo -> FLOAT','tipo',1,'p_tipo','main.py',235),
  ('tipo -> BOOL','tipo',1,'p_tipo','main.py',236),
  ('tipo -> STR','tipo',1,'p_tipo','main.py',237),
  ('tipo -> NONE','tipo',1,'p_tipo','main.py',238),
  ('asignacion_instr -> ID IGUAL expression','asignacion_instr',3,'p_asignacion_instr','main.py',242),
  ('definicion_asignacion_instr -> ID DOSP tipo IGUAL expression','definicion_asignacion_instr',5,'p_definicion_asignacion_instr','main.py',245),
  ('asignacion_arreglo_instr -> ID index_list IGUAL expression','asignacion_arreglo_instr',4,'p_asignacion_arreglo_instr','main.py',248),
  ('call_function -> ID PARIZQ PARDER','call_function',3,'p_call_function_instr','main.py',251),
  ('call_function -> ID PARIZQ exp_list PARDER','call_function',4,'p_call_function_instr','main.py',252),
  ('exp_list -> exp_list COMA expression','exp_list',3,'p_exp_list_instr','main.py',255),
  ('exp_list -> expression','exp_list',1,'p_exp_list_instr','main.py',256),
  ('index_list -> index_list CORCHETEIZQ expression CORCHETEDER','index_list',4,'p_index_list_instr','main.py',259),
  ('index_list -> CORCHETEIZQ expression CORCHETEDER','index_list',3,'p_index_list_instr','main.py',260),
  ('statement -> instrucciones','statement',1,'p_statement','main.py',263),
  ('declare_function -> DEF ID PARIZQ dec_params PARDER DOSP statement END','declare_function',8,'p_declare_function','main.py',266),
  ('declare_function -> DEF ID PARIZQ PARDER DOSP statement END','declare_function',7,'p_declare_function','main.py',267),
  ('dec_params -> dec_params COMA ID DOSP tipo','dec_params',5,'p_dec_params','main.py',270),
  ('dec_params -> dec_params COMA ID','dec_params',3,'p_dec_params','main.py',271),
  ('dec_params -> ID DOSP tipo','dec_params',3,'p_dec_params','main.py',272),
  ('dec_params -> ID','dec_params',1,'p_dec_params','main.py',273),
  ('if_state -> IF expression DOSP statement END','if_state',5,'p_if_state','main.py',276),
  ('if_state -> IF expression DOSP statement ELSE DOSP statement END','if_state',8,'p_if_state','main.py',277),
  ('if_state -> IF expression DOSP statement else_if_list END','if_state',6,'p_if_state','main.py',278),
  ('else_if_list -> ELIF expression DOSP statement','else_if_list',4,'p_else_if_list','main.py',281),
  ('else_if_list -> ELIF expression DOSP statement ELSE statement','else_if_list',6,'p_else_if_list','main.py',282),
  ('else_if_list -> ELIF expression DOSP statement else_if_list','else_if_list',5,'p_else_if_list','main.py',283),
  ('while_state -> WHILE expression DOSP statement END','while_state',5,'p_while_state','main.py',286),
  ('for_state -> FOR ID IN expression DOSP expression DOSP statement END','for_state',9,'p_for_state','main.py',289),
  ('for_state -> FOR ID IN expression DOSP statement END','for_state',7,'p_for_state','main.py',290),
  ('break_state -> BREAK','break_state',1,'p_break','main.py',293),
  ('continue_state -> CONTINUE','continue_state',1,'p_continue','main.py',296),
  ('return_state -> RETURN','return_state',1,'p_return','main.py',299),
  ('return_state -> RETURN expression','return_state',2,'p_return','main.py',300),
]
