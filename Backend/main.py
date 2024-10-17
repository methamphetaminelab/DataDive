from codes import RESPONSE_CODES
from chooseData import chooseData
from chooseMode import chooseMode
from loadData import loadData
from sortData import sortData
from getPoints import getPoints

"""
codes - коды ответов, возвращает название ошибки
chooseMode - выбор режима работы, возвращает выбранный режим ([1] xlsx [2] csv) и путь к файлу
loadData - загрузка данных, возвращает загруженный датасет
chooseData - выбор данных, возвращает выбранный датасет (т.е. датасет с выбранными колонками)
sortData - сортировка данных, возвращает отсортированный датасет
getPoints - получение точек для графика
"""

def main():
    try:
        mode, dataFile = chooseMode()

        if mode in [1, 2, 3]:
            df = loadData(dataFile, mode)
            data = chooseData(df)
            print(f'\n------\ndata\n{data}\n------\n')
        else:
            raise ValueError(RESPONSE_CODES[3])

        sortedData = sortData(data)
        print(f'\n------\nsortedData\n{sortedData}\n------\n')

        results = getPoints(sortedData, sortedData.columns[0], sortedData.columns[1])

        return results

    except Exception as e:
        raise Exception(f"{RESPONSE_CODES[101]}: {e}")


if __name__ == '__main__':
    print(main())
else:
    raise Exception(f"{RESPONSE_CODES[101]}")
