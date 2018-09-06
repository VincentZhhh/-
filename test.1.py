# from bs4 import BeautifulSoup
# import urllib.request
with open('城市字典的本地路径','r') as f:
    r = f.read()
    c = r.split()
    ci = [i.strip('市') for i in c]
# print(len(ci))

from xpinyin import Pinyin
p = Pinyin()
allcity = []
for i in ci:
    res = p.get_pinyin(i,show_tone_marks=True,splitter=' ')
    allcity.append(res)
# print(allcity)

from pandas import DataFrame,Series
import random
second = [i.split()[-1] for i in allcity]
frist = [i.split()[0] for i in allcity]

df_city = DataFrame([frist,second,ci]).T
df_city = df_city.rename(columns={0:'frist',1:'second',2:'name'})
# print(df_city)
df_city_g = df_city.groupby('frist')
dl = list(df_city_g.groups.keys())

print('输入城市名')
putt = input()
print('输入接龙次数')
time = input()
time = int(time)

def main():
    put = putt
    def bibao():
        nonlocal put
        for count in range(time):       
            inp = p.get_pinyin(put,show_tone_marks=True,splitter=' ').split()[-1]
            # print(inp)
            if inp in dl and count<time:
                reall = list(df_city_g.get_group(inp)['name'].values)
                re = random.sample(reall,1)[0]
                print(re)
                put = re                    
            else:
                print('no more..')
                break
    return bibao  
ff = main()
ff()
