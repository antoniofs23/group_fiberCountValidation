import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('tractmeasures-mean_nodes.csv')
subjects = data.subjectID.unique()
tracts = data.structureID.unique()

streamCount = []
for sub in subjects:
    streamCount.append(list(data.loc[data['subjectID']==sub].StreamlineCount))

# convert to array for simple math    
st_count = np.array(streamCount)
#compute mean
stC_mean = np.mean(np.array(st_count),axis=0)
#compue standard deviation
stC_std = np.std(np.array(st_count),axis=0)


# plot individual subjects
for sub in streamCount:
    plt.plot(sub,'.',alpha=0.30)
#plot the mean
plt.bar(tracts,stC_mean)
plt.xticks(rotation='vertical')
plt.errorbar(tracts,stC_mean,3*stC_std,ecolor='k',capsize=5,fmt='none')
plt.ylabel('mean count')
plt.title('mean number of fibers across subjects')
plt.show() 
    
    
    