import pandas as pd
import pdb
import matplotlib.pyplot as plt

print 'carrega dados'
df = pd.read_csv('gapminder.tsv',sep ='\t')
#print df.head
print df.shape
print df.columns 	

print ''

print df.dtypes

print ''

print df.info()

print 'select collum'

df_country = df ['country']

print df_country.head() #show first five

print ''

print df_country.tail() #show 5 end

subset = df[['country', 'continent', 'year']]

print subset.head()

#print position
#df.loc[0]
#df.loc[0,1,99]
#def.loc
#or
#df.iloc[0]
#select colum
#df.ix[[0, 99, 999], [0, 3, 5]])

#print(df.groupby('year')['lifeExp'].mean())


#df.groupby(['year', 'continent'])[['lifeExp','gdpPercap']].mean()

#df.groupby('continent')['country'].nunique())

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
global_yearly_life_expectancy.plot()
#global_yearly_life_expectancy.show()
#plt.show()

print(df.groupby('continent')['country'].nunique())


#pdb.set_trace()
