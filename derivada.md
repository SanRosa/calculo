---
header-includes: \usepackage{tikz}
				 \usepackage{pgfplots}
				 \pgfplotsset{width=\textwidth,compat=1.9}
---

# La derivada.

El concepto de derivada responde al siguiente problema: Considera una función
$f(x)$ y algún punto $x = x_{0}$. Determina la ecuación de la recta tangente
que pasa por el punto $(x_{0},f(x_{0}))$.

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

Sin embargo, resolver este problema parece muy complicado en principio, pues
solo conocemos *un* punto que pasa por la recta tangente $(x_{0}, f(x_{0}))$.
Para encontrar la pendiente utilizamos el siguiente método: 

1. Ubica algún otro punto que este sobre la función $f(x)$ llamémoslo $(b, f(b))$. Si conectas los dos puntos en cuestión obtenemos una recta secante.
2. La pendiente de esta recta tangente es: $$m = \frac{f(b) - f(x_{0})}{b - x_{0}}$$
3. Aproxima el punto $(b, f(b))$ hacia el punto $(x_{0}, f(x_{0}))$. Matemáticamente esto es: $$\lim_{b \to x_{0}} \frac{f(b) - f(x_{0})}{b - x_{0}}$$
4. Esta última expresión se conoce como **derivada por definición**.

Existe una formulación alterna que es más fácil de manipular:

1. Ubica algún otro punto que este sobre la función $f(x)$ llamémoslo $$(x_{0} + h, f(x_{0} + h))$$, donde $h$ es la distancia entre las coordenadas $x$ de nuestros puntos. 
2. La pendiente de esta recta tangente es: $$m = \frac{f(x_{0} + h) - f(x_{0})}{x_{0} + h - x_{0}} = \frac{f(x_{0} + h) - f(x_{0})}{h}$$
3. Aproxima el punto $(x_{0} + h, f(x_{0} + h))$ hacia el punto $(x_{0}, f(x_{0}))$. Matemáticamente esto es: $$\lim_{h \to 0} \frac{f(x_{0} + h) - f(x_{0})}{h}$$

Ejemplo: Calcula la recta tangente a la curva $f(x) = x^{2}$ en el punto $x =
3$. Evidentemente, conocemos las coordenadas del punto por donde pasa la
recta:
$$(3, f(3)) = (3, 9)$$
solo nos falta conocer el valor de la pendiente. Este valor $m$ se calcula:

\begin{align*}
	\lim_{h \to 0} \frac{f(3 + h) - f(3)}{h} &= \lim_{h \to 0} \frac{(3 + h)^{2} - 9}{h} \\
										     &= \lim_{h \to 0} \frac{9 + 6h + h^{2} - 9}{h} \\
										     &= \lim_{h \to 0} \frac{6h + h^{2}}{h} \\
										     &= \lim_{h \to 0} \frac{h(6 + h)}{h} \\
										     &= \lim_{h \to 0} 6 + h = 6 \\
\end{align*}

ya que conocemos el valor de un punto y la pendiente, sustituimos en la fórmula:
$$y - y_{1} = m(x - x_{1})$$
$$y - 9 = 6(x - 3)$$

Repitamos este ejercicio pero ahora en el punto $x = -2$. La coordenada por
donde pasa la tangente es:
$$(-2, f(-2)) = (-2, 4)$$
y la pendiente:

\begin{align*}
	\lim_{h \to 0} \frac{f(2 + h) - f(2)}{h} &= \lim_{h \to 0} \frac{(-2 + h)^{2} - 4}{h} \\
										     &= \lim_{h \to 0} \frac{4 - 4h + h^{2} - 4}{h} \\
										     &= \lim_{h \to 0} \frac{-4h + h^{2}}{h} \\
										     &= \lim_{h \to 0} \frac{h(-4 + h)}{h} \\
										     &= \lim_{h \to 0} -4 + h = -4 \\
\end{align*}

y por lo tanto, la ecuación de la recta tangente es:
$$y - 4 = -4(x + 2)$$

