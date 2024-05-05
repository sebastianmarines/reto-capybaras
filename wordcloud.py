import pandas as pd
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')
text = " ".join(tweet for tweet in df.tweet)

text = text.lower()

stopwords_es = [
    "a", "al", "algo", "algún", "alguna", "algunas", "alguno", "algunos", "ante", "antes",
    "aquel", "aquella", "aquellas", "aquello", "aquellos", "aquí", "arriba", "así",
    "aunque", "bajo", "bastante", "bien", "cabe", "cada", "casi", "cierto", "ciertos",
    "como", "con", "conmigo", "contigo", "contra", "cual", "cuales", "cualquier", "cualquiera",
    "cuando", "de", "del", "demás", "dentro", "desde", "donde", "dos", "el", "él",
    "ella", "ellas", "ello", "ellos", "en", "encima", "entonces", "entre", "era",
    "erais", "eran", "eras", "eres", "es", "esa", "esas", "ese", "eso", "esos",
    "esta", "está", "estaba", "estabais", "estaban", "estabas", "estad", "estada", "estadas",
    "estado", "estados", "estáis", "estamos", "están", "estar", "estará", "estarán", "estarás",
    "estaré", "estaréis", "estaremos", "estaría", "estaríais", "estaríamos", "estarían", "estarías",
    "estas", "este", "esté", "estéis", "estemos", "estén", "estés", "esto", "estos",
    "estoy", "estuve", "estuviera", "estuvierais", "estuvieran", "estuvieras", "estuvieron", "estuviese",
    "estuvieseis", "estuviesen", "estuvieses", "estuvimos", "estuviste", "estuvisteis", "estuvo", "ex",
    "excepto", "fuera", "fueran", "fueras", "fueron", "fuese", "fueseis", "fuesen", "fueses",
    "fui", "fuimos", "fuiste", "fuisteis", "ha", "habéis", "había", "habíais", "habíamos",
    "habían", "habías", "habida", "habidas", "habido", "habidos", "habiendo", "habremos", "habrá",
    "habrán", "habrás", "habré", "habréis", "habría", "habríais", "habríamos", "habrían", "habrías",
    "hace", "haceis", "hacemos", "hacen", "hacer", "haces", "hacia", "hago", "hasta",
    "incluso", "intenta", "intentais", "intentamos", "intentan", "intentar", "intentas", "intento",
    "ir", "jamás", "junto", "juntos", "la", "lado", "las", "le", "lejos",
    "lo", "los", "luego", "mal", "más", "me", "menos", "mi", "mía",
    "mías", "mientras", "mio", "míos", "mis", "misma", "mismo", "mismos", "modo",
    "mucha", "muchas", "mucho", "muchos", "muy", "nada", "ni", "ningún", "ninguna",
    "ningunas", "ninguno", "ningunos", "no", "nos", "nosotras", "nosotros", "nuestra", "nuestras",
    "nuestro", "nuestros", "nunca", "o", "os", "otra", "otras", "otro", "otros",
    "para", "parecer", "pero", "poca", "pocas", "poco", "pocos", "podéis", "podemos",
    "poder", "podría", "podríais", "podríamos", "podrían", "podrías", "por", "porque", "primero",
    "puede", "pueden", "puedo", "pues", "que", "qué", "querer", "quién", "quienes",
    "quiere", "realizado", "se", "sea", "seáis", "seamos", "sean", "seas", "según",
    "ser", "será", "serán", "serás", "seré", "seréis", "seremos", "sería", "seríais",
    "seríamos", "serían", "serías", "señaló", "si", "sido", "siendo", "siempre", "sin",
    "sino", "sobre", "sois", "solamente", "solo", "somos", "soy", "su", "sus",
    "suya", "suyas", "suyo", "suyos", "tal", "tales", "también", "tampoco", "tan",
    "tanta", "tantas", "tanto", "tantos", "te", "tenéis", "tenemos", "tener", "tengo",
    "ti", "tiempo", "tiene", "tienen", "toda", "todas", "todavía", "todo", "todos",
    "tras", "tu", "tú", "tus", "tuya", "tuyo", "tuyos", "último", "un",
    "una", "unas", "uno", "unos", "usted", "ustedes", "va", "vais", "valor",
    "vamos", "van", "varias", "varios", "vaya", "veces", "ver", "vez", "vosotras",
    "vosotros", "voy", "y", "ya", "yo"
]

words = [word.replace(".","") for word in words]
words = [word for word in words if word not in stopwords_es]
words = [word for word in words if word not in ["les", "son", "sí","fue", "ahí", "dan", "pae", "ni", "mande", "vía", "hay"]]
words = [word for word in words if not word.isnumeric()]

freq = Counter(words)

wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(freq)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
