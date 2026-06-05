![](_page_0_Picture_1.jpeg)

Folhetim Educ. Mat., Feira de Santana, Ano 17, N´umero 162, set./out., 2011 ISSN 1415-8779

Este Folhetim ´e um ve´ıculo de divulga¸c˜ao, circula¸c˜ao de ideias e de est´ımulo ao estudo e `a curiosidade intelectual. Dirige-se a todos os interessados pelos aspectos pedag´ogicos, filos´oficos e hist´oricos da Matem´atica. Pretende construir uma ponte para unir os que est˜ao pr´oximos e os que est˜ao distantes.

Dando continuidade `a transcri¸c˜ao das notas intituladas "A Matem´atica: suas origens, seu objeto e seus m´etodos - Parte I", de autoria do professor Carloman, neste n´umero, veremos a Axiom´atica dos N´umeros Reais. Em seguida, retornamos aos princ´ıpios que devem reger qualquer axiom´atica: o princ´ıpio de consistˆencia, o princ´ıpio de completude e o princ´ıpio de independˆencia.

E poss´ıvel axiomatizar cada setor da ´ Matem´atica de tal maneira que se possa dessa axiomatiza¸c˜ao deduzir a totalidade infinita de suas proposi¸c˜oes? Ao responder esta indaga¸c˜ao, o professor Carloman trata, inevitavelmente, do Teorema de G¨odel. Consequentemente, a classe das proposi¸c˜oes indecid´ıveis ´e outro conceito discutido nesta edi¸c˜ao do Folhetim.

Carloman Carlos Borges (UEFS) - in memoriam

In´acio de Sousa Fadigas (UEFS)

Marcos Grilo Rosa (UEFS)

Traz´ıbulo Henrique (UEFS)

A Matem´atica: suas origens, seu objeto e seus m´etodos (continua¸c˜ao)

Carloman Carlos Borges

# 2.2 Axiom´atica (continua¸c˜ao)

Finalmente, como ´ultimo exemplo, daremos a Axiom´atica abaixo:

iv) Axiom´atica dos N´umeros Reais

Esta axiom´atica estabelece inicialmente, a ideia de corpo, depois, a de corpo ordenado completo. Em um bom curso de An´alise mostra-se como TODAS as propriedades dos n´umeros reais s˜ao logicamente decorrentes desses axiomas.

Um corpo ´e um conjunto K, com duas opera¸c˜oes:

$$s: K \times K \longrightarrow K$$

$$p: K \times K \longrightarrow K$$

respectivamente, denominadas de adi¸c˜ao (a qual associa a cada par de elementos x, y ∈ K, sua soma x + y ∈ K) e de multiplica¸c˜ao (a qual associa a cada par de elementos x, y ∈ K, seu produto x.y ou simplesmente xy ∈ K ).

- I) Axiomas da Adi¸c˜ao
- A1. Associatividade: quaisquer que sejam x, y, z pertencentes a K, tem-se (x + y) + z = x + (y + z).
- A2. Comutatividade: quaisquer que sejam x, y pertencentes a K, tem-se x + y = y + x.
- A3. Elemento Neutro: existe 0 pertencente a K, tal que x + 0 = x, qualquer que seja x pertencente a K. Ao elemento 0, chama-se zero.
- A4. Sim´etrico: todo elemento x pertencente a K possui um sim´etrico −x pertencente a K de modo que x + (−x) = 0.
  - II) Axiomas da Multiplica¸c˜ao
- M1. Associatividade: dados x, y, z pertencentes a K, tem-se (xy)z = x(yz).
  - M2. Comutatividade: quaisquer que sejam x, y pertencentes

a K, tem-se xy = yx.

M3. Elemento Neutro: existe 1 pertencente a K tal que 1 difere de zero e x.1 = x, qualquer que seja x pertencente a K. Este elemento 1 chama-se um.

M4. Inverso Multiplicativo: para todo x diferente de zero, em K, existe um inverso  $x^{-1}$ , tal que  $x.x^{-1} = 1$ .

Ligando estas duas operações há o importante axioma:

