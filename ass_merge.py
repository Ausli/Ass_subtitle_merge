import os
import glob
os.chdir('K:\Violet Evergarden')


first_header=[]
data_list=[]
style_list=[]
for count,ass_file in enumerate(glob.glob(os.getcwd()+'/*.ass')):#glob.glob(os.getcwd()+'/*.ass')
    print(ass_file)
    f = open(ass_file, 'r',
             encoding='utf8')
    data = f.readlines()
    f, s = 0, 0
    for c,x in enumerate(data):
        if 'Format'.lower() in x.lower() and '[V4+ Styles]'.lower() in data[c - 1].lower():
            s = c + 1
        elif 'Format'.lower() in x.lower() and 'Events'.lower()in data[c-1].lower() and count==0:
            data_list.append(data[c - 2:c+1])
            data_list.append([','.join(i.split(',')[:4])+'-'+str(count)+','+','.join(i.split(',')[4:]) for i in data[c+1:]])
            f=c - 2
        elif 'Format'.lower() in x.lower() and 'Events'.lower()in data[c-1].lower():
            data_list.append([','.join(i.split(',')[:4])+'-'+str(count)+','+','.join(i.split(',')[4:]) for i in data[c+1:]])
            f = c - 2
        c += 1
    if count==0:
        first_header=data[:s]
    style=[i.split(',')[0]+'-'+str(count)+','+','.join(i.split(',')[1:]) for i in data[s:f]]
    style_list.append(style)
with open('../00000.ass','w',encoding='utf8') as f2:
    f2.writelines(first_header+[x for y in style_list for x in y]+[x for y in data_list for x in y])