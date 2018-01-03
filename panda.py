import pandas as pd
import pdb

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
pdb.set_trace()
