Definición formal de una función.
=================================

Dominio.
--------

A el conjunto de posibles argumentos de una función se le conoce como
**dominio**, utilizando la analogía de la máquina podemos pensar al
dominio como todos los posibles "inputs" que la máquina puede recibir.
Es posible restringir el dominio de una función, solamente hay que
escribir dentro de la definición de nuestra función el dominio que
queramos asignarle.

Por ejemplo: Sea la función $f(x) = 2x;x \geq 0$, esto quiere decir que
el dominio esta restringido a los números que sean iguales o mayores que
cero, así por ejemplo, podemos obtener los valores de $f(1) = 2$,
$f(3) = 6$ o $f(0.45) = 0.9$, sin embargo, para los valores que sean
menores que cero la función se considera *indefinida*.

Si no se indica explícitamente el dominio de la función, entonces se
asume que el dominio son todos los números reales $\mathbb{R}$, esto se
conoce como *dominio implícito*.[^1] Por lo tanto, podemos asumir que la
función $g(x) = 3x$ esta definida para todos los números reales,
mientras que la función $h(x) = 3x,x > 5$ solo esta definida para los
números que esan mayores que $5$. Nota que, aunque las funciones $g(x)$
y $h(x)$ tienen la misma fórmula **NO** son iguales. Dos funciones son
iguales si y solo si comparten el mismo dominio, el mismo rango y la
misma correspondencia entre elementos.

Sin embargo, aunque una función tenga dominio implícito, este puede que
no sean todos lo números reales $\mathbb{R}$, esto debido a ciertas
particularidades de las matemáticas. Por ejemplo, la función:

$$f(x) = \frac{x^{2} - 4}{x - 2}$$

no esta definida en $x = 2$, debido a que:

$$f(2) = \frac{(2)^{2} - 4}{2 - 2} = \frac{0}{0}$$

y por lo tanto su dominio son todos los números reales **excepto** 2.
Esto es expresado como
$\text{Dom}_{f_{}} = ( - \infty,2) \cup (2,\infty)$.

Considera la función:

$$g(x) = \frac{1}{x(x - 1)}$$

esta función tiene dos valores donde esta indefinida: $x = 0$ y $x = 1$

$$g(0) = \frac{1}{0(0 - 1)} = \frac{1}{0}$$

$$g(1) = \frac{1}{1(1 - 1)} = \frac{1}{0}$$

y por lo tanto su dominio son todos lo números reales **excepto** 0 y 1.
Esto se expresa como:
$\text{Dom}_{g_{}} = ( - \infty,0) \cup (0,1) \cup (1,\infty)$.

Problemas potenciales para funciones con dominio implícito.
-----------------------------------------------------------

Solo tenemos que preocuparnos por tres problemas que se pueden
presentar:

1.  División entre cero.
2.  Raíces de números negativos.
3.  Logaritmos de números iguales o menores que cero.

Rango.
------

Al conjunto de todos los posibles valores que pueden producir una
función se le conoce como rango. Utilizando la analogía de la maquina el
rango serian todos los elementos que la maquina puede producir. Por
ejemplo, considera la función:

$$f(x) = x^{2} + 1$$

Nota que el dominio de esta función son todos lo números reales, sin
embargo, esta función no puede producir ciertos valores, en particular
es imposible que esta función produzca algún número menor que 1, esto se
debe a que el término $x^{2}$ solo puede producir números positivos. Por
lo tanto, su rango son los números reales mayores o iguales a 1, esto de
denota como:

$$\text{Ran}_{f_{}} = \lbrack 1,\infty)$$

Otra función por considerar es $f(x) = x^{3}$, en este caso esta función
es capaz de producir cualquier número real. Por ejemplo, esta función es
capaz de producir al número 8 si usas como argumento al número 2
($f(2) = 2^{3} = 8$). Pero tambien es capaz de producir al número $- 8$
si usas como argumento al número $- 2$ ($f( - 2) = ( - 2)^{3} = - 8$).
Tambien puede producir al número 10, ahora usa como argumento
$\sqrt[3]{10}$ ($f(\sqrt[3]{10}) = (\sqrt[3]{10})^{3} = 10$).