Sin embargo, como seguro habras notado, la manera de obtener la pendiente de
ambas rectas es practicamente igual, si te pidiera ahora que encontraras la
pendiente usando la misma función pero en algun otro valor digamos $x = 1$
tendriamos que realizar la misma series de pasos otra vez. Un mejor sistema es
calcular la pendiente de la recta tangente pero de manera general, osea,
dejando el punto $x_{0}$ como un punto cualquiera y realizar el límite.

\begin{align*}
	\lim_{h \to 0} \frac{f(x_{0} + h) - f(x_{0})}{h} &= \lim_{h \to 0} \frac{(x_{0} + h)^{2} - x_{0}^{2}}{h} \\
										     &= \lim_{h \to 0} \frac{x_{0}^{2} + 2x_{0}h + h^{2} - x_{0}^{2}}{h} \\
										     &= \lim_{h \to 0} \frac{2x_{0}h + h^{2}}{h} \\
										     &= \lim_{h \to 0} \frac{h(2x_{0} + h)}{h} \\
										     &= \lim_{h \to 0} 2x_{0} + h = 2x_{0} \\
\end{align*}

Por lo tanto, la expresión $2x_{0}$ nos dice el valor de la pendiente en
cualquier punto $x_{0}$ que elijamos. Por ejemplo, si $x_{0} = 3$ al sustituir
en esta expresión obtenemos: $2(3) = 6$, si $x_{0} = -2$ al sustituir
obtenemos: $2(-2) = -4$. Regularmente, estas expresiones las escribimos sin el
subindice, es decir, solamente vamos a escribir $x$: $2x_{0} \to 2x$. Esta
expresión $2x$ se conoce como: *función derivada* o simplemente *derivada*. 

## Notación

La derivada de una función $f(x)$ se puede escribir como:
$$f'(x), \frac{df(x)}{dx}, D_{x}\left(f(x)\right)$$

## Notación de Leibniz

La notación de Leibniz es usada en todas las ramas de las matemáticas que
involucran al cálculo:
$$\frac{df(x)}{dx}$$
También es común encontrar esta notación como:
$$\frac{d}{dx}f(x), \frac{d}{dx}\big(f(x)\big)$$

Recuerda que es $f(x) = y$ y es posible encontrar la notación de Leibniz como:
$$\frac{dy}{dx}$$
o también
$$\frac{d}{dx}y, \frac{d}{dx}\big(y)$$

La notación $f'(x)$ se le conoce como notación de *Lagrange*, y es posible
encontrar $y'$.A la notación $D_{x}(f(x))$ se le conoce como notación de
*Euler*, y es posible encontrar $D_{x}(y)$.

Existe otra notación $\dot{y}$, conocida cono notación de *Newton*, pero es mas
común encontrar esta notación en libros de física.

A manera de ejemplo considera la función $f(x) = x^{2}$ y su derivada $2x$.
Usando las diferentes notaciones:

1. Leibniz: $$\frac{df(x)}{dx} = 2x$$
2. Lagrange: $$f'(x) = 2x$$
3. Euler: $$D_{x}(f(x)) = 2x$$

También es común encontrar las diferentes notaciones aplicadas directamente
sobre la fórmula de una función, es decir:

1. Leibniz: $$\frac{d(x^{2})}{dx} = 2x$$
2. Lagrange: $$(x^{2})' = 2x$$
3. Euler: $$D_{x}(x^{2}) = 2x$$

## Derivadas por definición.

Ejemplo. Calcula la derivada de la función $f(x) = x^{3}$. Usamos la fórmula de
derivada por definición:

\begin{align*}
	\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} &= \lim_{h \to 0} \frac{(x + h)^{3} - x^{3}}{h} \\
											 &= \lim_{h \to 0} \frac{x^{3} + 3x^{2}h + 3xh^{2}+ h^{3} - x^{3}}{h} \\
											 &= \lim_{h \to 0} \frac{3x^{2}h + 3xh^{2}+ h^{3}}{h} \\
											 &= \lim_{h \to 0} \frac{h(3x^{2} + 3xh+ h^{2})}{h} \\
											 &= \lim_{h \to 0} 3x^{2} + 3xh+ h^{2} = 3x^{2} \\
