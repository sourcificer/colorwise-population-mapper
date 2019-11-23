import requests
import lxml.html as lh
import pandas as pd

def population_scrapper(fetch_url):
    """
        using the url provided fetches
        population of all the countries in the world
        and stores the information in txt and csv.
        (**To do: Make it more compatiable with other
                population displaying websites)
    """
    url = fetch_url
    page = requests.get(url)
    colmns = []
    doc = lh.fromstring(page.content)
    tr_elements = doc.xpath('//tr')
    col = []

    i = 0
    for t in tr_elements[0]:
        i += 1
        name = t.text_content()
        try:
            name = int(name)
        except:
            pass
        colmns.append(name)
        col.append((name, []))

    for j in range(1, len(tr_elements)):
        i = 0
        T = tr_elements[j]
        if(len(T) != 12):
            break
        for k in T.iterchildren():
            data = k.text_content()
            try:
                data = data.replace("," or " %", "")
                data = int(data)
            except:
                try:
                    data = data.replace("," or " %", "")
                    data = float(data)
                except:
                    pass
            col[i][1].append(data)
            i += 1


    dict_1 = {title: column for title, column in col}
    df = pd.DataFrame(dict_1)
    df = df.drop("#", 1)
    df.to_csv("populationdata.txt", index_label="ID")
    df.to_csv("populationdata.csv", index_label="ID")
