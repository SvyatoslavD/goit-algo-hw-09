# HW #09

## Результати тестування

```bash
svyat@svyat-VirtualBox:~/Gits/goit-python/goit-algo-hw-09$ python3 find_coins_greedy.py
       113: 0.000009 seconds
      5222: 0.000007 seconds
     10121: 0.000087 seconds

svyat@svyat-VirtualBox:~/Gits/goit-python/goit-algo-hw-09$ python3 find_min_coins.py
       113: 0.000424 seconds
      5222: 0.022734 seconds
     10121: 0.043532 seconds

```

## Висновки

Жадібний алгоритм працює швидше і ефективніше за пам'яттю. Однак, у складніших сценаріях, де жадібний підхід не забезпечує оптимального рішення, алгоритм динамічного програмування має перевагу, оскільки здатний знаходити глобально оптимальне рішення за рахунок розгляду всіх можливих комбінаці.