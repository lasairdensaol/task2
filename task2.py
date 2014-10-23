#! /usr/bin/python
# -*- coding: utf-8 -*-


import itertools


def fun2(str):
    result_list = []
    
    if(str[0] == '['):
        
        index = 0
        begin = 1
        end = 0
        for i in range(len(str[1:-1]))[1:]:                    
            if (str[i] == '&'): 
                if (index == 0):
                    #print str[i+1]
                    end = i
                    #print fun1(str[begin:end])
                    result_list+=fun1(str[begin:end])
                    begin = end + 1
            if (str[i] == '[') | (str[i] == '{'):
                index += 1
            if  (str[i] == ']') | (str[i] == '}'):
                index -= 1
        result_list+=fun1(str[begin:-1])
    if(str[0] == '{'):  
        end_separator = str.find('|')
        separator = str[1:end_separator]   
        new_str = str[end_separator+1:-1]
        index = 0
        begin = 0        
        listForCombination = []
        for i in range(len(new_str)):
            if (new_str[i] == '&'): 
                if (index == 0):
                    listForCombination.append(new_str[begin:i])
                    begin = i + 1
            if (new_str[i] == '[') | (new_str[i] == '{'):
                index += 1
            if  (new_str[i] == ']') | (new_str[i] == '}'):
                index -= 1
        listForCombination.append(new_str[begin:])
        #print listForCombination
        # список для перестановок получе. необходимо получить перестановки 
        # перестановки записать в строки, разделяя запятыми
        ListOfPerm = list(itertools.permutations(listForCombination))
        
        for x in ListOfPerm:
            result_list += fun1(separator.join(list(x)))
        
        
    return result_list


def fun1(str):
    index = 0
    begin = 0
    end = 0
    list1 = [str]
    listOfSub = []
    for i in range(len(str)):
        if (str[i] == '[') | (str[i] == '{'):
            if (index == 0):  
                index += 1
                begin = i
            else:
                index += 1
        if  (str[i] == ']') | (str[i] == '}'):
            if (index == 1):
                end = i
                index -= 1
                listOfSub.append([fun2(str[begin:end+1]),[begin, end+1]])
            else:
                index -= 1 
    listOfSub = listOfSub[::-1]
    
    # Комбинации списков
    for x in listOfSub:
        tmp_lst = []
        for y in x[0]:
            for z in list1:
                temp_str = (z[:x[1][0]] + y + z[x[1][1]:])
                tmp_lst.append(temp_str)
        list1 = tmp_lst
        
    return list1
# Работа с обычной строкой
    # Поиск выражения в скобках
        # Если существует такое выражение
            # Запоминаем его расположение
            # Выражение в скобках посылаем в новую функции, которая вернет список
            # Соединяем строку и список, получаем список строк
    
# Работа с шаблоном
    # Определить тип шаблона
    # Разбить его на части
    # Каждую из частей отправить в функцию 1 для обработки
    # в зависимости от типа формировать список строк

#str = "Hello world [1. раз&2. Два&{ - |3. Три&4. Четыре}]!"
str = raw_input('Строка на ввод: ')
#print "Строка на ввод: "
#print str
print "Вывод: "
z = fun1(str)
for x in z:
    print x