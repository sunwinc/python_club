import matplotlib.pyplot as plt

###################################
## Temperatures for many cities 
###################################

##### Plotting multiple lines with labels
months = range(1, 13, 1)
edm_high = [-4,-4,2,10,18,22,24,23,18,10,0,-5]
plt.plot(months, edm_high, label = 'Edmonton high')
edm_low = [-13,-14,-8,-1,6,11,13,12,6,0,-9,-13]
plt.plot(months, edm_low, label = 'Edmonton low')
# Add labels and title
plt.title('Ave. Temperatures')
plt.xlabel('Month')
plt.ylabel('Degrees C')
# Change x axis labels to custom labels
plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12),
          ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

plt.legend(loc = 'best', fontsize=16) # position it automatically
plt.show()