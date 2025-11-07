#  متدهای لیست  ------------------------------------

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")                             #  یک عنصر را به انتهای لیست اضافه می کند
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()                                     # تمام عناصر یک لیست را حذف می کند
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()                                   #یک کپی از لیست مشخص شده را برمی گرداند
print(x)

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")                     #تعداد شمارش عناصر با مقدار مشخص شده را برمی گرداند
print(x)


fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)                       #عناصر لیست مشخص شده را به انتهای لیست فعلی اضافه می کند
print(fruits)


fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")                   # موقعیت اولین وقوع مقدار مشخص شده را برمی گرداند
print(x)


fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")     # مقدار مشخص شده را در موقعیت مشخص شده درج می کند.
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)                                   # عنصر را در موقعیت مشخص شده حذف می کند
print(fruits)


fruits = ['apple','banana','cherry','banana']
fruits.remove("banana")                         # ولین مورد از عنصری که مقدار مشخص شده را دارد، حذف می کند
print(fruits)


my_list = [1, 2, 3]
del my_list[1]
#del my_list                                    # یه آیتم خاص رو از لیست حذف میکنه یا حتی کل لیست رو از حافظه پاک میکند
print (my_list)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()                                # ترتیب مرتب سازی عناصر را معکوس می کند
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()                                     # به طور پیش فرض لیست را به صورت صعودی مرتب می کند
print(cars)



#  تاپل های پایتون  ------------------------------------

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#  سازنده تاپل  ------------------------------------

thistuple =tuple(("apple", "banana", "cherry"))
print(thistuple)


#  دسترسی به آیتم های تاپل  ------------------------------------

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#  بررسی تاپل  ------------------------------------
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
 print("Yes, 'apple' is in the fruits tuple")



#  به روز رسانی تاپل ها  ------------------------------------

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")   # حذف ایتم
thistuple = tuple(y)
print(thistuple)


#  بازکردن  تاپل ها  ------------------------------------

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)


#  تاپل های حلقه   ------------------------------------
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)


#  اتصال تاپل ها   ------------------------------------

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#  متدهای تاپل   ------------------------------------

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)          # تعداد دفعاتی که یک مقدار مشخص شده در تاپل ظاهر می شود را برمی گرداند
print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)   # ولین رخداد مقدار مشخص شده را پیدا می کند
print(x)


#  مجموعه های پایتون   ------------------------------------

thisset = {"apple", "banana", "cherry"}
print(thisset)



#  دسترسی به آیتم های مجموعه   ------------------------------------

thisset = {"apple", "banana", "cherry"}
for x in thisset:
 print(x)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)            # برای اضافه کردن آیتم ها از یک مجموعه دیگر به مجموعه فعلی
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")          #برای حذف یک آیتم در یک مجموعه
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()           #  یک آیتم تصادفی را حذف می کند
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()                 # متد ()clear مجموعه را خالی می کند
print(thisset)


#  پیمایش مجموعه   ------------------------------------

thisset = {"apple", "banana", "cherry"}
for x in thisset:
 print(x)


#  متد ()union    ------------------------------------

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


#  برای اتصال دو مجموعه    ------------------------------------

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)


#  تابع ()frozenset در پایتون    ------------------------------------

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

#  دیکشنری های پایتون    ------------------------------------
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict)


#  دسترسی به ایتم دیکشنری پایتون    ------------------------------------
thisdict={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict["model"]
print(x)


thisdict={
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.get("model")
print(x)



#  متد ()keys لیستی از تمام کلیدهای موجود در دیکشنری را برمی گرداند    ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.keys()
print(x)


#   متد ()values لیستی از تمام مقادیر موجود در دیکشنری را برمی گرداند    ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.values()
print(x)

#   متد ()items هر آیتم را در یک دیکشنری، به عنوان تاپل در یک لیست، برمی گرداند.   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.items()
print(x)


#    تعیین اینکه آیا یک کلید مشخص شده در یک دیکشنری وجود دارد یا خیر، از کلمه in کلیدی زیر استفاده میشود   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:
 print("Yes, 'model' is one of the keys in the thisdict dictionary")


#    اضافه کردن یک آیتم به دیکشنری با استفاده از یک کلید اندیس جدید   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

thisdict["color"] = "red"
print(thisdict)

#    اضافه کردن یک آیتم به دیکشنری با استفاده از یک کلید اندیس جدید   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#    متد ()pop ، آیتمی را که نام کلید مشخص شده را دارد، حذف می کند:   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.pop("model")

print(thisdict)



#    متد ()popitem آخرین آیتم درج شده را حذف می کند   ------------------------------------
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.popitem()
print(thisdict)


#    کلمه کلیدی del، آیتمی را که نام کلید مشخص شده را دارد، حذف می کند:   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
del thisdict["model"]
print(thisdict)

#  متد ()clear، دیکشنری را خالی می کند:   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
thisdict.clear()
print(thisdict)


#  حلقه زدن در دیکشنری   ------------------------------------

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict:
    print(thisdict[x])     # تمام مقادیر موجود در دیکشنری را یکی یکی چاپ می کند


thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
for x in thisdict:
    print(x)            #  تمام نام های کلید موجود در دیکشنری را یکی یکی چاپ میکند




#  کپی از دیکشنری   ------------------------------------

# روش  ()dict

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = dict(thisdict)
print(mydict)

# روش  ()copy

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = thisdict.copy()
print(mydict)



#  دیکشنری های تو در تو-Dictionaries Neste   ------------------------------------



                    # یک دیکشنری  که شامل سه دیکشنری است
myfamily ={
    "child1" : {
    "name" : "Emil",
    "year" : 2004
    },
    "child2" : {
    "name" : "Tobias",
    "year" : 2007
    },
    "child3" : {
    "name" : "Linus",
    "year" : 2011
    }
}
print(myfamily)



                      # می توانید با استفاده از ()items روی یک دیکشنری حلقه بزنید
myfamily = {
"child1" : {
"name" : "Emil",
"year" : 2004
},
"child2" : {
"name" : "Tobias",
"year" : 2007
},
"child3" : {
"name" : "Linus",
"year" : 2011
}
}
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])












