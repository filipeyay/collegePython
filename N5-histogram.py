import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib_venn import venn2
from faker import Faker

fake = Faker()
num_people = 10
names = [fake.name() for _ in range(num_people)]
score = np.random.randint(10, 50, size=num_people)

data = pd.DataFrame({'Name': names, 'Score': score})

data.to_csv('data.txt', index=False, sep='\t')

data_recovery = pd.read_csv('data.txt', sep='\t')

plt.figure(figsize=(10, 6))
plt.hist(data_recovery['Score'], bins=10,
         edgecolor='black')
plt.xlabel('Score')
plt.ylabel('Probability')
plt.title('Score Histogram')
plt.grid(True)
plt.show()

text = ' '.join(data_recovery['Name'])
wordcloud = WordCloud(width=800, height=400,
                      background_color='black').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Names')
plt.show()