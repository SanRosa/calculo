---
header-includes: \usepackage{tikz}
				 \usepackage{pgfplots}
				 \pgfplotsset{width=\textwidth,compat=1.9}
---

# Función.

El concepto de función surge cuando dos variables están relacionadas, de tal
manera que una de las variables determina el valor de la otra variable.

Ejemplos:

1. Física. Tiempo de caída, $t$ representa tiempo y $h$ representa altura:
$$ t = \sqrt{\frac{2 \cdot h}{9.81}}$$
2. Economía / Finanzas. Tipo de cambio. $m$ representa *MXN* (Peso Mexicano) y $d$ representa *USD* (Dólar Americano).^[Este es el tipo de cambio redondeado al tiempo que se escribe este árticulo.]
$$ d = \frac{m}{21} $$
3. Geometría. Área del círculo, $A$ representa el área y $r$ representa el radio del círculo:
$$ A = \pi \cdot r^{2} $$

Estas tres relaciones son ejemplos de funciones, si en *Tiempo de caída*
sustituimos un valor $h$ por algún número en especifico por ejemplo $h = 20$
entonces obtenemos:
$$ t = \sqrt{\frac{2 \cdot 20}{9.81}} = 2.019275\dots \approx 2.02 $$

O también, si en *Tipo de cambio* sustituimos $m = 105$ obtenemos:
$$ d = \frac{105}{21} = 5 $$

En ambos ejemplos, el valor de unas de las variables **determina** el valor de
la otra variable. En el ejemplo de economía si $m = 105$ entonces $d = 5$, en
el ejemplo de física si $h = 20$ entonces $t = 2.019275\dots$

En las funciones tenemos dos tipos de variables: **independientes** y
**dependientes**. Las variables **dependientes** reciben ese nombre porque
*dependen* del valor de la otra variable, como regla general las podemos
identificar porque siempre están despejadas. Las **independientes** tienen la
característica que nosotros podemos elegir libremente su valor. Puedo sustituir
$r = 1$, $r = 6.5$, $r = 10.1$ o cualquier valor que yo quiera en la función de
*Área del círculo*.

En nuestro ejemplos tenemos:

| Función          | Variable Independiente | Variable Dependiente |
| ---              | ---                    | ---                  |
| Tiempo de caída  | $h$: Altura            | $t$: Tiempo          |
| Tipo de cambio   | $m$: Peso Mexicano     | $d$: Dólar Americano |
| Área del círculo | $r$: Radio             | $A$: Área            |

## Notación $f(x)$

Para simplificar el uso de variables, en cálculo denotamos a las variables
independientes con la letra $x$ y las variables dependientes con la letra $y$.
Así, si expresamos nuestros ejemplos de la sección anterior tendríamos:

\begin{align*}
	t = \sqrt{\frac{2h}{9.81}} &\to y = \sqrt{\frac{2x}{9.81}} \\
	d = \frac{m}{21} &\to y = \frac{x}{21} \\
	A = \pi \cdot r^{2} &\to y = \pi \cdot x^{2} \\
\end{align*}

La notación que involucra a las variables $x$ y $y$ es común en cálculo, sin
embargo, existe otra notación donde a la variable dependiente $y$ la
sustituimos por el símbolo $f(x)$. Esta notación
nos permite escribir a la funciones de la siguiente manera:

\begin{align*}
	y = \sqrt{\frac{2x}{9.81}} &\to f(x) = \sqrt{\frac{2x}{9.81}} \\
	y = \frac{x}{21} &\to f(x) = \frac{x}{21} \\
	y = \pi \cdot x^{2} &\to f(x) = \pi \cdot x^{2} \\
\end{align*}

La letra $f$ que sirve para identificar una función se le conoce como *nombre
de la función*, claramente se puede nombrar una función como uno quiera, puedo
cambiar $f(x) = x^{2}$ por $g(x) = x^{2}$ y representan la misma función. Así
podemos entonces nombrar nuestra funciones como:

