import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Неизвестная операция."

'''
Задача. В настоящий момент реализовано три unit-теста
Проверяется корректность работы калькулятора для действий сложения, деления и неизвестной операции
Необходимо добавить тесты для следующих операций:
1. Вычитание
2. Умножение
'''

def test_calculate_subtraction():
    assert calculate(5, 3, '-') == 2


def test_calculate_multiplication():
    assert calculate(3, 4, '*') == 12


