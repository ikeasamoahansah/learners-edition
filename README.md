# learners-edition
Basic functions

print("Hello, World!")
Hello, World!

exit()
#this will exit the work you are doing

#syntax
if 5 > 2:
  print("Five is greater than two!")
Five is greater than two!

#syntax error
if 5 > 2:
print("Five is greater than two!")
File "demo_indentation_test.py", line 2
    print("Five is greater than two!")
        ^
IndentationError: expected an indented block


#The number of spaces is up to you as a programmer, but it has to be at least one

Example
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")
Five is greater than two!
Five is greater than two!

#syntax error
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
File "demo_indentation2_error.py", line 3
    print("Five is greater than two!")
    ^
IndentationError: unexpected indent
