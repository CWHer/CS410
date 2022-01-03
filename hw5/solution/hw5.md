## Homework5

### Problem1

$z=\theta^\top x$ is convex on $\theta$.
$$
\frac {\partial \mathcal L}{\partial z}= -y(1-\sigma(z)) + (1-y)\sigma(z)=-y+\sigma(z) \\
\frac {\partial^2  \mathcal L}{\partial z^2}=\sigma(z)(1-\sigma(z)) >0
$$
Thus, $ \mathcal L$ is convex on $z$. In sum, $\mathcal{L}$ is convex on $\theta$.

### Problem2

(a)
$$
h_1=\sigma( 1.5 \times 1 + 2.5\times 0+1 \times 1)=0.924 \\
h_2=\sigma(2 \times 1 -1.5\times 0 -3\times 1)=0.269\\
\widehat y=\sigma(-1 \times 1 + 1\times0.924+0.5\times 0.269)=0.515
$$
(b)

==New Weights==

Weight between input i and output j in layer k is denoted as $w_{ij}^{k}$
$$
\frac{\partial E}{\partial O}=O-1=-0.485 \\
\frac{\partial E}{\partial w_{11}^2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial w_{11}^2}=-0.1212\\
\frac{\partial E}{\partial w_{21}^2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial w_{21}^2}=-0.1120\\
\frac{\partial E}{\partial w_{31}^2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial w_{31}^2}=-0.0326\\
$$

| Layer 2 | output 1 |
| ------- | -------- |
| input 1 | -0.8788  |
| input 2 | 1.1120   |
| input 3 | 0.5326   |

$$
\frac{\partial E}{\partial h_1}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial h_1}=-0.1347\\
\frac{\partial E}{\partial h_2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial h_2}=-0.0645\\
$$

$$
\frac{\partial E}{\partial w_{11}^1}=\frac{\partial E}{\partial h_1}\cdot\frac{\partial h_1}{\partial w_{11}^1}=-0.0095\\
\frac{\partial E}{\partial w_{21}^1}=\frac{\partial E}{\partial h_1}\cdot\frac{\partial h_1}{\partial w_{21}^1}=0\\
\frac{\partial E}{\partial w_{31}^1}=\frac{\partial E}{\partial h_1}\cdot\frac{\partial h_1}{\partial w_{31}^1}=-0.0095\\
\frac{\partial E}{\partial w_{12}^1}=\frac{\partial E}{\partial h_2}\cdot\frac{\partial h_2}{\partial w_{12}^1}=-0.0126\\
\frac{\partial E}{\partial w_{22}^1}=\frac{\partial E}{\partial h_2}\cdot\frac{\partial h_2}{\partial w_{22}^1}=0\\
\frac{\partial E}{\partial w_{32}^1}=\frac{\partial E}{\partial h_2}\cdot\frac{\partial h_2}{\partial w_{32}^1}=-0.0126
$$

| Layer 1 | output 1 | output 2 |
| ------- | -------- | -------- |
| input 1 | 1.5095   | 2.0126   |
| input 2 | 2.5000   | -1.5000  |
| input 3 | 1.0095   | -2.9874  |

$$
h_1=0.9255 \\
h_2=0.2739\\
\widehat y=0.5735\\
E=0.0910
$$

New error is lower.

==Old Weights==

**Calculate gradient**

Weight between input i and output j in layer k is denoted as $w_{ij}^{k}$
$$
\frac{\partial E}{\partial O}=O-1=-0.485 \\
\frac{\partial E}{\partial h_1}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial h_1}=-0.121\\
\frac{\partial E}{\partial h_2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial h_2}=-0.061\\
\frac{\partial E}{\partial w_{11}^2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial w_{11}^2}=-0.1212\\
\frac{\partial E}{\partial w_{21}^2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial w_{21}^2}=-0.1120\\
\frac{\partial E}{\partial w_{31}^2}=\frac{\partial E}{\partial O}\cdot\frac{\partial O}{\partial w_{31}^2}=-0.0326\\
$$

