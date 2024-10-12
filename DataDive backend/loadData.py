from codes import RESPONSE_CODES
import pandas as pd

def loadData(file, mode):
    if mode == 1:
        df = pd.read_excel(file)
    elif mode == 2:
        df = pd.read_csv(file)
    elif mode == 3:
        pass
    else:
        raise ValueError(RESPONSE_CODES[3])

    return df