import pandas as pd

world_cup={'Team':['West Indies','West indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','Insia','Australia'],
           'Rank':[7,7,2,1,6,4,1,1,1,2,1],
           'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]}
df=pd.DataFrame(world_cup)
print(df)
print(df.groupby('Team').groups)
print(df.groupby('Team','Rank').groups)

grouped=df.groupby('Team')
for name,group in grouped:
    print(name)


grouped = df.groupby('Team')
print(grouped.get_group('India'))

import pandas
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
           'ICC_rank':[2,3,7,8,4],
           'World_champions_Year':[2011,2015,1979,1992,1996],
           'Points':[874,787,753,673,855]}

chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
           'ICC_rank':[1,5,9],
           'Points':[895,764,656]}

df1=pandas.DataFrame(world_champions)
df2=pandas.DataFrame(chokers)

import pandas
world_champions={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
           'ICC_rank':[2,3,7,8,4],
           'World_champions_Year':[2011,2015,1979,1992,1996],
           'Points':[874,787,753,673,855]}

chokers={'Team':['South Africa','New Zealand','Zimbabwe'],
           'ICC_rank':[1,5,9],
           'Points':[895,764,656]}

df1=pandas.DataFrame(world_champions)
df2=pandas.DataFrame(chokers)
print(pandas.merge(df1,df2,on='Team',how='left'))

print(pandas.concat([df1,df2],axis=1))
print(df1.append(df2))
print(pandas.concat([df1,df2]))
print(pandas.concat([df1,df2],axis=1))




import pandas
champion_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
           'ICC_rank':[2,3,7,8,4],
           'World_champions_Year':[2011,2015,1979,1992,1996],
           'Points':[874,787,753,673,855]}

match_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
             'World_cup_played':[11,10,11,9,8],
             'ODIs_played':[733,988,712,679,662]}


df1=pandas.DataFrame(champion_stats)
df2=pandas.DataFrame(match_stats)

print(df1)
print(df2)
print(pandas.merge(df1,df2,on='Team'))