Como identificar el dominio y rango de una función usando su gráfica.
---------------------------------------------------------------------

Para identificar el dominio en la gráfica observamos los valores donde
$x$ esta definida, en nuestro ejemplo todos los valores una salida en la
función y por lo tanto podemos determinar que el dominio de nuestra
función son todos los números reales.

Para identificar el rango observaos lo valores donde $y$ esta definida,
en nuestro ejemplo solo los valores que son iguales o mayores que cero
están definidos. Esto se debe a que cualquier valor al ser elevado al
cuadrado es positivo.

En este otro ejemplo nota que los valores que están a la izquierda de
cero no esta definidos. Esto es debido a que no existen raíces de
números negativos.

El rango de esta función son todos los números positivos mayores o
iguales que cero. Nota que es un poco difícil de apreciar en la gráfica
debido a su tamaño.

Función inversa
---------------

Considera la función $f(x) = x^{3} + 1$, y considera su comportamiento
desde $- 3$ hasta $3$:

  $$x$$     $$f(x)$$
  --------- --------------------
  $$- 3$$   $$f( - 3) = - 26$$
  $$- 2$$   $$f( - 2) = - 7$$
  $$- 1$$   $$f( - 1) = 0$$
  $$0$$     $$f(0) = 1$$
  $$1$$     $$f(1) = 2$$
  $$2$$     $$f(2) = 9$$
  $$3$$     $$f(3) = 28$$

La función inversa de $f(x) = x^{3} + 1$ es una función que denotamos
como $f^{- 1}(x)$ tal que tiene el siguiente comportamiento:

  $$x$$      $$f^{- 1}(x)$$
  ---------- --------------------
  $$- 26$$   $$f( - 26) = - 3$$
  $$- 7$$    $$f( - 7) = - 2$$
  $$0$$      $$f(0) = - 1$$
  $$1$$      $$f(1) = 0$$
  $$2$$      $$f(2) = 1$$
  $$9$$      $$f(9) = 2$$
  $$28$$     $$f(28) = 3$$

Dicho de otra manera: "Deshace" lo que la función original calculó:

$$x = 2 \rightarrow f(x) = x^{3} + 1 \rightarrow f(2) = (2)^{3} + 1 = 9$$

$$x = 9 \rightarrow f^{- 1}(x) \rightarrow f(9) = 2$$

Representación analítica de la función inversa.
-----------------------------------------------

Para calcular la fórmula de la función inversa seguimos la siguiente
serie de pasos:

1.  En la función original sustituir el símbolo $f(x)$ por la letra
    $y$.[^2]
2.  Despejar la variable $x$.
3.  Cambiar la letra $x$ por el símbolo $f^{- 1}(x)$ y la letra $y$ por
    la letra $x$.

En nuestro ejemplo tendríamos:

No siempre es posible encontrar una representación analítica para una
función inversa. Considere la función $f(x) = x^{x}$, en este caso no es
posible despejar a la variable $x$. Sin embargo, ¡la función inversa si
existe! pero tiene que ser expresada como una gráfica o una enumeración.

Operaciones con funciones.
--------------------------

Es posible combinar funciones a través de diversos procedimientos. En
todos los ejemplos que siguen vamos a asumir $f(x) = x^{2} - 1$ y
$g(x) = 2x + 2$

### Suma de funciones.

### Resta de funciones.

### Multiplicación de funciones.

### División de funciones.

O también:

### Composición de funciones.

O también:

[^1]: Siempre y cuando cada argumento esta determinado.

[^2]: Este paso no es necesario solo nos ayuda a no tener tantos
    símbolos