D1. Axioma da Distributividade: Dados x, y, z em K, tem-se x(y+z) = xy + xz.

Antes da introdução de corpo ordenado, podemos apresentar as definições de: a) diferença (x-y): para x,y em K, x-y=x+(-y); b) quociente  $(\frac{x}{y})$ : se x,y são elementos de K e se y difere de zero,  $\frac{x}{y}=xy^{-1}$ .

Introduziremos, agora, a ideia de corpo ordenado, através da definição: um par ordenado (K, P), onde K é um corpo e P é um subconjunto de K, denomina-se de corpo ordenado quando, e somente quando, são verificadas as condições abaixo:

P1. Lei de Tricotomia: Para todo número x pertencente a K se cumpre uma, e somente uma, das seguintes alternativas: ou x = 0 ou x pertence a P ou -x pertence a P. O conjunto P é chamado de conjunto dos elementos positivos.

P2. Se x e y pertencem a P, então x + y pertence a P e x.y pertence a P.

As seguintes definições são válidas:

- i) x > y, se x y pertence a P;
- ii) x < y, se y > x;
- iii)  $x \ge y$ , se x > y ou x = y;
- iv)  $x \le y$ , se x < y ou x = y.

A desigualdade x > y lê-se "x é maior do que y" e x < y lê-se "x é menor do que y". Desta forma, o conjunto P é o conjunto dos elementos de K maiores do que zero. Finalmente, procuremos introduzir o conceito de corpo ordena-

do completo, dando, primeiro, as definições:

- i) O conjunto A é limitado superiormente quando, e somente quando, existe k pertencente a K tal que para todo x pertencente a A, tem-se  $x \leq k$ . Ao elemento k dá-se o nome de um *limitante superior* do conjunto A.
- ii) Seja K um corpo ordenado e A um subconjunto de K, A não-vazio. Então dizemos que o elemento s pertencente a K é supremo de A, quando, e somente quando:
  - a)  $x \leq s$ , para qualquer x pertencente a A.
- b) para cada k pertencente a K, k < s, existe um x' pertencente a A tal que k é menor que x'.

Com estas definições, estamos em condições de definir corpo ordenado completo: um corpo ordenado K é completo quando, e somente quando, todo subconjunto A de K, A conjunto não-vazio e limitado superiormente, possui supremo.

Os axiomas mencionados acima poderiam ser designados por axiomas operacionais de corpo K, pois deles decorrem todas as propriedades do corpo K, o qual pode ser identificado como o corpo ordenado completo  $\mathbb{R}$ , para o qual postulamos:

Existe um corpo ordenado completo,  $\mathbb{R}$ , chamado o corpo dos números reais.

A este postulado de existência, alguns autores chamam de axioma fundamental da Análise Matemática.

Voltaremos a falar, agora, acerca dos princípios que devem reger qualquer axiomática, os quais são os seguintes:

- a) princípio de consistência ou da não-contradição;
- b) princípio de ser completo:
- c) princípio de independência.

Cada princípio mencionado impõe uma condição, à qual nenhuma axiomática pode fugir, deixando, portanto, de ser arbitrária. Assim, pelo princípio (a), uma axiomática não pode apresentar axiomas que sejam contraditórios entre si, isto é, eles não devem contradizer-se uns com os outros; ainda, de uma mesma axiomática não se deve deduzir dois teoremas, sendo um a negação do outro.

## NEMOC - NÚCLEO DE EDUCAÇÃO MATEMÁTICA OMAR CATUNDA

Folhetim Educ. Mat., Feira de Santana, Ano 17, Número 162, set./out. 2011 - Editores: Inácio, Grilo e Trazíbulo - Digitação: Josenildes Oliveira Venas Almeida e Manoel Aquino dos Santos - Editoração: Evandro Vaz e Nivaldo Assis - Impressão: Imprensa Gráfica Universitária - Periodicidade: bimestral - Tiragem: 1.500 exemplares - Distribuição gratuita - Endereço: Avenida Transnordestina s/n, Módulo Prof. Carloman Carlos Borges, bairro Novo Horizonte, Feira de Santana, BA, Brasil. CEP 44.036-900. - Telefone: (75)3161-8115 - Fax: (75)3161-8086 - E-mail: nemoc@uefs.br - Home-Page: www.uefs.br/nemoc

