#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be
# integer or string and expressions will be mathematical operators.
# 
# * expression
# 'hello'----value
# -87.8 -----value
# - expression
# / expression
# + expression
# 6---value

# 2. What is the difference between string and variable?
# Ans: Variable is a kind of entity which helps to hold the data inside the main memory or RAM. Data can be a file, a movie file,
#     a string, a integer, excel sheet, csv anything.
#     eg: a=5 here a is variable which hold 5.
#     
#     String is a combination of charecters or string is a type of information stored in variable in quotes.
#     eg: g= 'gunja'  ----here gunja is string stored in variable g
#              

# In[1]:


#if we run this and print a it gives 10 as output.
a=10
a


# In[2]:


g='gunja'
type(g)


# 3. Describe three different data types.
# Ans: 1. Int – It stores the integers values that can be positive or negative and do not contain any decimal point. eg: a=5
#      2. Float – These are floating-point real numbers that stores the decimal values. It consists of integer and fraction parts. 
#                 eg: a= 5.60
#      3. Complex – These are complex numbers specified as a real part and an imaginary part. eg: 6+5j

# 4. What is an expression made up of? What do all expressions do?
# Ans: An expression is made up of values, variables, operators and function call that always produces or returns a result value.
#      An Expression always evaluates (calculate) to itself.
#      eg: 5>3  it gives output as True
#          7*1+4  it gives output as 11.
#      
# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# Ans: spam=10, this statement performs the action of assigning the variable spam with a value of 10.
#      A statement refers to a piece of code that executes a specific instruction or tells the computer to complete a task.  A      statement can take the form of assignments, control statements, import statements, loop statements, jump statements, or method calls.
#      An expression usually refers to a piece of code that can be evaluated to a value, and is composed of variables, operators, function calls, and literals. In most programming languages, common examples of expressions are method calls and mathematical operations.

# In[3]:


#6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1


# In[6]:


#7. What should the values of the following two terms be?
'spam' + 'spamspam'


# In[5]:


'spam' * 3


# In[9]:


#8. Why is eggs a valid variable name while 100 is invalid?
eggs=10
eggs


# In[10]:


100=10
100


# 9.What three functions can be used to get the integer, floating-point number, or string version of a value?
# Ans: int() , float() , and str( ) functions.

# In[11]:


#10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'

# error is 'can only concatenate str (not "int") to str'


# In[13]:


#in order to fix this error we have to typecast the integer into string and the method are following:

'I have eaten ' + '99' +' burritos.'


# In[14]:


'I have eaten ' + str(99) + ' burritos.'


# In[ ]:




