## Homework4

### Problem1

(a)
$$
\text{sample}=r+\gamma V^\pi(s')\\
V^{\pi}(s)\leftarrow V^{\pi}(s) +\alpha(\text{sample}-V^{\pi}(s))
$$

$$
V_{t+1}(C)=0.6+0.5\times(0+1\times 0.4-0.6)=0.5\\
V_{t+2}(B)=0.4+0.5\times(0+1\times 0.2-0.4)=0.3\\
V_{t+3}(A)=0.2+0.5\times(0+1\times 0.3-0.2)=0.25\\
V_{t+4}(B)=0.3+0.5\times(0+1\times 0.5-0.3)=0.4\\
V_{t+5}(C)=0.5+0.5\times(0+1\times 0.8-0.5)=0.65\\
V_{t+6}(D)=0.8+0.5\times(0+1\times 1.0-0.8)=0.9\\
V_{t+7}(E)=1.0+0.5\times(1+1\times 0-1.0)=1.0\\
$$

(b)
$$
\begin{aligned}
\mid V_{n+m}-V_{n} \mid &=[1-(1-\alpha_{n+m})(1-\alpha_{n+m-1})\cdots(1-\alpha_{n+1})]V_n\\
	&+ (1-\alpha_{n+m})\cdots(1-\alpha_{n+2})\alpha_{n+1}x_{n+1} \\
	&+(1-\alpha_{n+m})\cdots(1-\alpha_{n+3})\alpha_{n+2}x_{n+2} \\
	& +\cdots \\
	&\leq [1-\frac{n(n+2)}{(n+1)^2}\cdots \frac{(n+m-1)(n+m+1)}{(n+m)^2}]V_n + \sum_{i=1}^m a_{n+i}x_{n+i} \\
	&\leq C_2[1- \frac{n(n+m+1)}{(n+1)(n+m)}]+C_1\sum_{i=1}^m  \frac{1}{(n+i)^2} \\
	&\leq C_2[1- \frac{n}{n+1}] + C_1\sum_{i=1}^m  \frac{1}{(n+i)(n+i-1)} \\
	&\leq \frac{C_2}{n+1} + \frac{C_1}{n+1}
\end{aligned}
$$
Thus, when $n\rightarrow \infin$, $\mid V_{n+m}-V_{n} \mid \rightarrow 0$. $\{V_n\}$ is a Cauchy sequence. 

### Problem2

(a)
$$
\begin{aligned}
\mid H(q_1)-H(q_2)\mid&=\gamma \sum_{s^\prime} T(s,a,s') \mid  \max_{a'} q_1(s',a') -  \max_{a'} q_2(s',a') \mid \\
\end{aligned}
$$
If we assume $\max_{a'} q_1(s',a') \geq  \max_{a'} q_2(s',a')$, then
$$
\max_{a'} q_1(s',a') -   q_2\left(s',\arg \max_{a} q_1(s,a)\right) \geq \max_{a'} q_1(s',a') -  \max_{a'} q_2(s',a') \\
$$
This still holds when $\max_{a'} q_1(s',a') \leq  \max_{a'} q_2(s',a')$.

Thus, we have
$$
\begin{aligned}
\mid H(q_1)-H(q_2)\mid& \leq \gamma \sum_{s^\prime} T(s,a,s') \max_{a'} \mid   q_1(s',a') -   q_2(s',a') \mid \\
&\leq \gamma \sum_{s^\prime} T(s,a,s') \left \|  q_1-q_2\right \|_{\infin}  \\
&=\gamma  \left \|  q_1-q_2\right \|_{\infin}  \\
\end{aligned}
$$
We can conclude that $\mid H(q_1)-H(q_2)\mid_{\infin } \leq \gamma  \left \|  q_1-q_2\right \|_{\infin} 
$. $H$ is a contradiction mapping.

(b)
$$
\begin{aligned}
\Delta_{t+1}(s,a)&=Q_{t+1}(s,a)-Q^\star(s,a) \\
&=(1-\alpha_{t})Q_{t}(s,a)+\alpha_t [R(s,a,s')+\gamma\max _{a'}Q_t(s',a')]-Q^\star(s,a)\\
&=(1-\alpha_{t})\Delta_{t}(s,a)+ \alpha_t [R(s,a,s')+\gamma\max _{a'}Q_t(s',a')-Q^\star(s,a)]

\end{aligned}
$$

- By definition, $0\leq\alpha_{t}\leq1$, $\sum_{t} \alpha_{t}=\infty$ and $\sum_{t} \alpha^2_{t}<\infty$

- Consider that MDP is stateless. We have $\mathbb{E}\left[F_{t} \mid \mathcal{F}_{t}\right]=\mathbb{E}\left[F_{t} \right]$
  $$
  \begin{aligned}
  \mathbb{E}\left[F_{t}(s,a) \right]&=\mathbb{E}[R(s,a,s')+\gamma\max _{a'}Q_t(s',a')]-Q^\star(s,a)\\
  &=H(Q_t(s,a))-H(Q^\star(s,a)) \\
  &\leq \left |H(Q_t)-H(Q^\star) \right |_{\infin}\leq \gamma  \left \|  Q_t-Q^\star \right \|_{\infin} 
  \end{aligned}
  $$
  Thus, $\mathbb{E}\left[F_{t} \mid \mathcal{F}_{t}\right]_{\infin} \leq \gamma \left \|  \Delta_t \right \|_{\infin} $

- $\mathbb{V}\left[F_{t}(s,a) \right]=\mathbb{V}\left[F_{t}(s,a) +Q^\star(s,a)\right]$
  $$
  \begin{aligned}
  \mathbb{V}\left[F_{t}(s,a) \right]&=\mathbb{V}[R(s,a,s')+\gamma\max _{a'}Q_t(s',a')]\\
  &= \mathbb{E}[(R(s,a,s')+\gamma\max _{a'}Q_t(s',a'))^2]-H^2(Q_t(s,a))
  \end{aligned}
  $$
  As $R$ and $Q_t$ are bounded, $ \mathbb{E}[(R(s,a,s')+\gamma\max _{a'}Q_t(s',a'))^2]$ is also bounded.

  Thus, $\mathbb V\left[F_{t}(x) \mid \mathcal{F}_{t}\right]< C$

Now it is sufficient to apply Lemma 1 to $\Delta_t(s,a)$. We have $\Delta_t(s,a)\rightarrow 0$, $Q_t(s,a)\rightarrow Q^\star(s,a)$. When $t\rightarrow \infin$, since $\mathbb{P}_{\pi}\left[A_{t}=a \mid S_{t}=s\right]>0$, the number of iterations tend to infinity for all state-action pairs. Thus, $Q_t\rightarrow Q^\star$.

### Problem3

(a)

The normal equation is $X^\top X \theta=X^\top y $

where
$$
X=\left[\begin{array}{cc}
1 & 6.2 \\
1 & 6.5 \\
1 & 5.48 \\
1 & 6.54 \\
1 & 7.18 \\
1 & 7.93
\end{array}\right], y=\left[\begin{array}{c}
26.3 \\
26.65 \\
25.03 \\
26.01 \\
27.9 \\
30.47
\end{array}\right]
$$
and 
$$
\theta=\left[\begin{array}{c}
12.55 \\
2.19
\end{array}\right]
$$
(b)
$$
7*2.19+12.55=27.88
$$
