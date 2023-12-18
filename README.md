# Funcion_error

Esta es una funcion para calcular errores de propagación de alguna expresión matemática

Para utilizar la función es necesario instalar sympy

La función es propiamente: "error_propagacion" 

Esta requiere de una expresión simbolica de la función a la que le desea sacar la incertidumbre de propagación, una lista de las variables que desea considerar y de haber, una lista de las "constantes" o variables que no desea considerar 


ENTRADAS DE LA FUNCIÓN

1) Función simbólica de interés de sympy
2) Lista de variables que poseen error
3) Lista de variables (constantes) que no se les considera error, de colocar ninguna se considerará todo como una variable con error

Las siguientes entradas corresponden a opciones que se tienen sobre los outputs
1 ---> Sí \\

0 ---> No

4) Visualizar unicamente la expresión del error de propagación (0 ó 1)
5) Generar texto en formato latex (0 ó 1)
6) Convertir la expresión simbólica en una expresión numérica para realizar cálculos (0 ó 1)
