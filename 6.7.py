tableData=[['apples', 'oranges' , 'cherries', 'banana'],
           ['Alice', 'Bob', 'Carol' , 'David'],
           ['dogs', 'cats', 'moose', 'goose']]
''' print list like this:
  apples Alice  dogs
 oranges   BOb  cats
cherries Carol moose
  banana David goose
'''

def printTable(table):
    colWidths=[0]*len(table)
    length=len(table[0])
    for i in range(len(colWidths)):
        max=0
        for j in range(length):
            if len(table[i][j])>max:
                max=len(table[i][j])
        colWidths[i]=max
    for n in range(length):
        for m in range(len(colWidths)-1):
            string=table[m][n].rjust(colWidths[m])
            print(string,end=' ')
        print(table[m+1][n].rjust(colWidths[m]))
printTable(tableData)
