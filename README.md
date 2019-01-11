# Paginação de Itens
Algoritmo para paginação

Python 3.7

```python
items = list(range(1,101))
items_per_page = 49
```


```python
print(items)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]



```python
if (len(items) % items_per_page) > 0:
    qtd_group_rest = (len(items) % items_per_page)
    num_div = int((len(items) - qtd_group_rest) / items_per_page)
    
    array_final = []
    array_temp = items[:]
    
    i = 0
    while i < num_div:
        array_final = array_final + [array_temp[:items_per_page]]
        array_temp = array_temp[items_per_page:]
        i += 1
        
    array_final = array_final + [items[-qtd_group_rest:]]
else:
    num_div = int(len(items) / items_per_page)
    
    array_final = []
    array_temp = items[:]
    
    i = 0
    while i < num_div:
        array_final = array_final + [array_temp[:items_per_page]]
        array_temp = array_temp[items_per_page:]
        i += 1
```


```python
print(len(array_final), array_final)
```

    3 [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [99, 100]]


Após obter o array_final com os itens divididos por grupos de items_per_page, obtenha o numero da pagina via query_param para definir qual index do array_final usar.