Por exemplo, na Geometria de Euclides, n˜ao pode ser aceito o axioma "por um ponto exterior a uma reta dada, pode-se passar mais de uma reta paralela `a reta dada", pois, claramente, ele seria contradit´orio com o famoso Axioma de Paralelismo, mencionado no Folhetim 161, p.3, quando tratamos da axiom´atica da geometria plana. Igualmente, n˜ao pode ser aceito o teorema "a soma dos ˆangulos internos de qualquer triˆangulo ´e menor que 180◦", pois ele entraria em conflito com o conhecido teorema de que "a soma dos ˆangulos internos de qualquer triˆangulo ´e igual a 180◦".

A condi¸c˜ao (b), isto ´e, da axiom´atica ser completa, significa que, de duas proposi¸c˜oes contradit´orias quaisquer elaboradas exclusivamente dentro da axiom´atica considerada, uma ao menos pode ser provada dentro da mesma axiom´atica.

A condi¸c˜ao (c) - condi¸c˜ao de independˆencia - n˜ao deve fazer parte de uma mesma axiom´atica um "axioma" que possa ser provado com base nos outros axiomas, pois, neste caso, n˜ao seria um axioma e sim um teorema. Assim, o Princ´ıpio da Boa Ordena¸c˜ao, que afirma que todo subconjunto n˜ao-vazio de n´umeros naturais possui um elemento m´ınimo, decorre do Princ´ıpio da Indu¸c˜ao Completa (ver Folhetim n.161, p.2). Entretanto, pode-se demonstrar o Princ´ıpio de Indu¸c˜ao Completa, que passaria a ser um teorema, admitindo-se o Princ´ıpio da Boa Ordena¸c˜ao como um axioma. Esta exigˆencia, todavia, n˜ao ´e t˜ao forte como a apresentada pelas outras duas condi¸c˜oes e, `as vezes, por simplicidade, admite-se numa mesma axiom´atica a viola¸c˜ao dessa condi¸c˜ao.

O conhecimento ´e a tradu¸c˜ao conceitual de uma realidade concreta que existe independente de nossas ideias e de vontade; por´em, isto n˜ao significa que o homem deixa de modificar a realidade que lhe cerca, enriquecendo-a com a aplica¸c˜ao desse mesmo conhecimento. E justamente na interdependˆencia entre o su- ´ jeito cognoscente e a realidade objetiva, onde devemos procurar a fonte da vitalidade do conhecimento humano. E ´e nesta interdependˆencia que se forma, por assim dizer, uma experiˆencia, uma "pr´atica", a qual serve de crit´erio superior da verdade. Evidentemente, nas ciˆencias formais como a Matem´atica, se desejarmos verificar a veracidade de um teorema, devemos estud´a-lo face `a axiom´atica donde ele proveio: ele deve ser uma consequˆencia l´ogica dos axiomas e, al´em disto, uma verdade necess´aria. Consideremos a proposi¸c˜ao: "Todos os homens s˜ao mortais". Como saber que ´e uma proposi¸c˜ao verdadeira? E claro que ´ esta proposi¸c˜ao ´e considerada verdadeira porque, na realidade, todos os homens s˜ao mortais. Aqui, existe a concordˆancia do pensamento com a realidade objetiva; trata-se, portanto, de uma verdade real, material. Os axiomas matem´aticos n˜ao podem ser totalmente arbitr´arios, embora existam muitas op¸c˜oes para a sua escolha, a qual ´e guiada, em ´ultima instˆancia, pelos fatos experimentais. Ao admitir-se a total arbitrariedade dos axiomas - seria inexplic´avel as grandes aplica¸c˜oes da Matem´atica; tal arbitrariedade significaria uma separa¸c˜ao completa entre a forma e o conte´udo; no processo de abstra¸c˜ao, no processo de uma dedu¸c˜ao matem´atica, evidentemente, o pensamento deve operar com formas, e a corre¸c˜ao formal, a´ı, deve predominar; por´em, a dedu¸c˜ao e a abstra¸c˜ao revelam apenas aspectos do pensamento em seus variados movimentos de apreens˜ao da realidade; neste aspecto - quando est´a deduzindo logicamente - o pensamento negligencia o conte´udo, apegando-se `a forma; mas essa "elimina¸c˜ao" do conte´udo ´e parcial e momentˆanea, pois, aqui, trata-se t˜ao somente de uma etapa, entre outras, de sua atividade: a abstra¸c˜ao. E´ muito dif´ıcil justificar a existˆencia de formas puras e eternas; ali´as, existir˜ao, de fato, tais formas?

Coisa similar ao que acabamos de expor acontece com a gram´atica, no sentido de que ela estuda a corre¸c˜ao da frase de conformidade com determinadas regras, sem preocupar-se com o seu conte´udo; por´em, uma gram´atica que estudasse apenas a corre¸c˜ao formal das frases sem qualquer conte´udo objetivo - n˜ao seria levada a s´erio por nenhuma pessoa interessada em transformar a linguagem no seu meio de comunica¸c˜ao com os seus semelhantes.

E falsa, tamb´em, a tese de Poincar´e de que a Geo- ´ metria Euclidiana ´e mantida por motivos de comodidade; a este respeito, vejamos o que escrevem A. N. Kolmogorov e outros matem´aticos sovi´eticos: "O famoso matem´atico Poincar´e afirmou h´a algum tempo que a elei¸c˜ao de uma ou outra geometria estava ditada somente por motivos de simplicidade ou 'economia de pensamento' ... Sobre esta frase, Poincar´e assegurou que se abandonaria antes a lei da propaga¸c˜ao retil´ınea da luz e n˜ao a Geometria Euclidiana, pois esta ´e 'mais simples'. Contudo, Poincar´e morreu trˆes anos antes de que a teoria da relatividade fosse finalmente desenvolvida; e nesta sucede precisamente o contr´ario: abandona-se a Geometria Euclidiana, conservando em troca a lei da propaga¸c˜ao da luz, ainda que em forma generalizada: a luz se propaga em linhas geod´esicas".

Como j´a vimos em n´umeros anteriores, foram os gregos os primeiros a introduzirem na Matem´atica, a axiom´atica e, com ela, as chamadas demonstra¸c˜oes. A Geometria de Euclides, escrita 300 anos antes de Cristo, exerceu poderosa influˆencia entre grandes pensadores da humanidade durante dois milˆenios, pois partindo de poucos axiomas - sua verdade estava acima de qualquer d´uvida - ela criava a possibilidade

de deduzir-se destes uma s´erie inesgot´avel de teoremas, isto ´e, de verdades provadas. Ora, como as verdades dos axiomas euclidianos eram aceitas ou melhor, eram tidas como "verdades auto-evidentes", verdades, ali´as, plenamente justificadas pela experiˆencia di´aria do homem, ent˜ao a consistˆencia rec´ıproca de todos os seus teoremas est´a plenamente assegurada. A Geometria de Euclides era o exemplo de um conhecimento cient´ıfico irrefut´avel; inclusive, alguns fil´osofos transformaram os seus axiomas, todos eles sugeridos pelas necessidades pr´aticas do homem em sua luta pela sobrevivˆencia (necessidades postas pela agrimensura, astronomia, etc.), em verdades eternas, pr´e-existentes no esp´ırito humano, irrevog´aveis porque produto da intui¸c˜ao pura. Da aceita¸c˜ao da Geometria de Euclides como a melhor sistematiza¸c˜ao de uma parte do conhecimento humano, surgiu a indaga¸c˜ao: ´e poss´ıvel axiomatizar outros ramos do conhecimento?

Focalizaremos nossa aten¸c˜ao sobre a pergunta mais particular: ´e poss´ıvel axiomatizar cada setor da Matem´atica de tal maneira que se possa dessa axiomatiza¸c˜ao deduzir a totalidade infinita de suas proposi¸c˜oes? A resposta positiva a tal pergunta se transformou em uma ideia fascinante para muitos eminentes matem´aticos. O grande matem´atico Hilbert ao adot´a-la, cria ser exequ´ıvel, ap´os a total formaliza¸c˜ao da Matem´atica, mostra a inexistˆencia de qualquer contradi¸c˜ao. Em seguida a Hilbert, muitos outros eminentes matem´aticos dele se tornaram disc´ıpulos; por´em o extraordin´ario sonho foi desfeito em 1931, quando do surgimento do artigo Sobre as proposi¸c˜oes indecid´ıveis dos Principia Mathematica e Sistemas Correlatos. Seu autor: o jovem matem´atico Kurt G¨odel, ent˜ao com apenas 25 anos. Alguns resultados do Teorema de G¨odel:

- a) nenhum sistema que englobe a aritm´etica pode demonstrar a sua pr´opria consistˆencia;
- b) ´e imposs´ıvel estabelecer a consistˆencia de in´umeros sistemas dedutivos, dentro deles mesmos.

Os resultados do Teorema de G¨odel mostram que:

- i) em sistemas dedutivos de maior interesse, existe incompatibilidade entre a completude e a consistˆencia: um sistema desse tipo se for consistente, n˜ao ´e completo;
- ii) tais sistemas n˜ao podem conter todas as verdades, salvo se deixarem demonstr´aveis algumas falsidades;
- iii) n˜ao se pode identificar a verdade matem´atica `a demonstrabilidade, pois, segundo G¨odel, h´a verdades indemonstr´aveis.