\begin{align*}
	f(x) = \sqrt{\frac{2x}{9.81}} &\to f(x) = \sqrt{\frac{2x}{9.81}} \\
	f(x) = \frac{x}{21} &\to g(x) = \frac{x}{21} \\
	f(x) = \pi \cdot x^{2} &\to h(x) = \pi \cdot x^{2} \\
\end{align*}

## Analogía de la máquina.

\begin{center}
	\begin{tikzpicture}

		\node[] (0) at (-2, 2) {};
		\node[] (1) at (-2, -1) {};
		\node[] (2) at (1, -1) {};
		\node[] (3) at (1, -2) {};
		\node[] (4) at (2, -2) {};
		\node[] (5) at (2, 1) {};
		\node[] (6) at (-1, 1) {};
		\node[] (7) at (-1, 2) {};
		\node[] (8) at (-1.5, 2.25) {};
		\node[] (9) at (-1.5, 3) {\huge $3$};
		\node[] (10) at (1.5, -2) {};
		\node[] (15) at (2.25, -2.5) {\huge $9$};
		\node[] (17) at (0, 0) {\huge $f(x)=x^{2}$};

		\draw (0.center) to (1.center);
		\draw (1.center) to (2.center);
		\draw (2.center) to (3.center);
		\draw (3.center) to (4.center);
		\draw (4.center) to (5.center);
		\draw (5.center) to (6.center);
		\draw (6.center) to (7.center);
		\draw (7.center) to (0.center);
		\draw[->, line width = 0.25mm] (9.south) to (8.center);
		\draw[->, line width = 0.25mm] [in=-180, out=-90] (10.south) to (15.west);

	\end{tikzpicture}
\end{center}

Una manera muy útil de representar funciones, es a través de una "máquina".
Nosotros le introducimos valores a esta "máquina", esta hace cálculos y nos
regresa un valor. En el diagrama de arriba tenemos representado este proceso:
Nuestra máquina es la función $f(x) = x^{2}$, le introducimos el número $3$ y
la máquina no devuelve el valor $9$.

A el número que le introducimos a esta máquina se le conocen como *argumento*,
*entrada* o *input*. Después la máquina "evalúa"^[Claramente nosotros somos los
que tenemos que hacer los cálculos a mano, la máquina es solo una analogia.] el
argumento y nos regresa un valor que se le conoce como *valor de retorno*,
*salida* o *output*.

En nuestro diagrama en particular: $3$ es el argumento, la función evalúa $f(3)
= 3^{2}$ y el valor de retorno es $9$.

## Representación de una función.

Tenemos tres maneras de representar una función, cada una de estas maneras
tiene ventajas y desventajas:

- Fórmula - Representación analítica.
- Gráfica.
- Enumeración.

Una fórmula es la representación mas común en esta materia, ya hemos visto
muchos ejemplos de fórmulas: $f(x) = x^{2}$, $f(x) = \frac{x}{21}$, etc. La
gráfica consiste en una colección de puntos en el plano cartesiano, en la
próxima sección veremos como podemos graficar funciones. Y por última una
enumeración consiste en describir a través de una lista o tabla a que argumento
le corresponde que valor de retorno.

\begin{center}
	\begin{tikzpicture}
		\node (2) at (-2.5, -2) {};
		\node (3) at (-3, -1.5) {};
		\node (6) at (-0.25, 2.5) {};
		\node (7) at (0.25, 2.5) {};
		\node (8) at (2.5, -2) {};
		\node (9) at (3, -1.5) {};
		\node (10) at (0, 3) {Fórmula};
		\node (11) at (-3, -1.75) {Gráfica};
		\node (12) at (3, -1.75) {Enumeración};

		\draw [->,bend right, looseness=1.25, line width=0.50mm] (6.center) to (3.center);
		\draw [<->,bend right, line width=0.50mm] (2.center) to (8.center);
		\draw [<-,bend right, line width=0.50mm] (9.center) to (7.center);
	\end{tikzpicture}
