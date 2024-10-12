from codes import RESPONSE_CODES

def chooseData(dataFile):
    columns = list(map(int, input('Enter columns (1,2|6,7): ').split(',')))
    lines = input('Enter lines (1,2,3,4|all): ').split(',')

    columnsHead, columnsTail = min(columns) - 1, max(columns)

    if 'all' in lines:
        linesHead, linesTail = 0, dataFile.shape[0]
    else:
        lines = list(map(int, lines))
        linesHead, linesTail = min(lines) - 1, max(lines)
        
    if linesHead < 0 or linesTail > dataFile.shape[0] or columnsHead < 0 or columnsTail > dataFile.shape[1]:
        raise IndexError(f"{RESPONSE_CODES[6]}: Selected indices are out of bounds")

    data = dataFile.iloc[linesHead:linesTail, columnsHead:columnsTail]
    return data