$$
\frac{\partial E}{\partial w_{11}^1}=\frac{\partial E}{\partial h_1}\cdot\frac{\partial h_1}{\partial w_{11}^1}=-0.0085\\
\frac{\partial E}{\partial w_{21}^1}=\frac{\partial E}{\partial h_1}\cdot\frac{\partial h_1}{\partial w_{21}^1}=0\\
\frac{\partial E}{\partial w_{31}^1}=\frac{\partial E}{\partial h_1}\cdot\frac{\partial h_1}{\partial w_{31}^1}=-0.0085\\
\frac{\partial E}{\partial w_{12}^1}=\frac{\partial E}{\partial h_2}\cdot\frac{\partial h_2}{\partial w_{12}^1}=-0.0119\\
\frac{\partial E}{\partial w_{22}^1}=\frac{\partial E}{\partial h_2}\cdot\frac{\partial h_2}{\partial w_{22}^1}=0\\
\frac{\partial E}{\partial w_{32}^1}=\frac{\partial E}{\partial h_2}\cdot\frac{\partial h_2}{\partial w_{32}^1}=-0.0119
$$

**Step**
$$
\theta\leftarrow \theta-\eta\nabla E
$$

| Layer 1 | output 1 | output 2 |
| ------- | -------- | -------- |
| input 1 | 1.5085   | 2.0119   |
| input 2 | 2.5000   | -1.5000  |
| input 3 | 1.0085   | -2.9881  |

| Layer 2 | output 1 |
| ------- | -------- |
| input 1 | -0.8788  |
| input 2 | 1.1120   |
| input 3 | 0.5326   |

**New error**
$$
h_1=0.9253 \\
h_2=0.2737\\
\widehat y=0.5735\\
E=0.0910
$$
New error is lower.

### Problem3

(1)

Joint all factors

| $P_1$ | $P_2$ | $P_3$ | $P_4$ | $\mathbb P$     |
| ----- | ----- | ----- | ----- | --------------- |
| +     | +     | +     | +     | 0.4x0.8x0.2x0.8 |
| +     | +     | +     | -     | 0.4x0.8x0.2x0.2 |
| +     | +     | -     | +     | 0.4x0.8x0.8x0.8 |
| +     | +     | -     | -     | 0.4x0.8x0.8x0.2 |
| +     | -     | +     | +     | 0.4x0.2x0.3x0.5 |
| +     | -     | +     | -     | 0.4x0.2x0.3x0.5 |
| +     | -     | -     | +     | 0.4x0.2x0.7x0.5 |
| +     | -     | -     | -     | 0.4x0.2x0.7x0.5 |
| -     | +     | +     | +     | 0.6x0.5x0.2x0.8 |
| -     | +     | +     | -     | 0.6x0.5x0.2x0.2 |
| -     | +     | -     | +     | 0.6x0.5x0.8x0.8 |
| -     | +     | -     | -     | 0.6x0.5x0.8x0.2 |
| -     | -     | +     | +     | 0.6x0.5x0.3x0.5 |
| -     | -     | +     | -     | 0.6x0.5x0.3x0.5 |
| -     | -     | -     | +     | 0.6x0.5x0.7x0.5 |
| -     | -     | -     | -     | 0.6x0.5x0.7x0.5 |

After elimination, $\mathbb P(\neg P_3)=0.762$

(2)

Reuse joint table in (1).

After elimination, $\mathbb P(P_2\mid\neg P_3)=\frac{0.496}{0.762}=0.651$

(3)

Reuse joint table in (1).

After elimination, $\mathbb P(P_1\mid P_2,\neg P_3)=\frac{0.256}{0.496}=0.516$

(4)

Reuse joint table in (1).

After elimination, $\mathbb P(P_1\mid \neg P_3,P_4)=\frac{0.2328}{0.5298}=0.439$

### Problem4

