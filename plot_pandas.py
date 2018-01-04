import pandas as pd
import pdb
import matplotlib.pyplot as plt
import seaborn as sns


anscombe  = pd.read_csv('anscombe.csv',sep =',')
#print(anscombe)

dataset_1 = anscombe[anscombe['dataset'] == 'I']
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']


# create the entire figure where our subplots will go
fig = plt.figure()
# tell the figure how the subplots should be laid out
# in the example below we will have
# 2 row of plots, each row will have 2 plots
# subplot has 2 rows and 2 columns, plot location 1
axesl = fig.add_subplot(2 , 2, 1)
# subplot has 2 rows and 2 columns, plot location 2
axes2 = fig.add_subplot(2 , 2, 2)
# subplot has 2 rows and 2 columns, plot location 3
axes3 = fig.add_subplot(2 , 2, 3)
# subplot has 2 rows and 2 columns, plot location 4
axes4 = fig.add_subplot(2 , 2, 4)


# add a plot to each of the axes created above
axesl.plot(dataset_1['x'], dataset_1['y'], 'o')
axes2.plot(dataset_2['x'], dataset_2['y'], 'o')
axes3.plot(dataset_3['x'], dataset_3['y'], 'o')
axes4.plot(dataset_4['x'], dataset_4['y'], 'o')

# add a small title to each subplot
axesl.set_title("dataset_l")
axes2.set_title("dataset_2")
axes3.set_title("dataset_3")
axes4.set_title("dataset_4")
# add a title for the entire figure
fig.suptitle("Anscombe Data")

plt.show()

#pdb.set_trace()

