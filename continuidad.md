---
header-includes: |
  ```{=tex}
  \usepackage{tikz} \usepackage{pgfplots}
  ```
  `\pgfplotsset{width=\textwidth,compat=1.9}`{=tex}
---

Continuidad
===========

Informalmente podemos decir que una función es continua si en principio
podemos trazar su gráfica sin tener que despegar el lápiz o bolígrafo
del papel. La función $f(x) = x^{2}$ es continua

```{=tex}
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
        {x^2};
        \end{axis}
    \end{tikzpicture}
\end{center}
```

Mientras que la función $f(x) = \frac{1}{x}$ no es continua, debido a
que cuando $x$ es cero la función no está definida y tendríamos que
dejar de trazar la función en ese punto para continuar más adelante.

```{=tex}
\begin{center}
    \begin{tikzpicture}
        \begin{axis}[
            xmin=-6,xmax=6, ymin=-10,ymax=10,
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
        \end{axis}
    \end{tikzpicture}
\end{center}
```
De manera formal, una función es continua en algún punto $x = x_{0}$ si
se cumplen tres condiciones:

1.  El límite de la función cuando $x$ tiende a $x_{0}$ existe.
2.  La función está definida en $x = x_{0}$, es decir $f(x_{0})$ es
    algún número real.
3.  El límite de la función cuando $x$ tiende a $x_{0}$ es igual al
    valor de $f(x_{0})$

Las tres condiciones pueden resumirse en:
$$\lim_{x \to x_{0}} f(x) = f(x_{0})$$

Nota que, usando estas condiciones solamente puedes verificar si la
función es continua en un punto. Si una función es discontinua en un
punto entonces alguna de las tres condiciones no se cumple. Por ejemplo,
la función $f(x) = \frac{1}{x}$ es discontinua en $x = 0$, debido a que
no cumple la condición 2, es decir, la función no está definida cuando
$x = 0$, nota que no es necesario revisar las tres condiciones, basta
con encontrar una que no se cumpla para acertar su discontinuidad.

Sin embargo, una función puede no ser discontinua en algún punto y
continua en otro u otros puntos. La misma función $f(x) = \frac{1}{x}$
es continua en, por ejemplo, $x = 2$. Podemos verificar las tres
condiciones:

1.  $$\lim_{x \to 2} f(x) = \lim_{x \to 2} \frac{1}{x} = \frac{1}{2}$$
2.  $$f(2) = \frac{1}{2}$$
3.  $$\lim_{x \to 2} \frac{1}{x} = \frac{1}{2} = f(2)$$

y por lo tanto, la función es continua en $x = 2$

Ahora revisemos la continuidad de la función $f(x) = x^{2}$ cuando $x =
0$

1.  $$\lim_{x \to 0} f(x) = \lim_{x \to 0} x^{2} = 0^{2} = 0$$
2.  $$f(0) = 0^{2} = 0$$
3.  $$\lim_{x \to 0} x^{2} = 0 = f(0)$$

Nota que esta función $f(x) = x^{2}$ es continua en cualquier punto
$x = x_{0}$, porque el límite siempre existe y es igual a la función
evaluada en ese punto, es decir:

$$\lim_{x \to x_{0}} = f(x_{0})$$

La continuidad de una función está relacionada con su dominio. Si el
dominio de una función **no** son todos los números reales eso implica
que existe una discontinuidad. Sin embargo, lo converso no es
necesariamente cierto, es decir si una función está definida en todos
los números reales eso no implica que la función sea continúa.

Considera la continuidad de la función: $$f(x) = \begin{cases}
            x^{2} + 1, \text{ si } x \neq 1 \\
            0, \text{ si } x = 1
         \end{cases}$$ en $x = 1$.

Revisemos las tres condiciones:

1.  $$\lim_{x \to 1} f(x) = \lim_{x \to 1} x^{2} + 1 = 1^{2} + 1 = 2$$
2.  $$f(1) = 0$$

La condición 3 no se cumple, puesto que: $$\lim_{x \to 1} f(x) = 2$$ y
$$f(1) = 0$$ por lo tanto: $$\lim_{x \to 1} f(x) = 2 \neq 0 = f(1)$$

Nota en este ejemplo que la función esta definida en todos lo números
reales, sin embargo es discontinua.

Considera la continuidad de la función: $$f(x) = \begin{cases}
            2x + 1, \text{ si } x < 2 \\
            x - 2, \text{ si } x \geq 2
         \end{cases}$$
en $x = 2$.

En este ejemplo la condición 1 no se cumple. Vamos a utilizar límites laterales
para comprobar que el límite no existe.  Por la izquierda tenemos:
$$\lim_{x \to 2^{-}} f(x) = \lim_{x \to 2^{-}} 2x + 1 = 2(2) + 1 = 5$$
mientras que por la derecha:
$$\lim_{x \to 2^{+}} f(x) = \lim_{x \to 2^{+}} x - 1 = 2 - 1 = 1$$

Como 
$$\lim_{x \to 2^{-}} f(x) = 5 \neq 1 \lim_{x \to 2^{+}} f(x)$$
el límite *no* existe y por lo tanto es discontinua.

## Tipos de discontinuidad.


