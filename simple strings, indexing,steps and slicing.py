Python 3.14.6 | packaged by Anaconda, Inc. | (main, Jul  9 2026, 14:37:38) [GCC 14.3.0] on linux
Enter "help" below or click "Help" above for more information.
a= "welcome to test"
a
'welcome to test'
a [0]
'w'
a [1]
'e'
a [3]
'c'
a [7]
' '
a [10]
' '
a [4]
'o'
a [9]
'o'
a [0:9]
'welcome t'
a [0:8]
'welcome '
a [0:7]
'welcome'
a [4:5]
'o'
a [4.4]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a [4.4]
TypeError: string indices must be integers, not 'float'
a [4:4]
''
a [0:0]
''
a [1:9:2]
'ecm '
a [1:4:4]
'e'
a [1:4:3]
'e'
a [1:4:2]
'ec'
a [1:5:2]
'ec'
>>> a [1:5:3]
'eo'
>>> b= "thirty seven days for christmas!!!"
>>> b
'thirty seven days for christmas!!!'
>>> b [9]
'v'
>>> b [11]
'n'
>>> b [0]
't'
>>> b.capitalize()
'Thirty seven days for christmas!!!'
>>> b [22]
'c'
>>> b [22:50]
'christmas!!!'
>>> b [22:67:31]
'c'
>>> b [22:31]
'christmas'
>>> b [31: ]
'!!!'
>>> b [ : ]
'thirty seven days for christmas!!!'
>>> b [ : 30]
'thirty seven days for christma'
>>> c= "end of the test xd"
>>> c
'end of the test xd'
>>> c [16:18}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> C [16:18]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    C [16:18]
NameError: name 'C' is not defined. Did you mean: 'c'?
>>> c [16:18]
'xd'
