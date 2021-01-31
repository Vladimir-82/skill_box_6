from random import randint
_comp_number=''

def make_a_number():
    global  _comp_number
    while len(_comp_number) < 4:
        i = str(randint(1, 9))
        if i not in _comp_number:
            _comp_number = _comp_number + i
    return _comp_number

def get_info(comp_number, your_number):
    current_number = '****'
    for i in range(4):
        if comp_number[i] == your_number[i]:
            current_number = current_number[:i:] + comp_number[i] + current_number[i+1::]
    return comp_number

def chek_number(comp_number, your_number):
    pass
                


def game_over():
    pass

get_info('1234', '1237')
