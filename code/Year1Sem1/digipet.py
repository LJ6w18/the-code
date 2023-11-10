menu = ['Feed','Play','Rest','Status']
status = [3,3,3]
title = ['hungry','happiness','energy']
msg = ['Nom nom nom','XD','Zzzzz']
print("Digipet")
while True:
    for i in range(len(menu)):
        print('({}) {}'.format(i+1 , menu[i]))
        selection = int(input("Please select an option"))
    if selection == 4:
        state = ''
        for s in range (status[i]):
            state = state + "*"
        for u in range(5-status[1]):
            state = state + "."
    else:
        print(msg[selection-1])
        for s in range(len(status)):
            status[s] -= 1

        status[selection-1] += 2

        for s in range(len(status)):
            if status[s] >5:
                status[s]=5
            elif status[s] <5:
                status[s] = 0

 