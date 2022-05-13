Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=3
>>> if(a==3): print(3)
	else: print('no 3')
	
SyntaxError: unexpected indent
>>> a=3
>>> if(a==3): print(3)
else: print('no 3')

3
>>> 
================================ RESTART: Shell ================================
>>> age = input('Cual es tu edad?')
Cual es tu edad?24
>>> age
'24'
>>> print('you are hal of your age',age,int(age)*2)
you are hal of your age 24 48
>>> 
>>> 
>>> s = (5,7,8)/2
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#15>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'tuple' and 'int'
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> mat.sqrt(4)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#19>", line 1, in <module>
NameError: name 'mat' is not defined
>>> math.sqrt(4)
2.0
>>> s=((5+7+8)/2)
>>> r = math.sqrt(s(s-5)(s-7)(s-8)/s)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#22>", line 1, in <module>
TypeError: 'float' object is not callable
>>> type(s)
<class 'float'>
>>> math.sqrt(s(s-5)(s-7)(s-8)/s)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#24>", line 1, in <module>
TypeError: 'float' object is not callable
>>> r = math.sqrt((s(s-5)(s-7)(s-8))/s)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#25>", line 1, in <module>
TypeError: 'float' object is not callable
>>> math.sqrt((s(s-5)(s-7)(s-8))/s)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#26>", line 1, in <module>
TypeError: 'float' object is not callable
>>> r = (s(s-5)(s-7)(s-8))/s
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#27>", line 1, in <module>
TypeError: 'float' object is not callable
>>> ((s(s-5)(s-7)(s-8))/s)
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#28>", line 1, in <module>
TypeError: 'float' object is not callable
>>> s
10.0
>>> r = (s*(s-5)*(s-7)*(s-8)/2)
>>> math.sqrt(r)
12.24744871391589
>>> 