Interleave joint and elimination.

(1)

Joint $P_1$ and $P_2$

| $P_1$ | $P_2$ | $\mathbb P$ |
| ----- | ----- | ----------- |
| +     | +     | 0.4x0.8     |
| +     | -     | 0.4x0.2     |
| -     | +     | 0.6x0.5     |
| -     | -     | 0.6x0.5     |

Eliminate $P_1$

| $P_2$ | $\mathbb P$ |
| ----- | ----------- |
| +     | 0.62        |
| -     | 0.38        |

Joint $P_2$ and $P_4$

| $P_2$ | $P_4$ | $\mathbb P$ |
| ----- | ----- | ----------- |
| +     | +     | 0.62x0.8    |
| +     | -     | 0.62x0.2    |
| -     | +     | 0.38x0.5    |
| -     | -     | 0.38x0.5    |

Eliminate $P_4$

| $P_2$ | $\mathbb P$ |
| ----- | ----------- |
| +     | 0.62        |
| -     | 0.38        |

Joint $P_2$ and $P_3$

| $P_2$ | $P_3$ | $\mathbb P$ |
| ----- | ----- | ----------- |
| +     | +     | 0.62x0.2    |
| +     | -     | 0.62x0.8    |
| -     | +     | 0.38x0.3    |
| -     | -     | 0.38x0.7    |

Eliminate $P_2$

| $P_3$ | $\mathbb P$ |
| ----- | ----------- |
| +     | 0.238       |
| -     | 0.762       |

Inference by enumeration: 2x2x2x2=16

Variable elimination: 2x2+2x2+2x2=12

(2)

Joint $P_1$ and $P_2$

| $P_1$ | $P_2$ | $\mathbb P$ |
| ----- | ----- | ----------- |
| +     | +     | 0.4x0.8     |
| +     | -     | 0.4x0.2     |
| -     | +     | 0.6x0.5     |
| -     | -     | 0.6x0.5     |

Eliminate $P_1$

| $P_2$ | $\mathbb P$ |
| ----- | ----------- |
| +     | 0.62        |
| -     | 0.38        |

Joint $P_2$ and $P_4$

| $P_2$ | $P_4$ | $\mathbb P$ |
| ----- | ----- | ----------- |
| +     | +     | 0.62x0.8    |
| +     | -     | 0.62x0.2    |
| -     | +     | 0.38x0.5    |
| -     | -     | 0.38x0.5    |

Eliminate $P_4$

| $P_2$ | $\mathbb P$ |
| ----- | ----------- |
| +     | 0.62        |
| -     | 0.38        |

Joint $P_2$ and $P_3$

| $P_2$ | $P_3$ | $\mathbb P$ |
| ----- | ----- | ----------- |
| +     | +     | 0.62x0.2    |
| +     | -     | 0.62x0.8    |
| -     | +     | 0.38x0.3    |
| -     | -     | 0.38x0.7    |

Eliminate $P_3$

| $\neg P_3$ | $P_2$    | $\neg P_2$ |
| ---------- | -------- | ---------- |
|            | 0.62x0.8 | 0.38x0.7   |

$\mathbb P(P_2\mid\neg P_3)=\frac{0.496}{0.762}=0.651$

Inference by enumeration: 2x2x2x2=16

Variable elimination: 2x2+2x2+2x2=12

**Findings**

1. VE is often of less computational complexity.
2. Inference by enumeration often allows the reuse of joint table while in most cases VE can not.

### Problem5

(a)

Path: `D - C - A` is active

No

(b)

Path: `D - E - B- C`, `D - E - A - C`, `D - A - E - B - C`, `D - A - C`. All inactive.

Yes

(c)

Path: `D - B - A` is active.

No

### Problem6

(a) $0.9 \times 0.8 = 0.72$ 

(b) 

|        |               |
| ------ | ------------- |
| W2 = R | 1.6/1.8=0.889 |
| W2 = S | 0.2/1.8=0.111 |

