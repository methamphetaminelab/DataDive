from codes import RESPONSE_CODES

def sortData(data):
    #mode = int(input('Choose sort type "by column/by row" or "by row/by column" (1,2): '))
    method = int(input('Choose sort order "increasing/decreasing" (1,2): '))

    if mode == 1:
        if method == 1:
            results = data.sort_values(by=data.columns[0], ascending=True)
        elif method == 2:
            results = data.sort_values(by=data.columns[0], ascending=False)
        else:
            raise ValueError(RESPONSE_CODES[8])
    # elif mode == 2:
    #     if method == 1:
    #         results = data.sort_values(by=data.index, ascending=True)
    #     elif method == 2:
    #         results = data.sort_values(by=data.index, ascending=False)
    #     else:
    #         raise ValueError(RESPONSE_CODES[8])
    else:
        raise ValueError(RESPONSE_CODES[7])
    
    return results