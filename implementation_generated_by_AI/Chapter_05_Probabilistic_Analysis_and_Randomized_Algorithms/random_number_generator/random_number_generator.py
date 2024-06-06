import random


def random_number():
    return random.randint(0, 1)


def random_number_generator(a:int, b:int):
    """
    return a random number in the range [a, b], 
    but use only random_number() 

    Args:
        a (int): _description_
        b (int): _description_
    """
    assert a <= b
