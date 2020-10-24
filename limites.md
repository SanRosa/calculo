---
header-includes: \usepackage{tikz}
				 \usepackage{pgfplots}
				 \usepackage{cancel}
				 \pgfplotsset{width=\textwidth,compat=1.9}
---

# Límite

El concepto de límite es un concepto clave porque formaliza la noción intuitiva
de aproximación hacia un punto concreto de una función.

De manera informal decimos que el límite de la función $f(x)$ es $L$ si a
medida que la variable $x$ se aproxima a un valor $a$ la función $f(x)$ se
aproxima a $L$. Esta idea se expresa como:

$$\lim_{x \to a}f(x) = L$$

# Límites laterales

Considera el comportamiento de la función $f(x) = x^{2}$ a medida que $x$
tiende a $2$. Tenemos dos maneras de aproximarnos al número $2$: por la derecha
(números más grandes que 2) y por la izquierda(números más pequeños que 2):

## Límite por la izquierda.

Vamos a aproximarnos al número 2 por la izquierda:

| $x$     | $f(x)$                      |
| ---     | ------                      |
| 1       | $f(1) = 1$                  |
| 1.5     | $f(1.5) = 2.25$             |
| 1.9     | $f(1.9) = 3.61$             |
| 1.99    | $f(1.99) = 3.9601$          |
| 1.999   | $f(1.999) = 3.996001$       |
| 1.9999  | $f(1.9999) = 3.99960001$    |
| 1.99999 | $f(1.99999) = 3.9999600001$ |

Podemos nosotros suponer que la función $f(x) = x^{2}$ tiende a $4$. Expresamos
esta idea como:

$$\lim_{x \to 2^{-}} x^{2} = 4$$ 

## Límite por la derecha.

Vamos a aproximarnos al número 2 por la derecha:

| $x$     | $f(x)$                      |
| ---     | ------                      |
| 3       | $f(3) = 9$                  |
| 2.5     | $f(2.5) = 6.25$             |
| 2.1     | $f(2.1) = 4.41$             |
| 2.01    | $f(2.01) = 4.0401$          |
| 2.001   | $f(2.001) = 4.004001$       |
| 2.0001  | $f(2.0001) = 4.00040001$    |
| 2.00001 | $f(2.00001) = 4.0000400001$ |

Y por lo tanto:

$$\lim_{x \to 2^{+}} x^{2} = 4$$ 

Como los límites por ambos lados tienden a $4$ decimos entonces que:

$$\lim_{x \to 2} x^{2} = 4$$ 

## El límite no existe.

Existen ocasiones en donde una función se aproxima a algún valor específico, es
decir, los limites por la izquierda y por la derecha son diferentes en ese caso
decimos que **el límite no existe.**

Considera la función:

$$f(x) = \frac{1}{x}$$

y estima que pasa con esta función a medida que $x$ se aproxima a cero, es
decir:

$$\lim_{x \to 0} \frac{1}{x}$$

Realizando límites laterales obtenemos

| $x$      | $f(x)$                  |
| ---      | ------                  |
| -1       | $f(-1) = -1$            |
| -0.5     | $f(-0.5) = -2$          |
| -0.1     | $f(-0.1) = -10$         |
| -0.01    | $f(-0.01) = -100$       |
| -0.001   | $f(-0.001) = -1000$     |
| -0.0001  | $f(-0.0001) = -10000$   |
| -0.00001 | $f(-0.00001) = -100000$ |

Podemos concluir que:

$$\lim_{x \to 0^{-}} \frac{1}{x} = -\infty$$

| $x$     | $f(x)$                |
| ---     | ------                |
| 1       | $f(1) = 1$            |
| 0.5     | $f(0.5) = 2$          |
| 0.1     | $f(0.1) = 10$         |
| 0.01    | $f(0.01) = 100$       |
| 0.001   | $f(0.001) = 1000$     |
| 0.0001  | $f(0.0001) = 10000$   |
| 0.00001 | $f(0.00001) = 100000$ |

$$\lim_{x \to 0^{+}} \frac{1}{x} = \infty$$

