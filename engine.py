from random import randint
_comp_number=''

def make_a_number():
    global _comp_number
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
    print(current_number)
    return current_number

def chek_number(comp_number, your_number):
    count_cow = 0
    count_bull = 0
    for i in range(4):
        if your_number[i] == comp_number[i]:
            count_cow += 1
    for i in your_number:
        if i in comp_number:
            count_bull += 1
    print('коров:', count_cow, 'быков', count_bull - count_cow)


def game_over():
    print('Вы отгадали число!')


