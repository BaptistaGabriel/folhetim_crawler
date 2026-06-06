![](_page_0_Picture_1.jpeg)

Folhetim Educ. Mat., Feira de Santana, Ano 18, Número 166, maio/jun., 2012 ISSN 1415-8779

Este Folhetim é um veículo de divulgação, circulação de ideias e de estímulo ao estudo e à curiosidade intelectual. Dirige-se a todos os interessados pelos aspectos pedagógicos, filosóficos e históricos da Matemática. Pretende construir uma ponte para unir os que estão próximos e os que estão distantes.

Dando continuidade à transcrição das notas intituladas "A Matemática: suas origens, seu objeto e seus métodos - Parte I", de autoria do professor Carloman, neste número, veremos mais aplicações do Princípio de Indução Completa. O leitor terá a oportunidade de perceber que a utilidade do Princípio de Indução não se restringe à Teoria dos Números: o Exemplo 8 contém uma demonstração do Teorema do Binômio de Newton para anéis comutativos e o Exemplo 9 apresenta uma demonstração da Fórmula de Leibniz, muito utilizada no Cálculo Diferencial e Integral.

Outro destaque desta edição do Folhetim trata da possibilidade de se demonstrar leis operatórias. Deve ficar claro para o leitor que um postulado em uma axiomática pode ser um teorema em outra axiomática. Ademais, um postulado P em uma axiomática A, será sempre um postulado na axiomática A e nunca será demonstrado na axiomática A.

Carloman Carlos Borges (UEFS) - in memoriam Inácio de Sousa Fadigas (UEFS) Marcos Grilo Rosa (UEFS) Trazíbulo Henrique (UEFS)

A Matemática: suas origens, seu objeto e seus métodos (continuação)

Carloman Carlos Borges

# 3.1 Indução Completa (continuação)

Exemplo 5. Sejam a e n números naturais, n > 0. Consideremos a definição por recorrência:

$$a^1 = a$$

$$a^{n+1} = a^n.a$$

Dados a, n e m naturais com n > 0 e m > 0, vamos demonstrar as leis operatórias:

$$I) \quad a^m.a^n = a^{m+n}$$

$$II) \ (a^m)^n = a^{mn}$$

Para o item I), seja

$$P(n): a^m.a^n = a^{m+n}$$

Fixado m arbitrariamente, vem:

- i) Para n = 1, decorre da definição a <sup>m</sup>.a<sup>1</sup> = a <sup>m</sup>+1; logo, P(1) é verdadeira.
- ii) Suponhamos que P(n) é verdadeira para todo n natural; mostremos que, desta suposição, podemos concluir a verdade de P(n + 1), isto é:

$$P(n+1): a^m.a^{n+1} = a^{m+n+1}$$

Prova: Temos:

$$a^{m}.a^{n+1} = a^{m}.(a^{n}.a) = (a^{m}.a^{n}).a$$

= $a^{m+n}.a = a^{m+n+1}$

As igualdades acima justificam-se pelo uso, nessa ordem, da definição, da lei associativa, da hipótese de indução e novamente, da definição.

Para o item II), seja

$$P(n): (a^m)^n = a^{mn}$$

Fixado m arbitrariamente, temos:

- i) Para n = 1, decorre da definição (a m) <sup>1</sup> = a m; logo, P(1) é verdadeira.
- ii) Suponhamos que P(n) é verdadeira para todo n natural; mostremos, daí, a verdade de P(n + 1), isto é:

$$P(n+1): (a^m)^{n+1} = a^{m+n+1}$$

Prova:

$$(a^m)^{n+1} = (a^m)^n \cdot a^m = a^{mn} \cdot a^m =$$

= $a^{mn+n} = a^{m(n+1)}$

As igualdades acima justificam-se pelo uso, nessa ordem, da definição, da hipótese de indução, da propriedade (I) e da distributividade.

### Exemplo 6. Demonstrar que

$$P(n): (1^5 + \dots + n^5) + (1^7 + \dots + n^7) = 2\left[\frac{n(n+1)}{2}\right]^4$$

é verdadeira para n ≥ 1.

- i) P(1) é, evidentemente, verdadeira.
- ii) Supondo P(n) verdadeira, mostremos, que:

