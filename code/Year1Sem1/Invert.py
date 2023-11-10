path= 'C:\\school\\ze programming\\'
f = open(path + "Colors.csv","r")
colors_dict={}
new_colors={}
for line in f:
    line = line.strip('\n')
    data_list = line.split(',')
colors_dict[data_list[0]] = data_list[1]
f.close

for name in colors_dict:
    color = colors_dict[name]
    if color in new_colors:
        name_list = new_colors[color]
    else:
        name_list = []
        
        name_list.append(name)
        
        new_colors[color] =name_list



print("Colors Dict\n",colors_dict)
print("\n New Colors \n",new_colors)
print(len(new_colors))