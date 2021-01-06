def printTable(data):
    colWidths = [0] *len(data)

    #find column widths and sets colWidths[i] to width
    for j in range(len(data)):
        lst = data[j]
        lengths = []
        for i in range(len(lst)):
            lengths.append(len(lst[i]))
        maxlength = max(lengths)
        colWidths[j] = maxlength

    #prints using the method in CH4 - 'flipping' the table
    #For future ref - it prints str


    for x in range(len(data[0])) :
        for y in range(len(data)) :
            print(data[y][x].ljust(colWidths[y]), end = '   ')
        print()



tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)