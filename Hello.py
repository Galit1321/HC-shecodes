import numpy as np


class Photo:
    def __init__(self, p_id, pos,noft, tags):
        self.noftag=noft
        self.id = p_id
        self.pos = pos
        self.tags = tags
        self.visit = False


def loadInputs(file_name):
    f = open(file_name)
    text = f.readlines()
    N = int(text[0])
    text.pop(0)
    res=list([])
    for i in range(N):
        row = text[i].split()
        p=Photo(i,row[0],row[1],row[2:])
        res.append(p)
    return res

def writeResults(results, file_name):
    outputFile = 'output/' + file_name + '.txt'
    f = open(outputFile, 'w')
    f.write(str(len(results)) + '\n')
    for r in results:
        f.write(str(r[0]) + ' ' + str(r[1]) + ' ' + str(r[2]) + ' ' + str(r[3]) + '\n')

    f.close()


if __name__ == "__main__":
    fileFullName = 'a_example.txt'
    p = loadInputs(fileFullName)
    for pic in p:
        print(pic.tags)
