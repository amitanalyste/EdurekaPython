import pandas as pd
dataset=pd.read_csv("AllCountries.csv")
print(dataset.shape)


import pandas as pd
dataset=pd.read_csv("AllCountries.csv")
print(dataset.dtypes)


import pandas as pd
dataset=pd.read_csv("AllCountries.csv")
print(dataset.head(5))


import pandas as pd
dataset=pd.read_csv("AllCountries.csv")
print(dataset.describe())


import pandas as pd
dataset=pd.read_csv("AllCountries.csv")
selected_data=dataset.loc[:,['Country','LandArea']]
for i in selected_data.itertuples():
    if i[2]>2000:
        print(i)



import pandas
import numpy
import matplotlib.pyplot as plt
plt.figure(figsize=(50,50))
dataset=pandas.read_csv("AllCountries.csv")
selected_data=dataset.loc[:,['Country','GDP','BirthRate']]
x=numpy.array(selected_data["GDP"])
y=numpy.array(selected_data['BirthRate'])
print(x,y)
plt.scatter(x,y)
plt.xlim(0,20000)
plt.show()



import pandas
import matplotlib.pyplot as plt
plt.figure(figsize=(50,50))
dataset=pandas.read_csv("AllCountries.csv")
selected_data=dataset.loc[:,['Country','GDP','BirthRate']]
sorted_data=selected_data.sort_index(by='GDP',ascending=False)
selected_sorted_data=sorted_data.iloc[:10]print(selected_sorted_data)
plt.pie(selected_sorted_data['GDP'],labels=selected_sorted_data['Country'])
plt.show()





