import requests
import  lxml.html as lh
import pandas as pd

url = "http://www.worldometers.info/world-population/population-by-country/"
page=requests.get(url)
colmns=[]
doc=lh.fromstring(page.content)
tr_elements=doc.xpath('//tr')
col=[]

i=0
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    try:
        name=int(name)
    except:
        pass
    colmns.append(name)
    col.append((name,[]))

for j in range(1,len(tr_elements)):
    i=0
    T=tr_elements[j]
    if(len(T)!=12):
        break
    for k in T.iterchildren():
        data=k.text_content()
        try:
            data=data.replace("," or " %","")
            data=int(data)
        except:
            try:
                data=data.replace("," or " %","")
                data=float(data)
            except:
                pass
        col[i][1].append(data)
        i+=1


dict_1 = {title:column for title,column in col}
df = pd.DataFrame(dict_1) 
df = df.drop("#",1)
df.to_json("populationdata.json")
df.to_csv("populationdata.txt",index_label="ID")
