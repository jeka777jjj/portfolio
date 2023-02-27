NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']
GOODCHAR = ['(', ')', '+', '-', '*', '/']

'''
Декоратор.
Видаляє всі пробіли та букви, залишаючи лише числа та дії
'''
def to_normal_vision(func):
    def wrapper(s: str):
        s.replace(' ', '').strip()
        resoult = ''
        for char in s:
            if char in NUMBERS or char in GOODCHAR:
                resoult += char
        return func(resoult)
    return wrapper


'''
Елементарні дії над числами
Приймаємо 2 числових значення та дію, яку необхідно провести над ними
Повертаємо результат дії
'''
def elementary(a, b, to_do):
    if to_do == '*':
        return a * b
    elif to_do == '/':
        return a / b
    elif to_do == '+':
        return a + b
    else:
        return a - b


'''
Отримуємо масив та дію, яку необхідно провести
Знаходимо індекс дії та проводимо її над сусідніми елементами
Заміняємо елемент дії та двох сусідніх ресультатом
'''
def action(l: list, a: str):
    index = l.index(a)
    res = elementary(l[index - 1], l[index + 1], a)
    for i in range(index + 1, index - 2, -1):
        l.pop(i)
    l.insert(index - 1, res)
    return l


def string_to_list(s: str):
    temp = []
    s_temp = ''
    '''
    Розділимо нашу строку на елементи масиву.
    Числові значення одразу переводимо в необхідний тип
    '''
    for char in s:
        if char not in NUMBERS:
            if s_temp != '':
                try:
                    temp.append(int(s_temp))
                    s_temp = ''
                except:
                    temp.append(float(s_temp))
                    s_temp = ''
            temp.append(char)
        else:
            s_temp += char
    try:
        temp.append(int(s_temp))
    except:
        temp.append(float(s_temp))
    return temp


def calc(temp: list):
    '''
    Поки ми будемо мати якісь дії в нашому масиві будемо їх виконувати, заміняючи результатом 2 числових масива та дію
    '''
    while '*' in temp or '/' in temp or '+' in temp or '-' in temp:
        if '*' in temp:
            temp = action(temp, '*')
        elif '/' in temp:
            temp = action(temp, '/')
        elif '+' in temp:
            temp = action(temp, '+')
        else:
            temp = action(temp, '-')
    return temp


@to_normal_vision
def main(s: str):
    q_list = string_to_list(s)
    if '(' in q_list and ')' in q_list:
        while '(' in q_list and ')' in q_list:
            for i in range(0, len(q_list)):
                if q_list[i] == '(':
                    open_index = i
            close_index = q_list[open_index: -1].index(')') + open_index
            temp_res = calc(q_list[open_index + 1: close_index])
            for i in range(close_index, open_index - 1, -1):
                q_list.pop(i)
            q_list.insert(open_index, temp_res[0])
        resoult = calc(q_list)
    else:
        resoult = calc(q_list)
    return resoult[0]



question = input('Enter your question - ')
print(main(question))
