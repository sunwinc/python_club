import matplotlib.pyplot as plt

# #set line width
# plt.rcParams['lines.linewidth'] = 2
# #set font size for titles
# plt.rcParams['axes.titlesize'] = 16
# #set font size for labels on axes
# plt.rcParams['axes.labelsize'] = 16
# #set size of numbers on x-axis
# plt.rcParams['xtick.labelsize'] = 10
# #set size of numbers on y-axis
# plt.rcParams['ytick.labelsize'] = 10
# #set size of ticks on x-axis
# plt.rcParams['xtick.major.size'] = 5
# #set size of ticks on y-axis
# plt.rcParams['ytick.major.size'] = 5
# #set size of markers
# plt.rcParams['lines.markersize'] = 10
# #set number of examples shown in legends
# plt.rcParams['legend.numpoints'] = 1
# #set the font size globally
# plt.rcParams['xtick.labelsize']=20
# plt.rcParams['ytick.labelsize']=20
# plt.rcParams['axes.labelsize'] = 26 
# plt.rcParams['axes.titlesize'] = 26 
# plt.rcParams["figure.figsize"] = (15,10)

########################
## Plotting many lines 
########################
nVals = []
linear = []
quadratic = []
cubic = []
exponential = []

for i in range(0, 30):
    nVals.append(i)
    linear.append(i)
    quadratic.append(i**2)
    cubic.append(i**3)
    exponential.append(1.5**i)

# #### Plotting one line
# plt.plot(nVals, linear)

# ##### order of data points matters
testSamples = [0,5,3,6,15,2,1,4,25,20,7,21,22,23,9,8,24,10,12,11]
testValues =  [0,25,9,36,225,4,1,16,625,400,49,441,484,529,81,64,576,100,144,121]
# plot connects the points
# plt.plot(testSamples, testValues)
# scatter plot does not connect the points
# plt.scatter(testSamples, testValues)

# ##### Plotting many lines
# plt.plot(nVals, linear)
# plt.plot(nVals, quadratic)
# plt.plot(nVals, cubic)
# plt.plot(nVals, exponential)

# ###### Plotting two lines on one plot
plt.figure('expo')
plt.plot(nVals, exponential)
plt.figure('lin')
plt.plot(nVals, linear)
plt.figure('quad')
plt.plot(nVals, quadratic)
plt.figure('cube')
plt.plot(nVals, cubic)
newExpo = []
for i in range(30):
    newExpo.append(1.6**i)
plt.figure('expo')
plt.plot(nVals, newExpo)
plt.show()

