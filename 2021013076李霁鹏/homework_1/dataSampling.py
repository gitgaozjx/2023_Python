import random
def dataSampling(**kwargs):
    structure = kwargs.get("struct")
    result = list()
    for index in range (0,kwargs.get("num")):
        element = dict()
        for key, value in structure.items():
            if value["datatype"] == "int":
                it = iter(value['datarange'])
                tmp = random.randint(next(it),next(it))
            elif value["datatype"] == "float":
                it = iter(value['datarange'])
                tmp = random.uniform(next(it), next(it))
            elif value["datatype"] == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            else:
                break
            element[key] = tmp
        result.append(element)
    return result

if __name__ == '__main__':
    a = dataSampling(
        num = 5,
        struct={
         "a":{
             "datatype":"int",
             "datarange":(0,100)},
         "b":{
             "datatype": "float",
             "datarange":(0,100)},
         "c":{
             "datatype": "str",
             "datarange":('abc','abuwe'),"len":5}
         }
         )
    print(a)