El límite por la izquierda tiende a $-\infty$ mientras que el límite por la
derecha tiende a $\infty$, como los valores son distintos décimos que el límite
no existe.

# Teoremas para el cálculo de límites.

Los limites laterales son una herramienta limitada para la estimación del valor
del un límite. Considera el límite:

$$\lim_{x \to 4} \frac{x - 4}{x^{2} - x - 12}$$

Realizando el límite por la izquierda:

| $x$     | $f(x)$                   |
| ---     | ------                   |
| 3       | $f(3) = 0.1666666$       |
| 3.5     | $f(3.5) = 0.1538461$     |
| 3.9     | $f(3.9) = 0.1449275$     |
| 3.99    | $f(3.99) = 0.1430615$    |
| 3.999   | $f(3.999) = 0.1428775$   |
| 3.9999  | $f(3.9999) = 0.1428591$  |
| 3.99999 | $f(3.99999) = 0.1428573$ |

El valor del límite no es evidente a partir de la tabulación, sin embargo,
incluso aunque puedas estimar que el valor "tiende" a $\frac{1}{7}$, no podemos
estar seguro de que ese sea el valor exacto del límite.

Un ejemplo con un comportamiento más extraño es:

$$\lim_{x \to 0} \cos\left(\frac{\pi}{x}\right)$$

Se deja como ejercicio al alumno investigar el comportamiento de ese límite.

Por lo tanto, para calcular límites usaremos álgebra.

1.
\begin{align*}
	\lim_{x \to 4} \frac{x - 4}{x^{2} - x - 12} &= \lim_{x \to 4} \frac{x - 4}{(x + 3)(x - 4)} \\
	&= \lim_{x \to 4} \frac{\bcancel{x - 4}}{(x + 3)\bcancel{(x - 4)}} \\
	&= \lim_{x \to 4} \frac{1}{(x + 3)} \\
	&= \frac{1}{(4 + 3)} = \frac{1}{7}
\end{align*}
2.
\begin{align*}
	\lim_{x \to 2} \frac{x^{2} - 4}{x - 2} &= \lim_{x \to 2} \frac{(x+2)(x-2)}{x - 2} \\
	&= \lim_{x \to 2} \frac{(x+2)\bcancel{(x-2)}}{\bcancel{x - 2}} \\
	&= \lim_{x \to 2} x + 2 = 2 + 2 = 4
\end{align*}
3.
\begin{align*}
	\lim_{h \to 0} \frac{(4 + h)^{2} - 16}{h} &= \lim_{h \to 0} \frac{16 + 2h + h^{2} - 16}{h} \\
	&= \lim_{h \to 0} \frac{2h + h^{2}}{h} \\
	&= \lim_{h \to 0} \frac{h(2 + h)}{h} \\
	&= \lim_{h \to 0} \frac{\bcancel{h}(2 + h)}{\bcancel{h}} \\
	&= \lim_{h \to 0} 2 + h  = 2 + 0 = 2
\end{align*}
4.
\begin{align*}
	\lim_{h \to 0} \frac{(3 + h)^{-1} - 3^{-1}}{h} &= \lim_{h \to 0} \frac{\frac{1}{3 + h} - \frac{1}{3}}{h} \\
	&= \lim_{h \to 0} \frac{\frac{3 - (3 + h)}{3(3 + h)}}{h} \\
	&= \lim_{h \to 0} \frac{\frac{-h}{3(3 + h)}}{h} \\
	&= \lim_{h \to 0} \frac{\frac{-h}{3(3 + h)}}{\frac{h}{1}} \\
	&= \lim_{h \to 0} \frac{-h}{h3(3 + h)} \\
	&= \lim_{h \to 0} \frac{-\bcancel{h}}{\bcancel{h}3(3 + h)} \\
	&= \lim_{h \to 0} \frac{-1}{3(3 + h)} = \frac{-1}{3(3 + 0)}  = \frac{-1}{9}\\