$$P(n+1): (1^5 + \dots + (n+1)^5) + (1^7 + \dots + (n+1)^7) =$$

$$= 2\left[\frac{(n+1)(n+2)}{2}\right]^4$$

Prova:

$$(1^{5} + \dots + n^{5} + (n+1)^{5}) + (1^{7} + \dots + n^{7} + (n+1)^{7}) =$$

$$= 2\left[\frac{n(n+1)}{2}\right]^{4} + (n+1)^{5} + (n+1)^{7} =$$

$$= (n+1)^{4}\left[\frac{n^{4} + (n+1 + (n+1)^{3})2^{3}}{2^{3}}\right] =$$

$$= (n+1)^{4}\left[\frac{n^{4} + 8n^{3} + 24n^{2} + 32n + 16}{2^{3}}\right] =$$

$$= \left[\frac{(n+1)^4(n+2)^4}{2^3}\right] = 2\left[\frac{(n+1)(n+2)}{2}\right]^4$$

Logo, P(n) é verdadeira para qualquer número natural n ≥ 1.

Exemplo 7. Demonstrar que 32n+2 − 2 <sup>n</sup>+1 é divisível por 7, qualquer que seja n natural maior do que 1. Temos:

- i) Para n = 1, 3<sup>4</sup> − 2 <sup>2</sup> = 81 − 4 = 77, donde P(1) é verdadeira.
- ii) Supondo que P(n) é verdadeira para qualquer que seja n natural, mostremos que P(n + 1) é verdadeira, isto é, 32n+4 − 2 <sup>n</sup>+2 é divisível por 7. Para facilitar a demonstração, denotemos a expressão 3 <sup>2</sup>n+2 − 2 <sup>n</sup>+1 por Pn.

Prova:

$$P_{n+1} - P_n = 3^{2n+4} - 3^{2n+2} - (2^{n+2} - 2^{n+1}) =$$

$$= 3^{2n+2}(9-1) - 2^{n+1}(2-1) =$$

$$= 3^{2n+2}.8 - 2^{n+1}$$

isto é,

$$P_{n+1} - P_n = 3^{2n+2} \cdot 8 - 2^{n+1} = 7 \cdot 3^{2n+2} + P_n$$

donde,

$$P_{n+1} = 7.3^{2n+2} + 2P_n$$

o que demonstra o resultado.

Exemplo 8. Considere um anel comutativo A e x e y dois de seus elementos. Demonstre a fórmula do Binômio de Newton:

$$(x+y)^n = \sum_{k=0}^n C_n^k x^k y^{n-k}, n \ge 1$$

Temos:

i) Para n = 1,

$$x + y = \begin{pmatrix} 0 \\ 0 \end{pmatrix} x^1 y^0 + \begin{pmatrix} 1 \\ 0 \end{pmatrix} x^0 y^1$$

## NEMOC - NUCLEO DE EDUCAC¸ ´ AO MATEM ˜ ATICA OMAR CATUNDA ´

Folhetim Educ. Mat., Feira de Santana, Ano 18, Número 166, maio/jun. 2012 - Editores: Inácio, Grilo e Trazíbulo - Digitação: Josenildes Oliveira Venas Almeida e Manoel Aquino dos Santos - Editoração: Evandro Vaz e Nivaldo Assis - Impressão: Imprensa Gráfica Universitária - Periodicidade: bimestral - Tiragem: 1.500 exemplares - Distribuição gratuita - Endereço: Avenida Transnordestina s/n, Módulo Prof. Carloman Carlos Borges, bairro Novo Horizonte, Feira de Santana, BA, Brasil. CEP 44.036-900. - Telefone: (75)3161-8115 - Fax: (75)3161-8086 - E-mail: nemoc@uefs.br - Home-Page: www.uefs.br/nemoc

ii) Supondo que P(n) é verdadeira, demonstre que P(n+1) é verdadeira, isto é,

$$(x+y)^{n+1} = \sum_{k=0}^{n+1} C_{n+1}^k x^k y^{n+1-k}, \quad n \ge 1$$

Prova: multiplicando ambos os membros da hipótese de indução por x + y, vem:

$$(x+y)^{n+1} = \sum_{k=0}^{n} C_n^k x^{k+1} y^{n-k} + \sum_{k=0}^{n} C_n^k x^k y^{n+1-k} \quad (I)$$

