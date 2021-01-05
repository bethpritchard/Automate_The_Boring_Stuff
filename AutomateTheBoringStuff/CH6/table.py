def printTable(data):
    colWidths = [0] *len(data)
    for i in range(len(data)):
        col = data[i]
        for j in range(len(data[i])):
            colWidths = max(len(data[i]))
    print(colWidths)



tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)