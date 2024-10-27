arr =  [10, 3, 50, 100]

def test():

    for element in arr:
        if element == 3:
            continue
        else:
            print(element)

test()