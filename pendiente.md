---
header-includes: \usepackage{tikz}
				 \usepackage{pgfplots}
				 \pgfplotsset{width=\textwidth,compat=1.9}
---

# La linea recta y su pendiente.

Una ecuación que tiene la forma:
$$ax + by + x = 0$$
representa una línea recta, en el sentido que, las soluciones de esta ecuación
al ser puestas como puntos $(x, y)$ en el plano forman visualmente una recta.

Considera la ecuación: $2x + 3y - 12 = 0$. La gráfica de las soluciones de esta
ecuación forman la siguiente gráfica:

\begin{center}
	\begin{tikzpicture}
		\begin{axis}[
			xmin=-6,xmax=6,
			ymin=-6,ymax=6,
			grid=both,
			axis lines=middle,
			grid style={line width=.1pt, draw=gray!10},
			xlabel = $x$,
			ylabel = {$f(x)$},
			minor tick num=1,
			axis line style={latex-latex},
		]
		\addplot [
			domain=-6:6,
			samples=10,
		]
		{4 - (2/3)*x};
		\end{axis}
	\end{tikzpicture}
\end{center}

Nota que esta recta pasa por puntos como: $(6, 0)$, $(3, 3)$, $(0, 4)$, y que
estos puntos son soluciones de la ecuación de la recta.

Para graficar una recta dada su ecuación seguimos el siguiente procedimiento:

1. Encontrar **2** soluciones de la ecuación.
2. Graficar las soluciones como puntos en el plano.
3. Unir esos puntos con una línea recta que se extiende indefinidamente.

Una cantidad que es de mucho interés en cálculo diferencial es la *pendiente*
de una recta. La pendiente de una recta indica que tan "inclinada" es una
recta. Para calcular la pendiente de una recta tenemos la fórmula:
$$m = \frac{y_{2} - y_{1}}{x_{2} - x_{1}}$$
donde $(x_{1}, y_{1})$ y $(x_{2}, y_{2})$ son soluciones de la ecuación.

En nuestra recta $2x + 3y - 12 = 0$, consideremos las soluciones: $(3, 3)$ y
$(6, 0)$ y al sustituirlos en la fórmula obtenemos:
$$m = \frac{3 - 0}{3 - 6} = -\frac{2}{3}$$

La *forma ordenada al origen* ofrece otra forma de determinar la pendiente de
una recta. La *forma ordenada la origen* de una recta es una ecuación que tiene
la siguiente esctructura:
$$y = mx + b$$
donde $m$ y $b$ son números que representn la pendiente de la recta y al
intersección con el eje $y$ respectivasmente

Para obtener la forma ordenada al origen solo requerimos despejar $y$. Vamos a
obtener la forma ordenada al origen de nuestra ecuación: $2x + 3y - 12 = 0$

\begin{align*}
	2x + 3y - 12 &= 0 \\
	2x + 3y &= 12 \\
	3y &= 12 - 2x \\
	y &= \frac{12 - 2x}{3} \\
	y &= \frac{12}{3} - \frac{2x}{3} \\
	y &= 4 - \frac{2x}{3} \\
	y &= - \frac{2x}{3} + 4\\
\end{align*}

Podemos observar que $m = -\frac{2}{3}$.

Para obtener la ecuación de una recta tenemos dos opciones:

1. Conocer 2 puntos que pertenezcan a la recta.
2. Conocer 1 punto y la pendiente de la recta.

Si conoces 1 punto y la pendiente de la recta usamos la fórmula:
$$y - y_{1} = m(x - x_{1})$$
donde $m$ es el valor de la pendiente y $(x_{1}, y_{1})$ es el punto que
pertenece a la recta. Si conoces dos puntos que pasan sobre la recta utiliza la
fórmula:
$$m = \frac{y_{2} - y_{1}}{x_{2} - x_{1}}$$
para obtener el valor de la pendiente y sigue el mismo procedimiento que el
caso pasado.

Por ejemplo, considera los puntos $(2, 1)$ y $(5, 5)$ y obtén la ecuación de la
recta que pasa por ellos. Utilizamos la fórmula para obtener la pendiente:
$$m = \frac{5 - 1}{5 - 2} = \frac{4}{3}$$
y sustituimos la pendiente y alguno de los dos puntos en nuestra fórmula:
$$y - 1 = \frac{4}{3}(x - 2)$$
