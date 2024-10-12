from codes import RESPONSE_CODES
import os

def chooseMode():
    mode = int(input('Choose mode:\n[1] xlsx\n[2] csv\n[3] text\n'))

    dataFile = None
    if mode in [1, 2]:
        dataFile = input('Enter file path: ')

    if mode == 1:
        if os.path.splitext(dataFile)[1].lower() != '.xlsx':
            raise ValueError(f"{RESPONSE_CODES[1]}: Expected '.xlsx' file but got '{os.path.splitext(dataFile)[1].lower()}'")
        elif not os.path.exists(dataFile):
            raise FileNotFoundError(f"{RESPONSE_CODES[99]}: File not found at '{dataFile}'")
        
    elif mode == 2:
        if os.path.splitext(dataFile)[1].lower() != '.csv':
            raise ValueError(f"{RESPONSE_CODES[1]}: Expected '.csv' file but got '{os.path.splitext(dataFile)[1].lower()}'")
        elif not os.path.exists(dataFile):
            raise FileNotFoundError(f"{RESPONSE_CODES[99]}: File not found at '{dataFile}'")

    elif mode == 3:
        pass
    else:
        raise ValueError(RESPONSE_CODES[3])
    
    return mode, dataFile