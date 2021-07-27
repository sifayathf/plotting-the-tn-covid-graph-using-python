import pandas as pd
import os
import re
import natsort
import matplotlib.pyplot as plt

# to get file list
filelist=[]
for root, dirs, files in os.walk(r'C:\Users\SifayathAhmedF\Documents\pythonclassfiles'):    
     print(files)
     filelist.append(files)
filelist=filelist[0]


# to get datafile list 
finalfilelist=[]
filelist1=[]
for file in filelist:
     filelist1=re.match("^datafile.*",file)
     if filelist1 is not None:
          print(filelist1.group(0))
          finalfilelist.append(filelist1.group(0))

     
# to add full path to filename
str1="""C:\\Users\\SifayathAhmedF\\Documents\\pythonclassfiles\\"""
paths= ["".join([str1,x])for x in finalfilelist]

# to sort paths in ascending order of filenames

paths = natsort.natsorted(paths)

# pandas to read excel and store it in a set using     
dfs = {}
for path in paths:
    df=pd.read_excel(path)
    #to get only the needed columns     
    df1=df.iloc[:, 1:3]
    dfs[path]=df1

# to merge dataframe column wise
for i in range(1,len(paths),1):
     if(i==1):
          result=dfs[paths[0]]
     result=pd.concat([result,dfs[paths[i]]],axis=1, join="inner")

# to remove duplicated columns in dataframe

result = result.loc[:,~result.columns.duplicated()]


# to upload the dataframe row into list

#datalist=result[result.District=='Coimbatore'].values.tolist()

datalist=[]
datalistdict={}  # this is a dict
for district in result.District:
        for data in (result[result.District==district].values.tolist()):
                data.remove(district)
                datalist.append(data)
                datalistdict.update({district:data})

for key,value in datalistdict.items():
     print(key,value)
     data1=[]
     for i in range(1,len(value)):
        data1.append(value[i]-value[i-1])
     plt.plot(data1,'*-')


# datalist is actually a list of list so have to get the data. [[265029, 269614, 272118, 274734, 'Chennai', 277300, 283436, 286569, 290364, 294073, 297814, 301541, 305570, 309899, 314074, 318614, 323452, 328520, 333804, 345966, 352260, 358573, 364081, 370596, 377042, 383644, 390589, 397498, 404733,
# 412505, 419261, 425603, 432344, 438391, 444371, 450267, 456496, 462448, 468262, 473671, 478710, 483757, 487691, 491197, 493881]]

#for data in datalist:
#    pass

#data.remove('Coimbatore')

# toget the difference

#data1=[]
#for i in range(1,len(data)):
#    data1.append(data[i]-data[i-1])
     

# to display the district results in a chart

#plt.plot(data1,'*-')
plt.show()











