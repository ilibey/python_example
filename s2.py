#  تنظیم نوع داده خودکار در پایتون  ------------------------------------

x= "Hello"                          # string
y= 20                               # integer
z= ["apple", "banana", "cherry"]    # list

print(type(x))
print(type(y))
print(type(z))

# تنظیم نوع داده خاص در پایتون  ------------------------------------


w = bool(5)                              # bool
x= str(2.0)                              # string
y = float(20)                            # float
z= list(["apple", "banana", "cherry"])   # list


print(type(w))
print(type(x))
print(type(y))
print(type(z))


# اعداد پایتون  در پایتون ------------------------------------

x = 1 # int
y = 2.8 # float
z = 1j # complex

print(type(x))
print(type(y))
print(type(z))


# رشته های چندخطی در پایتون ------------------------------------

text = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(text)


# دسترسی به کاراکتر خاص در رشته ------------------------------------

a = "Hello, World!"
print(a[1])



# پیمایش رشته در پایتون ------------------------------------

for x in "banana":
    print(x)

#  بررسی وجود یک کلمه خاص در رشته در پایتون ------------------------------------

txt = "The best things in life are free!"
print("free" in txt)


#  برش رشته در پایتون ------------------------------------

b = "Hello, World!"
print(b[2:5])  # برش در یک بازه معین

b = "Hello, World!"
print(b[:5]) # برش از ابتدای رشته

b = "Hello, World!"
print(b[2:])  # برش از انتهای رشته



# متدهای‌از‌پیش ‌تعریف‌ شده در پایتون ------------------------------------

a = "Hello, World!"
print(a.upper())    # Upper Case

a = "Hello, World!"
print(a.lower())    # Lower Case

a = " Hello, World! "
print(a.strip())   # Remove whiteSpace

a = "Hello, World!"
print(a.replace("H", "J"))    # Replace String

a = "Hello, World!"
b = a.split(",")    # Split String
print(b)


#   الحاق رشته در پایتون ------------------------------------

a = "Hello"
b = "World"
c = a + b
print(c)


a = "Hello"
b = "World"
c = a + " " + b
print(c)


#  قالب بندی رشته در پایتون -----------------------------------

age = 21
txt = f"My name is iliya, I am {age}"
print(txt)


#  کاراکتر‌ گریز در پایتون ------------------------------------

txt = 'It\'s alright.'
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)


txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)


# remove:
txt = "Hello \bWorld!"
print(txt)

txt = "Hello\tWorld!"
print(txt)



#  بولین های پایتون ------------------------------------

print(10 > 9) # True

a = 200
b = 33
if b > a:   # False
    print("b is greater than a")



#  عملگرهای پایتون ------------------------------------

x = 5
y = 3
print(x + y)


x = 5
y = 3
print(x * y)



#  عملگرهای انتساب پایتون ------------------------------------

x = 5
print(x)

x = 5
x += 3
print(x)


#  عملگرهای مقایسه ای پایتون ------------------------------------

x = 5
y = 3
print(x == y)

x = 5
y = 3
print(x != y)

x = 5
y = 3
print(x >= y)


#  عملگرهای مقایسه ای پایتون ------------------------------------

x = 5
print(x > 3 and x < 10)       # returns true

x = 5
print(x > 3 or x < 4)         # returns true

x = 5
print(not(x > 3 and x < 10))   # returns false



#  عملگرهای هویت پایتون ------------------------------------

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # returns True

print(x is y) # returns False

print(x == y) # returns True


#  عملگرهای عضویت پایتون ------------------------------------

x = ["apple", "banana"]
print("banana" in x)          # returns True


x = ["apple", "banana"]
print("pineapple" not in x)   # returns True



#  عملگرهای بیتی پایتون ------------------------------------

print(6 & 3) # return 2

print(6 | 3) # return 7


#  اولویت عملگرها ------------------------------------

print((6 + 3) - (6 + 3))

