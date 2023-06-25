#songlin_test_1
import random
import string

def DataSampling(**kwargs):
    """
    :param kwargs:
    :return:
    """
    result = list()
    for index in range(0,kwargs["num"]):
        element = list()
        for key in kwargs.get("struct"):
            if key["datatype"] == "int":
                it = iter(key["datarange"])
                tmp = random.randint(next(it),next(it))
            elif key["datatype"] == "float":
                it = iter(key["datarange"])
                tmp = random.uniform(next(it), next(it))
            elif key["datatype"] =="str":
                tmp = ''.join(random.SystemRandom().choice(key["datarange"]) for _ in range(key["len"]))
            else:
                break
            element.append(tmp)
        result.append(element)
    return result

s = DataSampling(
        num=3,
        struct=(
            {
                'datatype': "int",
                'datarange': (0, 100)
            },
            {
                'datatype': "float",
                'datarange': (0, 100)
            },
            {
                'datatype': "str",
                'datarange': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                'len': 5
            }
        )
    )
if __name__ == '__main__':
    print(s)