\end{center}

La representación analítica es la que preferimos porque es posible convertirla
en gráfica y en enumeración, mientras que las otras dos no tienen esta
característica: la gráfica la podemos convertir en una enumeración pero no
necesariamente la podemos convertir en fórmula y la enumeración la podemos
convertir en gráfica pero no necesariamente en fórmula.

## Gráfica de una función.(Tabulación)

El proceso para graficar una función dada una fórmula $f(x)$ es el siguiente:

1. Escoge un rango de valores para $x$. Por ejemplo: -3, -2, -1, 0, 1, 2 y 3.
2. Evalúa cada uno de los valores en la función $f(x)$. Hazlo en una tabla para mantener orden.
3. Cada uno de los valores obtenidos forman una coordenada $(x, f(x))$. Ubicalos en el plano.

Por ejemplo, vamos a conseguir la gráfica de al función $f(x) = x^{3}$ desde $-3$ hasta $3$.

| $x$  | $f(x) = x^{3}$           | $\big(x, f(x)\big)$ |
| ---  | --------------           | -----------         |
| $-3$ | $f(-3) = (-3)^{3} = -27$ | $(-3, -27)$         |
| $-2$ | $f(-2) = (-2)^{3} = -8$  | $(-2, -8)$          |
| $-1$ | $f(-1) = (-1)^{3} = -1$  | $(-1, -1)$          |
| $0$  | $f(0) = (0)^{3} = 0$     | $(0, 0)$            |
| $1$  | $f(1) = (1)^{3} = 1$     | $(1, 1)$            |
| $2$  | $f(2) = (2)^{3} = 8$     | $(2, 8)$            |
| $3$  | $f(3) = (3)^{3} = 27$    | $(3, 27)$           |

\begin{center}
	\begin{tikzpicture}
		\begin{axis}[
			xmin=-10,xmax=10,
			ymin=-30,ymax=30,
			grid=both,
			axis lines=middle,
			grid style={line width=.1pt, draw=gray!10},
			xlabel = $x$,
			ylabel = {$f(x)$},
			minor tick num=5,
			axis line style={latex-latex},
		]
		\addplot [
			only marks,
		]
		coordinates {(-3, -27)(-2, -8)(-1, -1)(0, 0)(1, 1)(2, 8)(3, 27)};
		\end{axis}
	\end{tikzpicture}
\end{center}

## Detalles técnicos de graficación.

Considera la función $f(x) = \frac{1}{x}$, vamos a realizar *tres* gráficas de
la misma función:

1. De $-5$ a $5$ pasando por: $-5, -3, -1, 1, 3, 5$ (2 unidades entre cada valor)
2. De $-5$ a $5$ pasando por: $-5, -4, -3, \dots , 3, 4, 5$ (1 unidad entre cada valor)
3. De $-5$ a $5$ pasando por: $-5, -4.9, -4.8, \dots , 4.8, 4.9, 5$ (0.1 unidades entre cada valor)

## Primer gráfica.

| $x$  | $f(x) = \frac{1}{x}$            | $\big(x, f(x)\big)$ |
| ---  | --------------                  | -----------         |
| $-5$ | $f(-5) = \frac{1}{-5} = -0.2$   | $(-5, -0.2)$        |
|      |                                 |                     |
| $-3$ | $f(-3) = \frac{1}{-3} = -0.333$ | $(-3, -0.333)$      |
|      |                                 |                     |
| $-1$ | $f(-1) = \frac{1}{-1} = -1$     | $(-1, -1)$          |
|      |                                 |                     |
| $1$  | $f(1) = \frac{1}{1} = 1$        | $(1, 1)$            |
|      |                                 |                     |
| $3$  | $f(3) = \frac{1}{3} = 0.333$    | $(3, 0.333)$        |
|      |                                 |                     |
| $5$  | $f(5) = \frac{1}{5} = 0.2$      | $(5, 0.2)$          |

