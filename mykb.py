import pandas
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

KB={("точіння", "перевага", "універсальність"),
    ("точіння", "перевага", "продуктивність"),
    ("точіння", "перевага", "точність"),
    ("точіння", "перевага", "простий інструмент"),
    ("точіння", "недолік",  "нетехнологічність"),
    ("нарізання мітчиком", "перевага", "технологічність"),
    ("нарізання мітчиком", "недолік", "спеціальний інструмент")}
df = pandas.DataFrame(columns=["s","p","o"])
i=0
for s,p,o in KB:
    df.loc[i]={"s":s, "p":p, "o":o}
    i+=1
#df.to_csv('kb.csv', index=False)
csv_file_path = os.path.join(current_dir, 'kb.csv')

df = pandas.read_csv(csv_file_path)