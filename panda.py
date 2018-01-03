import pandas as pd
import pdb
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

print df_countr.tail() #show 5 end

#pdb.set_trace()
