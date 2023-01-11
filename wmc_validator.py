import json 
import os
import numpy as np
import matplotlib.pyplot as plt

# set project directory (where all subject directories are)
project_dir = '/Users/antonio/Desktop/proj-6396777a6881d56fbfcd0bbc/'
n = 21 # number of subjects [hardcoded for now]
# get all subject directories -> first output is directory name
temp_dir = [direct[0] for direct in os.walk(project_dir)]

# only keep dir with the roi subdirectory as there are nested folders in project to subject roi dir
sub_dir = [direct for direct in temp_dir if 'dt-neuro-wmc.tag' in direct]

#remove tract subdirectory
print(sub_dir[1].split('/'))

tract_fiber_count = []
for subs in sub_dir:
    test_case = subs.split('/')
    if 'tracts' in test_case:
        continue
    else:
        # load inputs from _info.json
        with open(subs+'/'+'_info.json') as info_json:
            info = json.load(info_json)
            metadata = info['meta']['tracts'] 
            count = [c['count'] for c in metadata]
    tract_fiber_count.append(count)

# keep track of the tract names
trk_names = [tc['name'] for tc in metadata]
# mean of all counts across subjects
all_count = np.array(tract_fiber_count)
mean_count = np.mean(all_count,axis=0)   
std_count = np.std(all_count,axis=0)#/np.sqrt(n)

# plot the sum       
for sub in all_count:
    plt.plot(trk_names[1:],sub[1:],'o',alpha=0.50)
plt.bar(trk_names[1:],mean_count[1:])
plt.xticks(rotation='vertical')
plt.errorbar(trk_names[1:],mean_count[1:],std_count[1:],ecolor='k',fmt='none')
plt.ylabel('mean count')
plt.title('mean number of fibers across subjects')
plt.show()  