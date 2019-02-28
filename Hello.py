import numpy as np

def loadInputs(file_name):
    f = open(file_name)
    content = f.readlines()
    info = content[0].split()
    rows = int(info[0])
    columns = int(info[1])
    l = int(info[2])
    h = int(info[3])
    matrix = np.zeros((rows, columns), dtype=int)
    content.pop(0)
    for i in range(rows):
        for j in range(columns):
            if content[i][j] == 'M':
                matrix[i][j] = 1


def writeResults(results,file_name):
    outputFile = 'output/' + file_name + '.txt'
    f = open(outputFile, 'w')
    f.write(str(len(results)) + '\n')
    for r in results:
        f.write(str(r[0]) + ' ' + str(r[1]) + ' ' + str(r[2]) + ' ' + str(r[3]) + '\n')

    f.close()
