path= 'C:\\school\\ze programming\\'
f = open(path + "Sales.txt","r")
sales_list = []
for line in f:
    sales_list.append(line[:-1].split(","))
('\n').split(',')
f.close()


print(sales_list)
product_list = ['MacBook Air','Macbook Pro','iMac']


Total_units_list = [0, 0, 0]
print('{:15s}{:15s}{}'.format(sales_list[0][0],sales_list[0][1],sales_list[0][2]))

for item in sales_list[1:]:
    branch = item[0]
    product = item[1]
    units_sold = int(item[2])
    for i in range(len(product_list)):
        if product_list[i] == product:
            Total_units_list[i] += units_sold
            break
    print('{:15s}{:15s}{}'.format(branch,product,units_sold))