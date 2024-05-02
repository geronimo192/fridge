import datetime
from decimal import Decimal

goods = {}

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    x = {}
    x['amount'] = amount
    y = {}
    if expiration_date != None:
        y['expiration_date'] = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
    else:
        y['expiration_date'] = None
    
    if title in items:
        items[title] += x | y
    else:
        items[title] = x | y
    print  (items)
    items[title] = list(items[title])
    c = len (items[title])
    items[title][c-2] = x
    items[title][c-1] = y
    items[title][c-2] = items[title][c-2] | items[title][c-1] 
    items[title].pop(c-1)
    
add(goods, 'Яйца', Decimal('10'), '2023-9-30')
add(goods, 'Яйца', Decimal('3'), '2023-1-15')
add(goods, 'Яйца', Decimal('5'), '2023-11-15')
print (goods)

def add_by_note(items, note):
    lst = note.split()
    n = len(lst)
    print(Decimal(1.5))
    if '-' in note:
        expiration_date = lst[n-1]
        print(expiration_date)
        lst[n-2] = float(lst[n-2])
        amount = Decimal(lst[n-2])
        print(amount)
        print(lst)
        lst.pop(n-1)
        lst.pop(n-2)
        title = ' '.join(lst)
    else:
        expiration_date = None
        print(expiration_date)
        lst[n-1] = float(lst[n-1])
        amount = Decimal(lst[n-1])
        print(amount)
        print(lst)
        lst.pop(n-1)
        title = ' '.join(lst)
    return  add (items,title, amount, expiration_date)
    
add_by_note({}, 'Яйца Фабрики №1 4 2023-07-15')  
print(goods)
def find(items, needle):
    h = list(items)
    s= []
    for i in range(len(h)):
        if needle.casefold() in h[i].casefold():
            s.append(h[i])
    return s
def amount(items, needle):
    h = list(items)
    s = 0
    for i in range(len(h)):
        if needle.casefold() in h[i].casefold():
            x = items[h[i]]
            for i in range(len(x)):
                s+= x[i]['amount']
    if s==0:
        s = Decimal(0)
    return s


def expire(items, in_advance_days=0):
    a = []
    current_time = datetime.date.today()  + datetime.timedelta( days=in_advance_days )
    print(current_time)
    h = list(items)
    s = 0
    for i in range(len(h)):
         x = items[h[i]]
         e = Decimal(0)
         for j in range(len(x)):
             s = x[j]['expiration_date']
             print(s)
             if s != None:
                 if s <= current_time:
                    e += x[j]['amount']
         if e > Decimal(0): 
             a.append((h[i],e))
            
    return a