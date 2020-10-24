---
header-includes: \usepackage{tikz}
				 \usepackage{pgfplots}
				 \pgfplotsset{width=\textwidth,compat=1.9}
---

# Definición formal de una función.

\noindent\fbox{\parbox{\textwidth}{\textbf{Definición (Función): }Dados dos
conjuntos $A$ y $B$, una función (también aplicación o mapeo) entre ellos es
una asociación $f$ que a cada elemento de $A$ le asigna un \textit{único}
elemento de $B$. Se dice entonces que $A$ es el \textbf{dominio} (también
conjunto de partida o conjunto inicial) de $f$ y que $B$ es su \textbf{rango}
(también conjunto de llegada o conjunto final).}}

### Dominio.

A el conjunto de posibles argumentos de una función se le conoce como
**dominio**, utilizando la analogía de la máquina podemos pensar al dominio
como todos los posibles "inputs" que la máquina puede recibir. Es posible
restringir el dominio de una función, solamente hay que escribir dentro de la
definición de nuestra función el dominio que queramos asignarle.

Por ejemplo: Sea la función $f(x) = 2x; x \geq 0$, esto quiere decir que el
dominio esta restringido a los números que sean iguales o mayores que cero, asi
por ejemplo, podemos obtener los valores de $f(1) = 2$, $f(3) = 6$ o $f(0.45) =
0.9$, sin embargo, para los valores que sean menores que cero la función se
considera *indefinida*.

Si no se indica explícitamente el dominio de la función, entonces se asume que
el dominio son todos los números reales $\mathbb{R}$, esto se conoce como
*dominio implícito*.^[Siempre y cuando cada argumento esta determinado.] Por lo
tanto, podemos asumir que la función $g(x)=3x$ esta definida para todos los
números reales, mientras que la función $h(x)=3x, x > 5$ solo esta definida
para los números que sean mayores que $5$.  Nota que aunque las funciones
$g(x)$ y $h(x)$ tienen la misma fórmula **NO** son iguales. Dos funciones son
iguales si y solo si comparten el mismo dominio, el mismo rango y la misma
correspondencia entre elementos.

Sin embargo, aunque una función tenga dominio implícito, este puede que no sean
todos lo números reales $\mathbb{R}$, esto debido a ciertos particularidades de
las matemáticas. Por ejemplo, la función:

$$f(x) = \frac{x^{2} - 4}{x - 2}$$

no esta definida en $x = 2$, debido a que:

$$f(2) = \frac{(2)^{2} - 4}{2 - 2} = \frac{0}{0}$$

y por lo tanto su dominio son todos los números reales **excepto** 2. Esto es
expresado como $\text{Dom}_{f_{}}= (-\infty, 2) \cup (2, \infty)$.

Considera la función:

$$g(x) = \frac{1}{x(x - 1)}$$

esta función tiene dos valores donde esta indefinida: $x = 0$ y $x = 1$

$$g(0) = \frac{1}{0(0 - 1)} = \frac{1}{0}$$
$$g(1) = \frac{1}{1(1 - 1)} = \frac{1}{0}$$

y por lo tanto su dominio son todos lo números reales **excepto** 0 y 1. Esto
se expresa como: $\text{Dom}_{g_{}} = (-\infty, 0) \cup (0, 1) \cup (1,
\infty)$.



