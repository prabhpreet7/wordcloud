import wikipedia
from wordcloud import WordCloud, STOPWORDS
import os
import numpy as np
from PIL import Image
import sys

curr_dir= os.path.dirname(__file__)
query= sys.argv[1]

def get_wiki(query):
    title= wikipedia.search(query)[0]
    page= wikipedia.page(title)
    return (page.content)

def create_cloud(text):
     stopwords=set(STOPWORDS)
    # mask = np.array(Image.open(os.path.join(curr_dir, "word.png")))
     wc= WordCloud(background_color='black', max_words=150,stopwords=stopwords)
     wc.generate(text)
     wc.to_file(os.path.join(curr_dir,query+'.png'))

create_cloud(str(get_wiki(query)))