Em (I), podemos reescrever os dois somatórios da seguinte forma:

$$\sum_{k=0}^{n} C_n^k x^{k+1} y^{n-k} = \sum_{k=1}^{n+1} C_n^{k-1} x^k y^{n+1-k} =$$

$$= x^{n+1} + \sum_{k=1}^{n} C_n^{k-1} x^k y^{n+1-k} \quad (II)$$

$$\sum_{k=0}^{n} C_n^k x^k y^{n+1-k} = y^{n+1} + \sum_{k=1}^{n} C_n^k x^k y^{n+1-k} \quad (III)$$

Aplicando (II) e (III) em (I):

$$(x+y)^{n+1} =$$

$$= x^{n+1} + \sum_{k=1}^{n} (C_n^{k-1} + C_n^k) x^k y^{n+1-k} + y^{n+1}$$

A relação de Stifel

$$C_n^{k-1} + C_n^k = C_{n+1}^k$$

resulta na comprovação de P(n+1), pois:

$$(x+y)^{n+1} =$$

$$= x^{n+1} + \sum_{k=1}^{n} C_{n+1}^{k} x^{k} y^{n+1-k} + y^{n+1} =$$

$$= \sum_{k=0}^{n+1} C_{n+1}^{k} x^{k} y^{n+1-k}$$

**Exemplo 9.** Uma aplicação do exemplo 8 é mostrar a chamada Fórmula de Leibniz:

$$P(n): (u.v)^{(n)} = \sum_{k=0}^{n} C_n^k u^{(n-k)} v^{(k)}$$

sendo u e v funções de x que possuem derivadas de qualquer ordem no intervalo I.

Temos:

i) Para
$$n = 1$$
: $(u.v)^{(1)} = C_1^0 u^{(1)} v + C_1^1 u v^{(1)} =$

= u'.v + u.v'

ii) Mostremos que:

$$(u.v)^{(n+1)} = \sum_{k=0}^{n+1} C_{n+1}^k u^{(n+1-k)} v^{(k)}$$

Prova: diferenciando ambos os membros da hipótese:

$$(u.v)^{(n+1)} = \sum_{k=0}^{n} C_n^k u^{(n+1-k)} v^{(k)} + \sum_{k=0}^{n} C_n^k u^{(n-k)} v^{(k+1)}$$

Daí em diante, a marcha é inteiramente análoga ao exercício anterior.

**Exemplo 10.** Uma sequência de números reais é definida como segue:

$$P(n): \begin{cases} u_0 = u_1 = u_2 = 1\\ u_n = \left[\frac{u_{n-1} + u_{n-2} + u_{n-3}}{3}\right], & n \ge 3 \end{cases}$$

Mostrar que $u_n = 1$ para qualquer natural n. Temos:

i) Para n = 0, 1 e 2, a propriedade se verifica, pois:

$$u_0 = u_1 = u_2 = 1$$

ii) Admitindo-se que dado n natural, a proposição é verdadeira para 0, 1, ..., n-1, mostremos que ela é verdadeira para n.

Prova: realmente:

$$u_n = \left[\frac{u_{n-1} + u_{n-2} + u_{n-3}}{3}\right] =$$
$$= \left[\frac{1+1+1}{3}\right] = 1$$

Logo, a proposição é verdadeira para qualquer n natural.

Observação: é importante ressaltar que se trata de um caso particular de recorrência, pois a propriedade tem de se verificar para n=0,1,2; uma vez que não se verificasse para n=2, o raciocínio seria falso. Por exemplo: uma sequência de números reais é definida como segue,

$$u_0 = u_1 = 1$$

$$u_2 = 4$$

$$u_n = \left[\frac{u_{n-1} + u_{n-2} + u_{n-3}}{3}\right], \quad n \ge 3$$

É fácil mostrar que a proposição é verdadeira para n=0,1 e, em seguida, se ela é verdadeira para n-1, n-2 e n-3, resulta ser verdadeira para qualquer n; porém, se trata de um raciocínio falso pois, para n=2, tem-se $u_2=4$ , para n=3, tem-se $u_3=2$ , etc.

**Exemplo 11.** Consideremos a assim fórmula de Moivre:

$$[\rho(\cos x + i \sin x)]^n = \rho^n[(\cos(nx) + i \sin(nx))]$$

na qual $\rho$ é um número natural, $-\pi \le x \le \pi$ , $i = \sqrt{-1}$ e n um número natural qualquer.

Temos:

- i) Para n = 1, P(1) é, evidentemente, verdadeira.
- ii) Supondo que P(n) é verdadeira, mostremos que P(n+1) é verdadeira:

$$[\rho(\cos x + i \sin x)]^{n+1} =$$

$$= \rho^{n+1} [(\cos((n+1)x) + i \sin((n+1)x))]$$

Prova: desenvolvendo o primeiro membro da tese, vem:

$$[\rho(\cos x + i \sin x)]^{n+1} =$$

$$= \rho(\cos x + i \sin x)[\rho(\cos x + i \sin x)]^{n} =$$

$$= [\rho(\cos x + i \sin x)]\rho^{n}[\cos(nx) + i \sin(nx)] =$$

$$= [\rho^{n+1}(\cos(n+1)x + i \sin(n+1)x)]$$

A hipótese de indução justifica a segunda igualdade.

### Exemplo 12. Seja

$$P(n): \frac{1}{2} + \cos a + \cos 2a + \dots + \cos na = \frac{sen\frac{2n+1}{2}a}{2sen\frac{a}{2}}$$

Vamos mostrar que P(n) é satisfeita para qualquer n inteiro maior ou igual a zero, com a restrição, naturalmente, de que a que é um número real, seja diferente de um múltiplo inteiro de $2\pi$ .

i) Para n=0, temos:

$$\frac{1}{2} = \frac{1}{2}$$

ii) Supondo P(n) verdadeira, mostremos que, daí, se pode deduzir a verdade de P(n+1):

$$\frac{1}{2} + \cos a + \dots + \cos(na) + \cos(n+1)a = \frac{sen\frac{2n+3}{2}a}{2sen\frac{a}{2}}$$

Prova:

$$\frac{1}{2} + \cos a + \dots + \cos(na) + \cos(n+1)a =$$

$$= \frac{sen\frac{2n+1}{2}a}{2sen\frac{a}{2}} + \cos(n+1)a =$$

$$= \frac{sen\frac{2n+3}{2}a}{2sen\frac{a}{2}} \quad (I)$$

A demonstração termina se mostrarmos a validade de (I). Ora, podemos reescrever (I) na seguinte forma:

$$sen \frac{2n+3}{2}a - sen \frac{2n+1}{2} =$$

= $2 sen \frac{a}{2} cos((n+1)a)$ (II)

Em (II) temos, no primeiro membro, a diferença entre dois senos e esta, pela Trigonometria, é igual ao segundo membro de (II).

# PRÓXIMO NÚMERO

A Matemática: suas origens, seu objeto e seus métodos. (Continuação)

# **NOTÍCIAS**

## Revista Professor de Matemática Online

A SBM está lançando a revista Professor de Matemática Online (PMO), um veículo para publicação ágil e ampla divulgação de artigos acadêmicos relevantes à formação inicial e continuada do professor da Educação Básica, cobrindo todos os temas da Matemática, sua prática de ensino, sua história e suas aplicações. Ela poderá publicar trabalhos de conclusão de curso, ferramentas virtuais e outros produtos de docentes e discentes dos programas de formação de professores de Matemática. Maiores informações, no site: http://pmo.sbm.org.br

### **CEEM Semipresencial**

O Núcleo de Informática e Sociedade (NIS) e o NEMOC oferecerão o Curso de Especialização em Educação Matemática, modalidade semipresencial. As inscrições ocorrerão no período de 01 a 26 de outubro de 2012. Cada disciplina terá 15 horas presenciais na UEFS e 30 horas à distância. Maiores informações, no site do NEMOC: <a href=" http://www.uefs.br/nemoc">http://www.uefs.br/nemoc</a>

# **NÚMEROS ATRASADOS**

Envie para cada Folhetim um selo de postagem nacional de 1º porte. Dentro de no máximo quatro semanas, contadas a partir da data de recebimento do seu pedido, você receberá os folhetins solicitados. OBS.: É permitida a reprodução total ou parcial deste Folhetim, desde que citada a fonte.