\end{align*}

Ejemplo: Calcula la derivada de la función $f(x) = \frac{1}{x}$

\begin{align*}
	\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} &= \lim_{h \to 0} \frac{\frac{1}{x + h} - \frac{1}{x}}{h} \\
											 &= \lim_{h \to 0} \frac{\frac{x - (x + h)}{x(x + h)}}{h} \\
											 &= \lim_{h \to 0} \frac{\frac{x - x - h}{x(x + h)}}{h} \\
											 &= \lim_{h \to 0} \frac{\frac{-h}{x(x + h)}}{h} \\
											 &= \lim_{h \to 0} \frac{\frac{-h}{x(x + h)}}{\frac{h}{1}} \\
											 &= \lim_{h \to 0} \frac{-h}{hx(x + h)} \\
											 &= \lim_{h \to 0} \frac{-1}{x(x + h)} = \frac{-1}{x(x + 0)} = \frac{-1}{x^{2}} \\
\end{align*}

Ejemplo: Calcula la derivada de la función $f(x) = \sqrt{x}$

\begin{align*}
	\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} &= \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h} \\
											 &= \lim_{h \to 0} \frac{\sqrt{x + h} - \sqrt{x}}{h} \cdot \frac{\sqrt{x + h} + \sqrt{x}}{\sqrt{x + h} + \sqrt{x}} \\
											 &= \lim_{h \to 0} \frac{(\sqrt{x + h})^{2} - (\sqrt{x})^{2}}{h(\sqrt{x + h} + \sqrt{x})} \\
											 &= \lim_{h \to 0} \frac{x + h - x}{h(\sqrt{x + h} + \sqrt{x})} \\
											 &= \lim_{h \to 0} \frac{h}{h(\sqrt{x + h} + \sqrt{x})} \\
											 &= \lim_{h \to 0} \frac{1}{(\sqrt{x + h} + \sqrt{x})} = \frac{1}{\sqrt{x} + \sqrt{x}} = \frac{1}{2\sqrt{x}} \\
\end{align*}

Ejemplo: Calcula la derivada de la función $f(x) = 3x^{2} + 2x + 1$

\begin{align*}
	\lim_{h \to 0} \frac{f(x + h) - f(x)}{h} &= \lim_{h \to 0} \frac{3(x + h)^{2} + 2(x + h) + 1 - (3x^{2} + 2x + 1)}{h} \\
											 &= \lim_{h \to 0} \frac{3(x^{2} + 2xh + h^{2}) + 2(x + h) + 1 - (3x^{2} + 2x + 1)}{h} \\
											 &= \lim_{h \to 0} \frac{3x^{2} + 6xh + 3h^{2} + 2x + 2h + 1 - 3x^{2} - 2x - 1}{h} \\
											 &= \lim_{h \to 0} \frac{6xh + 3h^{2} + 2h}{h} \\
											 &= \lim_{h \to 0} \frac{h(6x + 3h + 2)}{h} \\
											 &= \lim_{h \to 0} 6x + 3h + 2 = 6x + 3(0) + 2 = 6x + 2
\end{align*}

# La regla de las potencias.

Si derivas funciones que sean potencias de $x$ obtienes el siguiente patrón:

| Función | Derivada |
| ------- | -------- |
| $x$     | $1$      |
| $x^{2}$ | $2x$     |
| $x^{3}$ | $3x^{2}$ |
| $x^{4}$ | $4x^{3}$ |
| $x^{5}$ | $5x^{4}$ |

A partir de esta tabla podemos formar una conjetura: *La derivada de $f(x) =
x^{n}$ es $f'(x) = nx^{n - 1}$*. La cuestión aqui es como demostrar que esto es
un hecho. ¿Como podemos estar seguros de que no existe un número $n$ tal que la
derivada de $f(x) = x^{n}$ no sea $f'(x) = nx^{n - 1}$?

Demostración:




