#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 20:03:58 2021

@author: vsriya23
"""

class Stack:
    '''implementing a minimalist Stack class with basic methods like pop(), push()...'''
    def __init__(self, size):
        self.stack = []
        self.size = size
        
    def push(self, element):
        if len(self.stack) < self.size:
            self.stack.append(element)
        
    def pop(self):
        
        last_element = self.stack[-1]
        self.stack = self.stack[:-1]
        
        return last_element
    
    def peek(self):
        
        return self.stack[-1]
    
    def is_Full(self):
        if len(self.stack) == self.size:
            return True
        else:
            return False
        
    def is_Empty(self):
        if len(self.stack) == 0:
            return True
        
        else:
            return False
    def __str__(self):
        
        return str(self.stack)
    
    
#%%   defining functions     
   

def StrtoList(exp):
    
    '''To convert the infix string to a list 
    Example: 
        infix = '3^4/(5*6)+10' 
        output = ['3', '^', '4', '/', '(', '5', '*', '6', ')', '+', '10']
        
    '''
    
    dig = '0123456789'
    ops = ['+' , '-', '/', '*', '^', ')']
    nums_list= []
    num = ''
    
    for idx in range(len(exp)):
        i = exp[idx]

        if i in dig:
            if idx != len(exp)-1:
                num = num + i
            else:
                num = num + i
                nums_list.append(num)
        elif i in ops:
            if len(num) != 0:
                nums_list.append(num)
                num = ''
                nums_list.append(i)
            else:
                nums_list.append(i)
            
        elif i =='(' :
            nums_list.append(i)
            
            
    return nums_list




def InfixtoPostfix(exp_str):
    
    '''convert infix format(string) to postfix format( list)
    Example:
    Infix =  '3^4/(5*6)+10' 
    Postfix Expression:  ['3', '4', '^', '5', '6', '*', '/', '10', '+']
    '''
    
    precedence = {'+' : 1, '-':1, '/':2, '*':2, '^': 3, '(': 1, ')':1}
    exp_stack = Stack(len(exp_str)) # creating an instance of a Stack
    nums_list= StrtoList(exp_str) # converting infix string to a list
    postfix_exp = []
    
    for ch in nums_list:
        if ch not in precedence:
            postfix_exp.append(ch)
        
        
        elif ch in precedence and ch != '(' and ch != ')':
            
            while not exp_stack.is_Empty():
                # print(exp_stack)
                if precedence[exp_stack.peek()] >= precedence[ch]:

                    postfix_exp.append(exp_stack.pop())
                else: 
                    
                    break
                    
            exp_stack.push(ch)    
            
        elif ch == '(':
            exp_stack.push(ch)
            
        elif ch == ')':
            
            while exp_stack.peek() != '(':
                # print(exp_stack.peek())
                postfix_exp.append(exp_stack.pop())
                # print(exp_stack.peek())
            exp_stack.pop()
    #print(exp_stack)    
    while not exp_stack.is_Empty():
        postfix_exp.append(exp_stack.pop())
              
    return postfix_exp    
    


def doOperation(x,y, opr):
    '''defining the operations for each operator in string format'''
    
    
    if opr == '+':
        return x+y
    elif opr == '-':
        return x-y
    elif opr == '*':
        return x*y
    elif opr == '^':
        return x**y
    elif opr == '/':
        return x/y
    

def EvaluatePostfix(postfix):
    
    ''' function for evaluating postfix expression
    Example:
        postfix = ['3', '4', '^', '5', '6', '*', '/', '10', '+']
        Value of expression:  12.7
    
    '''
    operands = Stack(len(postfix))
    operators = ['+' , '-', '/', '*', '^' ]
    
    for ch in postfix:
        if ch not in operators:
            
            operands.push(int(ch))
            
        else:
            op2 = operands.pop()
            op1 = operands.pop()
            operands.push(doOperation(op1, op2, ch))
    return operands.pop()        
#%%  

if __name__ == '__main__':      
    infix1 =  '3^4/(5*6)+10'  
    postfix1 =InfixtoPostfix(infix1)
    
    print('Postfix Expression: ', postfix1)      
    
    print('Value of expression: ', EvaluatePostfix((postfix1)))    

    infix2 = '5+6*7/9'
    postfix2 = InfixtoPostfix(infix2)
    print(postfix2)
    print(EvaluatePostfix(postfix2))