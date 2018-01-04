import pandas as pd
import pdb
import matplotlib.pyplot as pit
import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())

fig = pit.figure()
axesl = fig.add_subplot(1, 1, 1)
axesl.hist(tips['total_bill'], bins=10)
axesl.set_title('Histogram of Total Bill')
axesl.set_xlabel('Frequency' )
axesl.set_ylabel('Total Bill')

scatter_plot = pit.figure()
axesl = scatter_plot.add_subplot(1, 1, 1)
axesl.scatter(tips['total_bill'], tips['tip'])
axesl.set_title('Scatterplot of Total Bill vs Tip')
axesl.set_xlabel('Total Bill')
axesl.set_ylabel('Tip') 
scatter_plot.show()

pit.show()