import sympy as smp
import sys

# FUNCION: Generar la funcion de error de propacacion simbolica a partir de una ecuacion simbolica
def ef(funcion, variables:list):
    # Generar los deltas para cada variable con error de medicion o con una incertidumbre asociada
    var_list = []
    for i in range(len(variables)):
        var = smp.Symbol(r"\delta"+ f" {variables[i]}")
        var_list.append(var)

    # Generar las derivadas parciales de la funcion respecto a cada una de las variables anteriores
    partial_list = []
    for j in range(len(variables)):
        partial = smp.diff(funcion, variables[j])
        partial_list.append(partial)

    # Generar el error cuadrado de cada variables
    ecpv_list = []
    for k in range(len(variables)):
        ecpv = (partial_list[k] * var_list[k])**2
        ecpv_list.append(ecpv)
    
    # Suma de los errores cuadraticos
    ecf = 0
    for a in range(len(ecpv_list)):
        ecf += ecpv_list[a]

    # Raiz de la suma de errores
    ef = smp.sqrt(ecf)

    var_t = var_list + variables

    return ef, var_t


# FUNCION: Convertir expresion simbolica a numerica
def ef_n(func_err, list_var, list_cons):

    list_aux = list_cons + list_var

    ef_n = smp.lambdify(list_aux, func_err)

    return ef_n


def error_propagacion(f,lista_var, lista_const, n1 = "Expresion simbolica", n2 = "Generar texto LATEX", 
                    n3 = "Conversion a expresion numerica"):

    E1 = "ERROR: Revisar opcion 1 ----> Generar expresion simbolica ----> input invalido "
    E2 = "ERROR: Revisar opcion 2 ----> Generar texto LATEX ----> input invalido"
    E3 = "ERROR: Revisar opcion 3 ----> Conversion a expresion numerica ----> input invalido"
    E = ("Los espacios: 'n1' , 'n2' y 'n3' son para escoger que output obtener de la funcion" +
        "\n" + "Unicamente son validos los sientes valores numericos ENTEROS" + "\n" + "1 ----> SI" + "\n" + "0 ----> NO")


    if n1 == 0 or n1 == 1:
        if n2 == 0 or n2 == 1:

            if n3 == 0 or n3 == 1:
                pass
            else: 
                print(E3 + "\n" + E )
                sys.exit(1) 
        else:
            if n3 == 0 or n3 == 1:
                    print(E2 + "\n" + E )
                    sys.exit(1)
            else: 
                    print(E2 + "\n" + E3 + "\n" + E )
                    sys.exit(1)
                
    else:
        if n2 == 0 or n2 == 1:
            if n3 == 0 or n3 == 1:
                    print(E1 + "\n" + E )
                    sys.exit(1)
            else: 
                    print(E1 + "\n" + E3 + "\n" + E )
                    sys.exit(1)
        else:
            if n3 == 0 or n3 == 1:
                    print(E1 + "\n" + E2 + "\n" + E )
                    sys.exit(1)
            else: 
                    print(E1 + "\n" + E2+ "\n" + E3 + "\n" + E )
                    sys.exit(1)


    F, var_listT = ef(f, lista_var)
    # 0 es no
    # 1 es si


    if n1 == 0:
        if n2 == 0:
            if n3 == 0:
                pass
            elif n3 == 1:
                FF = ef_n(F, lista_var + var_listT , lista_const)
                return FF
            

        elif n2 == 1:
            from sympy import latex
            L = latex(F)
            if n3 == 0:
                return L
            elif n3 == 1:
                FF = ef_n(F, lista_var + var_listT , lista_const)
                return L, FF
            

    elif n1 == 1:
        if n2 == 0:
            if n3 == 0:
                return F
            elif n3 == 1:
                return F, FF
        
        elif n2 == 1:
            from sympy import latex
            if n3 == 0:
                L = latex(F)
                return F,L
            elif n3 == 1:
                L = latex(F)
                FF = ef_n(F, lista_var + var_listT , lista_const)
                return F, L, FF