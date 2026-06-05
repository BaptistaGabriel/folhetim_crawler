![](_page_0_Picture_1.jpeg)

Folhetim Educ. Mat., Feira de Santana, Ano 19, N´umero 168, set./out., 2012 ISSN 1415-8779

Este Folhetim ´e um ve´ıculo de divulga¸c˜ao, circula¸c˜ao de ideias e de est´ımulo ao estudo e `a curiosidade intelectual. Dirige-se a todos os interessados pelos aspectos pedag´ogicos, filos´oficos e hist´oricos da Matem´atica. Pretende construir uma ponte para unir os que est˜ao pr´oximos e os que est˜ao distantes.

Dando continuidade `a transcri¸c˜ao das notas intituladas "A Matem´atica: suas origens, seu objeto e seus m´etodos - Parte I", de autoria do professor Carloman, neste n´umero, veremos as Demonstra¸c˜oes Indiretas. O texto basicamente ´e apresentado por meio de exemplos de aplica¸c˜ao da tautologia que estabelece a equivalˆencia entre a implica¸c˜ao da hip´otese para a tese e a falsidade da conjun¸c˜ao entre a hip´otese e a nega¸c˜ao da tese. Os exemplos s˜ao ricos e abrangentes, e v˜ao desde propriedades dos n´umeros racionais e irracionais, passando por propriedades dos n´umeros primos. Outra equivalˆencia l´ogica, a contrapositiva da condicional, tamb´em ´e ilustrada com v´arios exemplos da teoria dos n´umeros, conjuntos e geometria.

Carloman Carlos Borges (UEFS) - in memoriam In´acio de Sousa Fadigas (UEFS) Marcos Grilo Rosa (UEFS) Traz´ıbulo Henrique (UEFS)

A Matem´atica: suas origens, seu objeto e seus m´etodos (continua¸c˜ao)

Carloman Carlos Borges

### 4. Demonstra¸c˜oes indiretas

Algumas das demonstra¸c˜oes indiretas podem ser justificadas pela tautologia:

(H ⇒ T) ⇔ [( H∧ ∼ T) ⇒ f] cuja tabela-verdade damos abaixo:

| H | T | H ⇒ T | ∼ T | H∧ ∼ T | f | (H∧ ∼ T) ⇒ f | (H ⇒ T) ⇔      |
|---|---|-------|-----|--------|---|--------------|----------------|
|   |   |       |     |        |   |              | [(H∧ ∼ T) ⇒ f] |
| V | V | V     | F   | F      | F | V            | V              |
| V | F | F     | V   | V      | F | F            | V              |
| F | V | V     | F   | F      | F | V            | V              |
| F | F | V     | V   | F      | F | V            | V              |

Alguns exemplos servir˜ao para ilustrar o emprego dessa importante tautologia.

Exemplo 1. Sendo a um n´umero racional e b um n´umero irracional, mostre que:

i) a + b ´e irracional

ii) a · b ´e irracional (a 6= 0)

Para (i), temos,

