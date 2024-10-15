from codes import RESPONSE_CODES

def sortData(data):
    method = int(input('Choose sort order "increasing/decreasing" (1,2): '))

    if method == 1:
        results = data.sort_values(by=data.columns[0], ascending=True)
    elif method == 2:
        results = data.sort_values(by=data.columns[0], ascending=False)
    else:
        raise ValueError(RESPONSE_CODES[8])
    
    return results