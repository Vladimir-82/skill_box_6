from random import randint


def make_a_number():
    comp_number=''
    while len(comp_number) < 4:
        i = str(randint(1, 9))
        if i not in comp_number:
            comp_number = comp_number + i
    return comp_number

def chek_number(comp_number, your_number):
    for i in range(3):
        if your_number[i] == comp_number[i]:


def game_over():
    pass