$$H \left\{ \begin{array}{ll} a, & \text{racional} \\ b, & \text{irracional} \end{array} \right.$$

T: a + b ´e irracional ∼ T: a + b ´e racional

Consideremos, ainda:

H' : H ∧ ∼ T T': f

Demonstra¸c˜ao: N = a + b (um n´umero racional, conforme H'), donde conclu´ımos N - a = b; ora, como N ´e racional e a, igualmente, N - a ´e um n´umero racional (a diferen¸ca entre dois racionais é um racional); logo, N - a=b representa uma contradição pois, no primeiro membro temos um número racional, N - a, enquanto no segundo membro temos b, que é irracional. Conforme a tautologia em estudo, concluímos definitivamente: a+b é um número irracional. A demonstração de (ii) é inteiramente análoga.

**Exemplo 2.** Mostre que  $\sqrt{n}$  é um número irracional, toda vez que o número n não seja o quadrado de outro número natural. Temos:

$$H\left\{ \begin{array}{ll} n \neq m^2, & m \quad \text{um número natural} \\ x = \sqrt{n} \end{array} \right.$$

 $T: x \text{ \'e irracional} \sim T: x \text{ \'e racional}$ 

Consideremos, ainda:

$$H': H \wedge \sim T$$
  $T': f$ 

Demonstração:  $x=\sqrt{n}=\frac{p}{q}$  é racional (conforme H'; aqui, p e q são dois números inteiros, primos entre si). Elevando ambos os membros ao quadrado e transpondo  $q^2$  ao primeiro membro, obtemos  $nq^2=p^2$ .

Mostremos, agora, que  $nq^2 = p^2$ , que é o nosso T' representa uma contradição. Realmente, devido ao sinal de igualdade, os dois números  $nq^2$  e  $p^2$  quando decompostos em fatores primos deverão coincidir, isto é, a representação de  $nq^2$  como produto de fatores primos deverá apresentar os mesmos fatores primos da representação de  $p^2$  quando escrito como produto de fatores primos. Cada número primo deve aparecer um número par de vezes na decomposição tanto de  $p^2$  como de  $q^2$ (pois ambos os números  $p \in q$  estão ao quadrado) e isto significa que a mesma coisa deverá ocorrer na decomposição de n, o que implica ser n um quadrado perfeito, contrariando, portanto H. Logo, de acordo com a tautologia,  $\sqrt{n}$  é um número irracional toda vez que n não for um quadrado perfeito. Observação: na demonstração acima empregamos

o chamado "Teorema Fundamental da Aritmética": "Todo número inteiro N maior do que 1, pode ser decomposto em um produto de fatores primos, e esta decomposição é única, a menos da ordem dos fatores".

**Exemplo 3.** Mostre que  $\sqrt{2} + \sqrt{5}$  é um número irracional. Temos:

$$H: x = \sqrt{2} + \sqrt{5};$$

T: x é irracional  $\sim T$ : x é racional

Seja ainda:

$$H': H \wedge \sim T$$
  $T': f$ 

Demonstração: seja

 $x = \sqrt{2} + \sqrt{5}$  um número racional (conforme H').  $x^2 = 7 + 2\sqrt{10}$  (elevando ao quadrado)

Ora,  $x^2 = 7 + 2\sqrt{10}$  representa uma contradição pois,  $x^2$  é racional (o quadrado de todo número racional é um número racional), enquanto  $7 + 2\sqrt{10}$  é um número irracional conforme exemplos 1 e 2, logo acima. Assim, a demonstração está terminada.

**Exemplo 4.** Mostre que existem infinitos números primos. Temos:

H: seja C o conjunto dos números primos  $p_1$ ,  $p_2$ ,  $p_3$ , etc.;

 $T: C \neq \text{ um conjunto infinito } \sim T: C \neq \text{ finito}$ 

Consideremos, ainda:

$$H': H \wedge \sim T$$
  $T': f$ 

Demonstração: conforme H', C é um conjunto finito de números primos, isto é, C é um conjunto formado dos únicos números primos  $p_1, p_2, \ldots p_n$ ; então, há sentido formar-se o número  $N = (p_1 \cdot p_2 \cdot \ldots \cdot p_n) + 1$ ; a análise de N nos leva a uma contradição, senão vejamos:

### NEMOC - NÚCLEO DE EDUCAÇÃO MATEMÁTICA OMAR CATUNDA

Folhetim Educ. Mat., Feira de Santana, Ano 19, Número 168, set./out. 2012 - Editores: Inácio, Grilo e Trazíbulo - Digitação: Josenildes Oliveira Venas Almeida e Manoel Aquino dos Santos - Editoração: Evandro Vaz e Nivaldo Assis - Impressão: Imprensa Gráfica Universitária - Periodicidade: bimestral - Tiragem: 1.500 exemplares - Distribuição gratuita - Endereço: Avenida Transnordestina s/n, Módulo Prof. Carloman Carlos Borges, bairro Novo Horizonte, Feira de Santana, BA, Brasil. CEP 44.036-900. - Telefone: (75)3161-8115 - Fax: (75)3161-8086 - E-mail: nemoc@uefs.br - Home-Page: www.uefs.br/nemoc

- a) N ´e, claramente, maior que 1 (estamos considerando apenas os n´umeros primos positivos);
  - b) N ´e maior que cada um dos p<sup>i</sup> ;
- c) N n˜ao ´e um n´umero primo, pois ele ´e diferente e maior do que cada um dos p<sup>i</sup> existentes;
- d) N n˜ao sendo um n´umero primo, pode ser decomposto num produto de fatores primos, conforme Teorema Fundamental da Aritm´etica;
- e) Como N 1 ´e divis´ıvel por cada um dos p<sup>i</sup> , isto significa que N n˜ao o ´e e, conforme (d), na decomposi¸c˜ao de N h´a de aparecer um n´umero primo diferente de cada um dos p<sup>i</sup> .

Esta contradi¸c˜ao demonstra o teorema de que existem infinitos n´umeros primos.

Exemplo 5. Aqui, empregamos a equivalˆencia:

$$(H \Rightarrow T) \Longleftrightarrow (\sim T \Rightarrow \sim H)$$

Considere o teorema: "Se x <sup>2</sup> ´e divis´ıvel por 5 ent˜ao, x tamb´em o ´e". Temos:

H: x <sup>2</sup> ´e divis´ıvel por 5;

T: x ´e divis´ıvel por 5;

∼ T: x n˜ao ´e divis´ıvel por 5;

∼ H: x <sup>2</sup> n˜ao ´e divis´ıvel por 5.

Podemos, pois, escrever a equivalˆencia:

<sup>2</sup> ´e divis´ıvel por 5, ent˜ao, x tamb´em o ´e".

"Se 
$$x^2$$
 é divisível por 5, então,  $x$  também o é"  $\updownarrow$ 

"Se x n˜ao ´e divis´ıvel por 5, ent˜ao, x 2 tamb´em n˜ao o ´e".

Neste caso, temos:

$$\sim T \left\{ \begin{array}{l} x = 5n+1 \\ x = 5n+2 \\ x = 5n+3 \\ x = 5n+4 \end{array} \right. \sim H \left\{ \begin{array}{l} x^2 = 5p+1 \\ x^2 = 5p+2 \\ x^2 = 5p+3 \\ x^2 = 5p+4 \end{array} \right.$$

n e p s˜ao n´umeros naturais.

Demonstra¸c˜ao: temos que considerar, separadamente, cada um dos quatro tipos da hip´otese (∼ T) e verificar se, partindo da´ı, chegamos a um dos tipos representados pela tese (no caso ∼ H). Assim, de x = 5n + 1, vem:

$$x^2 = 25n^2 + 10n + 1 = 5(5n^2 + 2n) + 1 = 5p + 1$$
 (fazendo  $5n^2 + 2n = p$ )

De 
$$x = 5n + 2$$
, vem:

$$x^2 = 25n^2 + 20n + 4 = 5(5n^2 + 4n) + 4 = 5p + 4$$

De 
$$x = 5n + 3$$
, vem:

$$x^{2} = 25n^{2} + 30n + 9 = 5(5n^{2} + 6n + 1) + 4 = 5p + 4$$

Finalmente, de x = 5n + 4, tem-se:

$$x^{2} = 25n^{2} + 40n + 16 = 5(5n^{2} + 8n + 3) + 1 = 5p + 1$$

e a demonstra¸c˜ao est´a terminada.

Exemplo 6. Considere a defini¸c˜ao: "no plano euclidiano, duas retas AB e CD s˜ao paralelas se, e somente se, sua interse¸c˜ao ´e vazia". Consideremos a figura abaixo:

![](_page_2_Picture_31.jpeg)

Seja a hip´otese: "os ˆangulos 1 e 2 s˜ao iguais entre si"; tese: "as retas AB e CD s˜ao paralelas". Temos:

∼ T: AB e CD se intersectam em I;

∼ H: os ˆangulos 1 e 2 s˜ao diferentes entre si.

Demonstra¸c˜ao: no triˆangulo PQI, o ˆangulo 2 ´e interno, enquanto que o ˆangulo 1 ´e exterior; logo, a medida de 1, isto ´e, m(1) ´e maior que m(2) pois "a medida do ˆangulo externo de um triˆangulo ´e igual `a soma das medidas dos dois ˆangulos internos n˜ao adjacentes" (prove este teorema); esta contradi¸c˜ao prova o teorema, conforme a equivalˆencia usada no exemplo 5.

Exemplo 7. Sejam A, B e C trˆes conjuntos, f uma aplica¸c˜ao de A dentro de B e g uma aplica¸c˜ao de B dentro de C. Demonstre: se gof ´e injetora ent˜ao f ´e injetora.

No teorema direto temos:

H: gof ´e injetora;

T: f ´e injetora.

ent˜ao, podemos escrever:

∼ T: f n˜ao ´e injetora;

∼ H: gof ´e n˜ao injetora.

Demonstra¸c˜ao: se f n˜ao ´e injetora ent˜ao, por defini¸c˜ao, existem em A dois elementos a e a 0 com a mesma imagem y por f, donde se conclui que a e a 0 ter˜ao mesma imagem g(y) por gof, o que implica a fun¸c˜ao composta ser n˜ao injetora.

**Exemplo 8.** Sejam  $E_1$  e  $E_2$  dois espaços métricos com as distâncias respectivas  $d_1$  e  $d_2$ ; então, uma aplicação de  $E_1$  dentro de  $E_2$  é uniformemente contínua se, para todo  $\varepsilon > 0$ , existe a > 0 tal que, quaisquer que sejam x e x dentro de  $E_1$ , tem-se:

$$d_1(x', x'') < a \Rightarrow d_2(f(x'), f(x'')) < \varepsilon$$

Esta definição é equivalente à seguinte: seja f uma função real (pode ser complexa também) definida sobre um intervalo I. A função f é uniformemente contínua dentro de I se, para  $\varepsilon>0$ , existe a>0, tal que

$$|x - x'| < a, \quad x, x' \in I \quad \Rightarrow |f(x) - f(x')| < \varepsilon$$

É evidente que uma função uniformemente contínua dentro de  $E_1$  é contínua em todo ponto de  $E_1$ , porém, a recíproca é falsa. Por exemplo: seja a função  $f(x) = x^2$ , a qual é contínua para qualquer x real, porém, esta função não é uniformemente contínua dentro de  $\mathbb{R}$ . Temos:

H: f é contínua para qualquer x real;

T: f não é uniformemente contínua para qualquer x real;

 $\sim T$ : f é uniformemente contínua;

 $\sim H$ : f não é contínua.

Demonstração: na definição acima basta fazer  $\varepsilon = 1$ ; existirá, então, um número a > 0 tal que:

$$|x-x'| < a$$
,  $x, x' \in \mathbb{R}$ ,  $\Rightarrow |x^2 - x'^2| > 1$ 

Façamos 
$$x=\frac{1}{a}, x'=\frac{1}{a}+\frac{a}{2}.$$
 Tem-se:  $|x-x'|=\frac{a}{2}< a,$  e  $|x^2-x'^2|=|\frac{1}{a^2}-(\frac{1}{a^2}+\frac{a^2}{4}+1)|=1+\frac{a^2}{4}>1.$ 

**Exemplo 9.** A propriedade mais importante dos números reais provavelmente é a seguinte: "Se C é um conjunto não vazio de números reais e C está acotado superiormente, então, C tem uma cota superior mínima".

**Teorema:** Seja  $\mathbb N$  o conjunto dos números naturais. Mostrar que  $\mathbb N$  não está acotado superiormente. Temos:

H: seja  $\mathbb{N}$  o conjunto dos números naturais;

T: N não está cotado superiormente;

 $\sim T$ : N está acotado superiormente. Façamos:

H':  $(H \land \sim T)$  T': f

Demonstração: admitamos que  $\mathbb{N}$  esteja acotado superiormente; como  $\mathbb{N}$  é diferente do conjunto vazio, ele possui uma cota superior mínima a. Logo,

 $a \ge n$ , para qualquer n pertencente a  $\mathbb{N}$  (definição de cota superior mínima ou supremo – sup);

 $a \geq n+1$ , (igualmente, consequência do item anterior).

Ora, seja  $a \ge n+1$  para qualquer n natural e como n+1 pertence a  $\mathbb{N}$ , podemos escrever:  $a-1 \ge n$  para qualquer n natural, o que mostra ser o número a-1 também, uma cota superior de  $\mathbb{N}$ , o que entra em contradição com o fato admitido de ser a a cota superior mínima.

**Exemplo 10.** Para quaisquer a e b reais positivos, existe um número inteiro natural n pertencente a  $\mathbb N$  , tal que an>b. Temos:

 $H: a \in b \text{ reais positivos}, n \in \mathbb{N};$ 

 $T: an > b \sim T: an < b$ 

Façamos:

H':  $(H \land \sim T)$  T': f

Demonstração: consideremos o conjunto A dos "múltiplos positivos" de a, isto é:

 $\mathbf{A}=\{na\};$ ora, da hipótese (isto é, de  $\sim T),$  concluímos ser A majorado por b, donde existe  $s=\sup \mathbf{A}.$ 

Podemos, pois, escrever:

 $(\forall n \in \mathbb{N}), (n+1) \ a \leq s \Rightarrow na \leq s-a, \text{ o contradiz}$  o fato de ser  $s = \sup A$ .

# PRÓXIMO NÚMERO

A Matemática: suas origens, seu objeto e seus métodos. (Continuação)

## NOTÍCIAS

# Simpósio Nacional da Formação do Professor de Matemática

No período de 27 a 29 de setembro de 2013, a SBM e o PROFMAT realizarão em Brasília-DF, o 1º Simpósio Nacional da Formação do Professor de Matemática. O evento oferecerá um programa diversificado de atividades voltadas para a formação e atualização do professor de Matemática na Escola Básica, incluindo Conferências, Minicursos, Oficinas e Comunicações. O Simpósio propiciará, igualmente, um fórum para discussão de temas atuais e relevantes para a comunidade da Escola Básica. Maiores informações no endereço http://simposio.profmat-sbm.org.br.

# **NÚMEROS ATRASADOS**

Envie para cada Folhetim um selo de postagem nacional de 1º porte. Dentro de no máximo quatro semanas, contadas a partir da data de recebimento do seu pedido, você receberá os folhetins solicitados. OBS.: É permitida a reprodução total ou parcial deste Folhetim, desde que citada a fonte.