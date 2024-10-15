def getPoints(data, columnX, columnY):
    xPoint = data[columnX].tolist()
    yPoint = data[columnY].tolist()

    uniqueX = sorted(list(set(xPoint)))
    uniqueY = sorted(list(set(yPoint)))

    resultX = [uniqueX.index(x) for x in xPoint]
    resultY = [uniqueY.index(y) for y in yPoint]

    coordinates = list(zip(resultX, resultY))

    return coordinates