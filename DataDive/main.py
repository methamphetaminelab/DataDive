from codes import RESPONSE_CODES
from sortData import sortData
from chooseData import chooseData
from chooseMode import chooseMode
from loadData import loadData

def main():
    try:
        mode, dataFile = chooseMode()

        if mode in [1, 2, 3]:
            df = loadData(dataFile, mode)
            data = chooseData(df)
        else:
            raise ValueError(RESPONSE_CODES[3])

        print(f'\ndata:\n{data}')
        results = sortData(data)

        return results

    except Exception as e:
        raise Exception(f"{RESPONSE_CODES[101]}: {e}")

if __name__ == '__main__':
    print(f'\nresults:\n{main()}')
else:
    raise Exception(f"{RESPONSE_CODES[101]}: Script is being imported")