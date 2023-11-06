# Урок 8 - Декораторы и модули
## Контрольные вопросы:
- Что делает команда __from module import *__? 
какие проблемы могут возникнуть при её использовании?
- Какое определение функции будет использовано при 
возникновении конфликта имен?
- Зачем нужен \__init__.py? Каким должно быть его 
содержимое?
- В чем проблемы использования декораторов? 
Можно ли процесс декорирования обернуть вспять?
- Как порядок декорирования влияет на результат 
работы функции?
- В каких случаях имеет смысл использовать декораторы?
## Задания:
1) Написать декоратор, разворачивающий порядок 
переданных в функцию аргументов независимо от их 
количества (например декорированная `foo(4, 5)` должна
быть эквивалентна вызову недекорированной `foo(5, 4)`).
2) Написать декоратор, печатающий аргументы, 
переданные функции, после её выполнения.
3) Написать декоратор, пробующий запустить 
переданную функцию, и возвращающий строку __"error"__ в 
случае возникновения исключения.
4) Написать программу, сравнивающую скорость работы 
функции вычисления чисел Фибоначчи, написанной через 
циклы и через рекурсию, с использованием `@cache`
и без.