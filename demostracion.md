---
header-includes: |
  ```{=tex}
  \usepackage{tikz} \usepackage{pgfplots}
  ```
  `\pgfplotsset{width=\textwidth,compat=1.9}`{=tex}
---

El concepto de demostración.
============================

La idea de demostrar algo en matemáticas consiste en presentar un
argumento que establezca la veracidad o falsedad de un enunciado. Por
ejemplo, considera el enunciado: **El cuadrado de cualquier número par
es también un número par**, podríamos considerar algunos ejemplos:

  $n$    $n^{2}$
  ------ ----------------
  $0$    $0^{2} = 0$
  $2$    $2^{2} = 4$
  $4$    $4^{2} = 16$
  $6$    $6^{2} = 36$
  $8$    $8^{2} = 64$
  $10$   $10^{2} = 100$

al parecer el patrón es cierto: *cualquier número par elevado al
cuadrado resulta en un número par*. Sin embargo, ¿cómo podemos estar
seguros de que este patrón se cumple para siempre?, ¿cómo podemos estar
seguros de que no existe algún número par que al elevarse al cuadrado
resulta en un número impar?

En este caso la demostración es muy sencilla: Considera que cualquier
número par se puede escribir como: $$2n, n \in \mathbb{Z}$$ esto
significa que un número par se puede escribir como $2$ multiplicado por
algún número entero. Por ejemplo, $0 = 2(0)$, $2 = 2(1)$, $4 = 2(2)$,
$6 = 2(3)$, $8 = 2(4)$, etc. Cuando elevamos un número par al cuadrado
obtenemos: $$(2n)^{2} = 4n^{2}$$ que podemos escribir como:
$$4n^{2} = 2 (2n^{2})$$ que evidentemente es un número par.

Considera el siguiente enunciado: **El cuadrado de cualquier número impar
es también un número impar**. Veamos algunos ejemplos:

  $n$    $n^{2}$
  ------ ----------------
  $1$    $1^{2} = 1$
  $3$    $3^{2} = 9$
  $5$    $5^{2} = 25$
  $7$    $7^{2} = 49$
  $9$    $9^{2} = 81$
  $11$   $11^{2} = 121$

al igual que en el caso de los números pares el patrón parece cierto.
¿Existe algún argumento que nos asegure que esto es cierto? La respuesta
es *si*, Considera que cualquier número impar puede ser escrito como:
$$2n + 1, n \in \mathbb{Z}$$ esto es: cualquier número impar es el
resultado de multiplicar un número entero por 2 y luego sumarle 1:
$1 = 2(0) + 1$, $3 = 2(1) + 1$, $5 = 2(2) + 1$, $7 = 2(3) + 1$,
$9 = 2(4) + 1$, $11 = 2(5) + 1$, etc. Cuando elevamos un número impar al
cuadrado obtenemos: $$(2n + 1)^{2} = 4n^{2} + 4n + 1$$ que podemos
escribir como: $$4n^{2} + 4n + 1 = 2(2n^{2} + 2n) + 1$$ que
evidentemente es un número impar.

Incluso podriamos combinar estos dos enunciados para formar un enunciado mas
fuerte: **Cualquier número entero al elevarse al cuadrado mantiene su paridad:
un número par al cuadrado resulta en un número par, mientras que un número
impar elevado al cuadrado resulta en un número impar.**

