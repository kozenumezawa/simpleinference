import json

import numpy


def split(item):
    reshaped = item.reshape((2, len(item) // 2))
    return {
        'x': [str(v) for v in reshaped[0]],
        'y': [str(v) for v in reshaped[1]],
    }


def main():
    data = numpy.load('logistic.npy')
    obj = {
        'data': [{'X': list(item[0]), 'Y': list(item[1])} for item in data],
    }
    json.dump(obj, open('../logistic.json', 'w'), sort_keys=True, indent=2)

if __name__ == '__main__':
    main()
