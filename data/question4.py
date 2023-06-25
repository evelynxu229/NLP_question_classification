#统计fine_labels.txt与coarse_labels.txt前两列相同的数据count
array2d = []
output_dict={}
origin_dict={}
count=0
with open(r"data/coarse_output.txt", "r") as f:
    all_data = f.readlines()
    for i in range(0,len(all_data)):
        temp_list = []
        for element in all_data[i].split():
            temp_list.append(element)
        
        if temp_list[0] in origin_dict:
            origin_dict[temp_list[0]]+=1
        else:
            origin_dict.update({temp_list[0]:1})

        if temp_list[0]==temp_list[1]:
            if temp_list[0] in output_dict:
                output_dict[temp_list[0]]+=1
            else:
                #output_dict[temp_list[0]].append(0)
                output_dict.update({temp_list[0]:1})
            #count+=1
        
        array2d.append(temp_list)

#print(array2d)
#print(count)
print(output_dict)
print(origin_dict)

for key in output_dict:
    if key in origin_dict:
        #print(output_dict[key])
        #print(origin_dict[key])
        output_dict[key]=round(output_dict[key]/origin_dict[key],2)
for key in origin_dict:
    if key not in output_dict:
        output_dict.update({key:0})

print(output_dict)



