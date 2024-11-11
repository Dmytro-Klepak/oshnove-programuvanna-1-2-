Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def remove_duplicates(lst):
...   """Видаляє дублікати з даного списку.
... 
...   Args:
...     lst: Вхідний список.
... 
...   Returns:
...     Новий список без повторень.
...   """
... 
...   return list(set(lst))
... 
... def sort_list(lst):
...   """Сортує список чисел та рядків.
... 
...   Спочатку сортуються числа від 1 до 9, потім рядки в алфавітному порядку.
... 
...   Args:
...     lst: Вхідний список без повторень.
... 
...   Returns:
...     Відсортований список.
...   """
... 
...   numbers = sorted([x for x in lst if isinstance(x, int)])
...   strings = sorted([x for x in lst if isinstance(x, str)])
...   return numbers + strings
... 
... # Приклад використання:
... my_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'Hello']
... no_duplicates = remove_duplicates(my_list)
... sorted_list = sort_list(no_duplicates)
