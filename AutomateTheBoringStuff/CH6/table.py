def printTable(data):
    colWidths = [0] *len(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            maxlength = len(data[i][j])
            print(data[i][j])
            print(len(data[i][j]))
        #maxlength = max(len(data[i]))
        #print(max)

    print(colWidths)




tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)