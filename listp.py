Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> book = ["chair","goat","rose"]
>>> book
['chair', 'goat', 'rose']
>>> book.append("we")
>>> book
['chair', 'goat', 'rose', 'we']
>>> #copy the list grocery and assign it to new variable of new grocery.
>>> #list comprehension.
>>> #Let’s say you want to make the same list as before, but you only want to multiply the numbers that can be divided by 2
>>> c = []
>>> y=[2,5,8,12,23]
>>> c= [n*n for n in y:
  File "<stdin>", line 1
    c= [n*n for n in y:
                      ^
SyntaxError: invalid syntax
>>> c= [n*n for n in y: if n%2==0
  File "<stdin>", line 1
    c= [n*n for n in y: if n%2==0
                      ^
SyntaxError: invalid syntax
>>> c= [n*n for n in y; if n%2==0
  File "<stdin>", line 1
    c= [n*n for n in y; if n%2==0
                      ^
SyntaxError: invalid syntax
>>> c= [n*n for n in y]:
  File "<stdin>", line 1
    c= [n*n for n in y]:
                       ^
SyntaxError: invalid syntax
>>> c= [n*n for n in y if n%2==0]:print c
  File "<stdin>", line 1
    c= [n*n for n in y if n%2==0]:print c
                                 ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(c)?
>>> c= [n*n for n in y if n%2==0]:print(c)
  File "<stdin>", line 1
    c= [n*n for n in y if n%2==0]:print(c)
                                 ^
SyntaxError: invalid syntax
>>> c= [n*n for n in y if n%2==0]:print(c)
  File "<stdin>", line 1
    c= [n*n for n in y if n%2==0]:print(c)
                                 ^
SyntaxError: invalid syntax
>>> Note that you can also use list comprehension to loop over a list. Here, the results are already printed out without you having to pass print():
  File "<stdin>", line 1
    Note that you can also use list comprehension to loop over a list. Here, the results are already printed out without you having to pass print():
         ^
SyntaxError: invalid syntax
>>> 
>>> c= [n*n for n in y if n%2==0]
>>> print(c)
[4, 64, 144]
>>> Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
  File "<stdin>", line 1
    Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
          ^
SyntaxError: invalid syntax
>>> 
>>> Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
  File "<stdin>", line 1
    Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
          ^
SyntaxError: invalid syntax
>>> 
>>> Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
  File "<stdin>", line 1
    Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
          ^
SyntaxError: invalid syntax
>>> 
>>> fruit = []
>>> food = ["passion","mcele","anne","azma"]
>>> fruit=[if fruit.startswith("a") :
  File "<stdin>", line 1
    fruit=[if fruit.startswith("a") :
           ^
SyntaxError: invalid syntax
>>> fruit=[if fruit.startswith("a")] :print(fruit)
  File "<stdin>", line 1
    fruit=[if fruit.startswith("a")] :print(fruit)
           ^
SyntaxError: invalid syntax
>>> fruit=[if fruit.startswith("a") :

