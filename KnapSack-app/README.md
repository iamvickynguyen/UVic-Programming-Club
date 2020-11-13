## 0/1 Knapsack App
Simple Python web app for choosing optimal items.

## Installation
```pip3 install -r requirements.txt```

## Run
```python3 app.py```

## Instructions
Complete the ```knapsack()``` function in ```app.py``` <br>
Get ```value``` of item at index 1: ```int(items[1]['value'])``` <br>
Get ```weight``` of item at index 1: ```int(items[1]['weight'])``` <br>
Return a list which includes item at index 0 and 1: <br>
```
result = []
result.append(items[0])
result.append(items[1])
return result
```