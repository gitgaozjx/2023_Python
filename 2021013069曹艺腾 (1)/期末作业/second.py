import random


def decorate(*args):
    temp = args;
    def tmp(func):
        def wrapper(*args, **kwargs):
            result = dict()
            randomNumbers = func(*args, **kwargs)
            result['data'] = randomNumbers
            sumNumbers = sum(sum(_) for _ in randomNumbers)
            for operate in temp:
                if operate == 'AVG':  
                    result[operate] = sumNumbers/(len(randomNumbers) * len(randomNumbers[0]))
                elif operate == 'SUM':
                    result[operate] = sumNumbers
                else:
                    raise Exception('wrong operation')

            return result
        return wrapper
    return tmp


@decorate('AVG', 'SUM')
def dataSampling(*args, **kwargs):
    result = []
    for _ in range(kwargs['num']):
        element = []
        for data in kwargs['struct']:
            if data['datatype'] == 'int':
                it = iter(data['datarange'])
                tmp = random.randint(next(it), next(it))
            elif data['datatype'] == 'float':
                it = iter(data['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif data['datatype'] == 'str':
                tmp = ''.join(random.SystemRandom().choice(data['datarange']) for _ in range(data['len']))
            else:
                break

            element.append(tmp)
        result.append(element)

    return result

def test():
    result = dataSampling(num=5, struct=[{'datatype':'int', 'datarange':[1, 100]},
                                         {'datatype': 'int', 'datarange':[1, 10]},
                                         {'datatype': 'int', 'datarange': [1, 100]}
                                        ])
    print(result)


if __name__ == "__main__":
    result = dataSampling(num=5, struct=[{'datatype':'int', 'datarange':[1, 100]},
                                         {'datatype': 'int', 'datarange':[1, 10]},
                                         {'datatype': 'int', 'datarange': [1, 100]}
                                        ])
    print(result)