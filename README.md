<h1>Identificação de Fake News com classificação de texto</h1>
<h3>Contexto</h3>
<p>A democratização da internet trouxe à tona características como a produção de informação desenfreada. Ambientes virtuais como redes sociais tornaram-se prósperos à disseminação de notícias falsas devido a facilidade de compartilhamento de informação e dificuldade em identificar a veracidade de um grande volume de dados.</p>
<h3>Experimento</h3>
<p>Esta aplicação é um experimento para trabalhar com técnicas de classificação de texto vinculada à outras atividades acadêmicas, como o próprio projeto de mestrado.</p>
<p>O conceito de conteinerização em Docker contribui para pensar futuros algoritmos de maior complexidade e utilizar este experimento como uma parte modular deste projeto.</p>
<h3>Conjunto de dados</h3>
<p>Para esta aplicação, foi utilizado o dataset <a href="https://github.com/ViniciusNunes0/SIRENE-news">SIRENE-news</a> composto por 4.742 notícias.</p>
<h3>Pré-requisitos</h3>
<p>É necessário ter a plataforma <a href="https://www.docker.com/products/docker-desktop" target="_blank" rel="noopener noreferrer">Docker</a> instalada em sua máquina.</p>
<h3>Bibliotecas Instaladas</h3>
<p>nltk - tokenização e remoção de stopwords</p>
<p>scikit-learn - vetorização de palavras, treinamento do algoritmo e importação do classificador</p>
<p>pandas - criação de dataframe para a leitura do dataset </p>
<h3>Como Utilizar</h3>
<p>1. Abrir um shell de comando</p>
<p>2. Acessar a pasta raíz da aplicação</p>
<p>3. Executar o comando: docker-compose up</p>
<p><img src="images/1.docker.jpg/" /></p>
<p>4. O resultado da precisão será emitido</p>
<p><img src="images/2.classificador.jpg/" /></p>
<h3>Resultados e Discussão</h3>
<p>Utilizando o classificador Random Forest, foi possível obter uma precisão de 97.81% na classificação de notícias entre falsas e verdadeiras. Serão incorporadas mais técnicas de Processamento de Linguagem Natural ao código Python, este código servirá como um módulo para incorporar um algoritmo classificador mais robusto.</p>
<h3>Observação</h3>
<p>A proposta de exibir a variável "Precisão" na página em HTML não foi concretizada</p>
<p> </p>
<p><br /><br /><br /></p>
<p> </p>