\end{align*}
5.
\begin{align*}
	\lim_{t \to 0} \frac{\sqrt{t^{2} + 9} - 3}{t^{2}} &= \lim_{t \to 0} \frac{\sqrt{t^{2} + 9} - 3}{t^{2}} \cdot \frac{\sqrt{t^{2} + 9} + 3}{\sqrt{t^{2} + 9} + 3} \\
	&= \lim_{t \to 0} \frac{\left(\sqrt{t^{2} + 9}\right)^{2} - 3^{2}}{t^{2}(\sqrt{t^{2} + 9} + 3)} \\
	&= \lim_{t \to 0} \frac{t^{2} + \bcancel{9} - \bcancel{9}}{t^{2}(\sqrt{t^{2} + 9} + 3)} \\
	&= \lim_{t \to 0} \frac{t^{2}}{t^{2}(\sqrt{t^{2} + 9} + 3)} \\
	&= \lim_{t \to 0} \frac{\bcancel{t^{2}}}{\bcancel{t^{2}}(\sqrt{t^{2} + 9} + 3)} \\
	&= \lim_{t \to 0} \frac{1}{\sqrt{t^{2} + 9} + 3} = \frac{1}{\sqrt{0^{2} + 9} + 3} = \frac{1}{\sqrt{9} + 3} = \frac{1}{6}
\end{align*}
6.
\begin{align*}
	\lim_{x	\to 16} \frac{4 - \sqrt{x}}{16x - x^{2}} &= \lim_{x \to 16} \frac{4 - \sqrt{x}}{16x - x^{2}} \cdot \frac{4 + \sqrt{x}}{4 + \sqrt{x}} \\
	&= \lim_{x \to 16} \frac{4^{2} - \sqrt{x}^{2}}{(16x - x^{2})(4 + \sqrt{x})} \\
	&= \lim_{x \to 16} \frac{16 - x}{(16x - x^{2})(4 + \sqrt{x})} \\
	&= \lim_{x \to 16} \frac{16 - x}{x(16 - x)(4 + \sqrt{x})} \\
	&= \lim_{x \to 16} \frac{\bcancel{16 - x}}{x\bcancel{(16 - x)}(4 + \sqrt{x})} \\
	&= \lim_{x \to 16} \frac{1}{x(4 + \sqrt{x})} = \frac{1}{16(4 + \sqrt{16})} = \frac{1}{128}
\end{align*}

# Límites con funciones definidas por casos.

Para este caso tenemos que fijarnos en el valor al que tiende $x$ y dependiendo
de este valor tomamos la fórmula correspondiente.

Considera la función:

$$f(x) = \begin{cases}x^{2} - 1, x \leq 2 \\ 4x + 2, x > 2\end{cases}$$

Vamos a determinar:

$$\lim_{x \to 2} f(x)$$

Debido a que $x \to 2$ y que $2$ es exactamente el valor donde nuestra función
se "separa" vamos a dividir el límite en dos partes: el límite por la izquierda
y el límite por la derecha.

Por la izquierda tenemos:

$$\lim_{x \to 2^{-}} f(x) = \lim_{x \to 2^{-}} x^{2} - 1 = 2^{2} - 1 = 3$$

Y por la derecha:

$$\lim_{x \to 2^{+}} f(x) = \lim_{x \to 2^{+}} 4x + 2 = 4(2) + 2 = 10$$

En este caso tenemos que los límites laterales no son iguales y por lo tanto el
límite no existe.

Considera la función:

$$g(x) = \begin{cases}x^{2} + 1, x \leq 0 \\ -x + 1, x > 0\end{cases}$$

Vamos a determinar:

$$\lim_{x \to 0} g(x)$$

Por la izquierda tenemos:

$$\lim_{x \to 0^{-}} g(x) = \lim_{x \to 0^{-}} x^{2} + 1 = 0^{2} + 1 = 1$$

Y por la derecha:

$$\lim_{x \to 0^{+}} g(x) = \lim_{x \to 0^{+}} -x + 1 = -0 + 1 = 1$$

Esta ocasión, como ambos límites van hacia el mismo valor decimos:

$$\lim_{x \to 0} g(x) = 1$$

# Límites infinitos

Tambien es posible encontrar límites de la forma:

$$\lim_{x \to \infty} f(x)$$

En estos casos lo que significa la expresión $x \to \infty$ es que $x$ es un
número muy grande.

Considera:

