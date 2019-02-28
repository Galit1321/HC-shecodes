import numpy as np



class Photo:
    def __init__(self, p_id, pos, noft, tags):
        self.noftag = noft
        self.id = p_id
        self.pos = pos
        self.tags = set(tags)
        self.visit = False


def loadInputs(file_name):
    f = open(file_name)
    text = f.readlines()
    N = int(text[0])
    text.pop(0)
    horizontal = list([])
    verticals = []
    for i in range(N):
        row = text[i].split()
        p = Photo(i, row[0], row[1], row[2:])
        if row[0] == 'V':
            verticals.append(p)
        else:
            horizontal.append(p)
    np.random.shuffle(verticals)
    res=list([])
    while len(verticals)!=0:
        temp1 = verticals[0]
        temp2=verticals[1]
        verticals.pop(0)
        verticals.pop(0)
        temp1.id=(temp1.id,temp2.id)
        temp1.tags= set(temp1.tags|temp2.tags)
        temp1.noftag=len(temp1.tags)
        res.append(temp1)
    res+horizontal
    np.random.shuffle(res)
    return res


def minPic(p1, p2):
    common = len(p1.tags & p2.tags)
    aDiff = len(p1.tags) - common
    bDiff = len(p2.tags) - common
    return min(common, aDiff, bDiff)


def createSlideShow(arr):
    # x = int(np.math.log(len(arr)))
    x = int(np.sqrt(len(arr)))
    if (x <100):
        x =100
    slide = list([])
    sum = 0
    elem = arr[0]
    slide.append(elem)
    arr.pop(0)
    while len(arr) != 0:
        elem = slide[-1]
        maxIp = 0
        maxNum = 0
        endIn = min(x, len(arr))
        for i in range(0, endIn):
            temp = minPic(elem, arr[i])
            if (temp > maxNum):
                maxNum = temp
                maxIp = i
        slide.append(arr[maxIp])
        arr.pop(maxIp)
        sum += maxNum

    return slide, sum


def printToOutput(photos):
    f = open("output.txt", "w")
    f.write(str(len(photos))+"\n")
    for photo in photos:
        f.write(' '.join([str(id)for id in photo.id])+"\n")


if __name__ == "__main__":
    files = [ 'a_example.txt']
    for fileFullName in files:
        pic = loadInputs(fileFullName)
        slide, sumSlide = createSlideShow(pic)
        print("slide: ", [elem.tags for elem in slide], "sum: ", sumSlide)