Assim, importantes setores da Matem´atica, mesmo formalizados, n˜ao estar˜ao livres de contradi¸c˜oes internas; n˜ao se pode exaurir nenhum ramo da Matem´atica, com base em um sistema de axiomas, pois isto, por isso mesmo, provoca quest˜oes imposs´ıveis de serem respondidas dentro desse sistema de axiomas. Na Aritm´etica, por exemplo, ´e imposs´ıvel a investiga¸c˜ao de todas as rela¸c˜oes rec´ıprocas entre os n´umeros inteiros, com base em um ´unico sistema de axiomas; dada uma determinada f´ormula, dentro de uma axiom´atica determinada, n˜ao existe, em geral, uma maneira de mostr´a-la que ela pode ser deduzida dos axiomas estabelecidos: existe, assim, dada uma axiom´atica, dentro dela, a classe das proposi¸c˜oes indecid´ıveis; perde-se, assim, o sonho de tornar a Matem´atica uma obra acabada, sonho alimentado com tanto entusiasmo pelos formalistas liderados por David Hilbert (1862-1943); por´em, o Teorema de G¨odel enche de alegria e entusiasmo todos aqueles esp´ıritos abertos a novas investiga¸c˜oes e que enxergam na verdade algo dinˆamico e nunca completamente acabado.

Dada uma rela¸c˜ao R dentro de uma determinada axiom´atica, se ela n˜ao for verdadeira - isto ´e, se ela n˜ao puder ser demonstrada - ela n˜ao ´e, necessariamente, falsa; pode acontecer que os axiomas estabelecidos n˜ao permitam demonstrar nem R, nem n˜ao R; tais rela¸c˜oes s˜ao chamadas, dentro da axiom´atica considerada, de indecid´ıveis.

A Matem´atica: suas origens, seu objeto e seus m´etodos. (Continua¸c˜ao)

## Profmat

A UEFS aderiu, recentemente, ao Mestrado Profissional em Matem´atica em Rede Nacional - PROF-MAT. O programa ´e coordenado pela SBM. A UEFS ofertar´a 20 vagas em 2012 e para maiores informa¸c˜oes, acesse o site: www.profmat-sbm.org.br

Envie para cada Folhetim um selo de postagem nacional de 1<sup>o</sup> porte. Dentro de no m´aximo quatro semanas, contadas a partir da data de recebimento do seu pedido, vocˆe receber´a os folhetins solicitados. OBS.: E permitida a reprodu¸c˜ao total ou parcial deste Fo- ´ lhetim, desde que citada a fonte.