$$\lim_{x \to \infty} \frac{1}{x}$$

Toma en cuenta que no podemos realizar límites laterales de la misma manera que
un límite regular porque no es posible acercarse a "infinito"($\infty$) por la
derecha, de la misma forma que no es posible acercarse a "infinito
negativo"($-\infty$) por la izquierda.

Debido a que $x \to \infty$ vamos a tomar valores cada vez mas grandes de $x$
empezando de manera arbitraria en algún valor en este caso $x = 1000$.

| $x$      | $f(x)$                    |
| ---      | ------                    |
| 1000     | $f(1000) = 0.001$         |
| 10000    | $f(10000) = 0.0001$       |
| 100000   | $f(100000) = 0.00001$     |
| 1000000  | $f(1000000) = 0.000001$   |
| 10000000 | $f(10000000) = 0.0000001$ |

A medida que incrementamos el valor de $x$ nuestra función tiende a 0, y por lo
tanto:

$$\lim_{x \to \infty} \frac{1}{x} = 0$$

Sin embargo, también es posible que la función "explote", es decir, que el
valor de la función se incrementa demasiado sin álgun patrón en particular.

Considera:

$$\lim_{x \to \infty} x^{2}$$

Si analizamos con límites laterales:

| $x$      | $f(x)$                       |
| ---      | ------                       |
| 1000     | $f(1000) = 1000000$          |
| 10000    | $f(10000) = 10000^{2}$       |
| 100000   | $f(100000) = 100000^{2}$     |
| 1000000  | $f(1000000) = 1000000^{2}$   |
| 10000000 | $f(10000000) = 10000000^{2}$ |

Podemos observar que la función $f(x) = x^{2}$ "explota" o "tiende a infinito"
porque el valor solo incrementa de manera arbitraria y escribimos:

$$\lim_{x \to \infty} x^{2} = \infty$$

Un tipo de función que analizamos con límites infinitos son funciones que tienen la forma:

$$f(x) = \frac{p(x)}{q(x)}$$

Ejemplo. Considera el límite:

$$\lim_{x \to \infty} \frac{x^{2} + x + 1}{2x^{2} - 3x - 4}$$

Para resolver este tipo de límites vamos a seguir los siguientes pasos:

1. Determinar la potencia mas grande del *denominador*, llamemosla $n$.
2. Multiplicar nuestra función por la expresion:$$\frac{\frac{1}{x^{n}}}{\frac{1}{x^{n}}}$$
3. Simplificar las potencias y "sustituir" $x$ por $\infty$.

En nuestro ejemplo la potencia mas grande del denominador es: $n = 2$ y por lo
tanto:

$$\lim_{x \to \infty} \frac{x^{2} + x + 1}{2x^{2} - 3x - 4} \cdot \frac{\frac{1}{x^{2}}}{\frac{1}{x^{2}}}$$

y obtenemos

$$\lim_{x \to \infty} \frac{\frac{x^{2}}{x^{2}} + \frac{x}{x^{2}} + \frac{1}{x^{2}}}{\frac{2x^{2}}{x^{2}} - \frac{3x}{x^{2}} - \frac{4}{x^{2}}}$$

simplificando:

$$\lim_{x \to \infty} \frac{\bcancel{\frac{x^{2}}{x^{2}}} + \frac{\bcancel{x}}{x^{\bcancel{2}}} + \frac{1}{x^{2}}}{\frac{2\bcancel{x^{2}}}{\bcancel{x^{2}}} - \frac{3\bcancel{x}}{x^{\bcancel{2}}} - \frac{4}{x^{2}}}$$

$$\lim_{x \to \infty} \frac{1 + \frac{1}{x} + \frac{1}{x^{2}}}{2 - \frac{3}{x} - \frac{4}{x^{2}}}$$

y por último "sustitumos" $\infty$

$$\lim_{x \to \infty} \frac{1 + \cancelto{0}{\frac{1}{x}} + \cancelto{0}{\frac{1}{x^{2}}}}{2 - \cancelto{0}{\frac{3}{x}} - \cancelto{0}{\frac{4}{x^{2}}}} = \frac{1}{2}$$