\begin{center}
	\begin{tikzpicture}
		\begin{axis}[
			xmin=-6,xmax=6,
			ymin=-10,ymax=10,
			grid=both,
			axis lines=middle,
			grid style={line width=.1pt, draw=gray!10},
			xlabel = $x$,
			ylabel = {$f(x)$},
			minor tick num=1,
			axis line style={latex-latex},
		]
		\addplot [
			only marks,
		]
		coordinates { (-5, -0.2)(-3, -0.333)(-1, -1)(1, 1)(3, 0.333)(5, 0.2)};
		\end{axis}
	\end{tikzpicture}
\end{center}

## Segunda gráfica.

| $x$  | $f(x) = \frac{1}{x}$                | $\big(x, f(x)\big)$ |
| ---  | --------------                      | -----------         |
| $-5$ | $f(-5) = \frac{1}{-5} = -0.2$       | $(-5, -0.2)$        |
|      |                                     |                     |
| $-4$ | $f(-4) = \frac{1}{-4} = -0.25$      | $(-4, -0.25)$       |
|      |                                     |                     |
| $-3$ | $f(-3) = \frac{1}{-3} = -0.333$     | $(-3, -0.333)$      |
|      |                                     |                     |
| $-2$ | $f(-2) = \frac{1}{-2} = -0.5$       | $(-2, -0.5)$        |
|      |                                     |                     |
| $-1$ | $f(-1) = \frac{1}{-1} = -1$         | $(-1, -1)$          |
|      |                                     |                     |
| $0$  | $f(0) = \frac{1}{0} (\text{indef})$ | $(0, -)$            |
|      |                                     |                     |
| $1$  | $f(1) = \frac{1}{1} = 1$&nbsp;      | $(1, 1)$            |
|      |                                     |                     |
| $2$  | $f(2) = \frac{1}{2} = 0.2$          | $(2, 0.2)$          |
|      |                                     |                     |
| $3$  | $f(3) = \frac{1}{3} = 0.333$        | $(3, 0.333)$        |
|      |                                     |                     |
| $4$  | $f(4) = \frac{1}{4} = 0.25$         | $(4, 0.25)$         |
|      |                                     |                     |
| $5$  | $f(5) = \frac{1}{5} = 0.2$          | $(5, 0.2)$          |


\begin{center}
	\begin{tikzpicture}
		\begin{axis}[
			xmin=-6,xmax=6,
			ymin=-10,ymax=10,
			grid=both,
			axis lines=middle,
			grid style={line width=.1pt, draw=gray!10},
			xlabel = $x$,
			ylabel = {$f(x)$},
			minor tick num=1,
			axis line style={latex-latex},
		]
		\addplot [
			only marks,
		]
		coordinates {(-5, -0.2)(-4, -0.25)(-3, -0.333)(-2, -0.5)(-1, -1)(1, 1)(2, 0.5)(3, 0.333)(4, 0.25)(5, 0.2)};
		\end{axis}
	\end{tikzpicture}
\end{center}

## Tercer gráfica.

\begin{center}
	\begin{tikzpicture}
		\begin{axis}[
			xmin=-6,xmax=6,
			ymin=-10,ymax=10,
			grid=both,
			axis lines=middle,
			grid style={line width=.1pt, draw=gray!10},
			xlabel = $x$,
			ylabel = {$f(x)$},
			minor tick num=1,
			axis line style={latex-latex},
		]
		\addplot [
			domain=-5:5,
			samples=100,
		]
		{1 / x};
		\addplot [
			only marks,
		]
		coordinates {(-5, -0.2)(-4, -0.25)(-3, -0.333)(-2, -0.5)(-1, -1)(1, 1)(2, 0.5)(3, 0.333)(4, 0.25)(5, 0.2)};
		\end{axis}
	\end{tikzpicture}
\end{center}

La forma de la gráfica de una función no siempre es evidente, la mejor
estrategia es usar el mayor número de puntos para obtener la mejor resolución
posible.
