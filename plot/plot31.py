import matplotlib.pyplot as plt


################
## Temperature with axes options
################
###### Plotting temperatures and changing xaxis
months = range(1, 13, 1)
temps = [-4,-4,2,10,18,22,24,23,18,10,0,-5]
plt.plot(months, temps)

# # ## Add axes, labels, and a title
# plt.title('Ave. high Temperature in Edmonton')
# plt.xlabel('Month')
# plt.ylabel('Degrees C')
# # #### Start axis at 1 to 12
# plt.xlim(1, 12)
# # # ### Change x axes labels
# # plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12))
# # #### Change x axes labels to custom labels
# plt.xticks((1,2,3,4,5,6,7,8,9,10,11,12),
#             ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

# # #### add/remove grid lines
# plt.grid()
# plt.plot(months, temps)
plt.show()