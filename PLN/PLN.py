import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ViniciusNunes0/SIRENE-news/master/noticias-sirene.csv', sep=';')
df = df[['noticia', 'classificacao']]
df = df.rename(columns={"noticia": "noticia", "classificacao": "label"})
df['label'] = df['label'].replace({0: 'true', 1: 'fake'})
df.head()
df.tail()   

x_train,x_test,y_train,y_test=train_test_split(df['noticia'], df['label'], test_size=0.25, random_state=42)

#parser monosintático
#pré-processamento de dados
tfidf_vectorizer = TfidfVectorizer(stop_words=stopwords.words('portuguese'),
        analyzer='word',
        ngram_range=(1, 1),
        lowercase=True,
        use_idf=True)

tfidf_train = tfidf_vectorizer.fit_transform(x_train) 
tfidf_test = tfidf_vectorizer.transform(x_test)

rf = RandomForestClassifier(random_state=0)
rf.fit(tfidf_train,y_train)

y_pred = rf.predict(tfidf_test)
score = accuracy_score(y_test,y_pred)
#print(f'Accuracy: {round(score*100,2)}%')
precisao = {round(score*100,2)}
