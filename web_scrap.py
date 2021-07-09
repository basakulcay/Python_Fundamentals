import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html","html.parser")

soup = BeautifulSoup(webpage.content)
#print(soup)


Ratings_1 = soup.find_all(attrs={"class":"Rating"})


ratings=[]
for i in Ratings_1[1:]:
  i_float=float(i.get_text())
  ratings.append(i_float)

#plt.hist(ratings)
#plt.show()

Companies = soup.find_all(attrs={"class":"Company"})

company=[]
for j in Companies[1:]:
  j.get_text()
  company.append(j.get_text())

dictionary = {"Company": company, "Ratings": ratings}
df = pd.DataFrame.from_dict(dictionary, orient="columns")

mean_vals = df.groupby("Company").Ratings.mean()
#print(mean_vals)

largest = mean_vals.nlargest(10)
#print(largest)

Cocoa = soup.find_all(attrs={"class":"CocoaPercent"})
cocoa_perc=[]

for k in Cocoa[1:]:
  new_k=float(k.get_text().replace("%",""))
  cocoa_perc.append(new_k)
#print(cocoa_perc)

dictionary2 = {"Company": company, "Ratings": ratings, "CocoaPercentage":cocoa_perc}
df2 = pd.DataFrame.from_dict(dictionary2, orient="columns")
print(df2)

plt.scatter(df2.CocoaPercentage, df2.Ratings)
z = np.polyfit(df2.CocoaPercentage, df2.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(df2.CocoaPercentage, line_function(df2.CocoaPercentage), "r--")
plt.show()


