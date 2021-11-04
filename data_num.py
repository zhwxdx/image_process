import os
path='/home/y00/data/20210924'
path1='gray'
path2='cam0'
path3='cam1'
files=os.listdir(path)
#print(files)
def statistic():
   result=[]
   for file in files:
      if file.endswith('.txt'):
         continue
      data_path=os.path.join(path,file)
      cam0_path=os.path.join(data_path,path1,path2)
      # cam1_path=os.path.join(data_path,path1,path3)
      data_cam0_num= len(os.listdir(cam0_path))
      result.append(str(file)+'\t'+str(data_cam0_num)+'\n')
   return result
def return_key(s):
   a=s.split('\t')[-1]
   a=int(a)
   return a
def num_sort(result):
   result.sort(key=return_key)
   return result
result=statistic()
num_sort(result)
# print(result)                                                  result.sort(key=return_key)
with open(path+'/data_num.txt','a') as f:
   f.writelines(result)
