from IPython.display import display, Latex
from fractions import Fraction
import random

#for converting string fractions into floating points
def convert_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        try:
            num, denom = frac_str.split('/')
        except ValueError:
            return None
        try:
            leading, num = num.split(' ')
        except ValueError:
            return float(num) / float(denom)        
        if float(leading) < 0:
            sign_mult = -1
        else:
            sign_mult = 1
        return float(leading) + sign_mult * (float(num) / float(denom))
#eq is a tuple of tuples, first component left side of equal sign, sencond component right side    
def latexify(eq):  
    #exceptions = ["cos", "sin", "tan", "cotan", "e^", "arcsin","arccos", "arctan", "sec","csc", "int", "sum", "prod", "lim", "inf"]
    str = ""
    for i in range(2):
        for k in range(len(eq[i])):        
            if k == 0:
                 str = str +eq[i][k]
            else:
                str = str + "+"+eq[i][k]
        if i ==1:
            continue
        str = str + " & ="
    return str    
def doquestion():
    #randomly asined coeficnts and variables
    a = random.randrange(1,10)
    b = random.randrange(1,10)
    c = random.randrange(10)

    #this is the equation
    #eq = f"{a}x+{b} = {c}"
    eq= ((str(a)+"x",str(b)),(str(c),))
   
    cont = False
    while cont == False:
        #student chooses which step to do first, all steps can lead to correct answer
        
        #displays options
        display(Latex(r"$ \Huge \begin{align}" +latexify(eq) +r" \end{align}$"))
        display(Latex(r"$ \Large \text{What do you want to do?} $"))
        display(Latex(r"$ \Large \text{a) add} $"))
        display(Latex(r"$ \Large \text{b) subtract} $"))
        display(Latex(r"$ \Large \text{c) multiply} $"))
        display(Latex(r"$ \Large \text{d) divide} $"))

        step = str(input())
        step = step.lower()
        if step == "a":
            cont = True
            cont1 = False
            while cont1 == False: 
                eq = add(eq)  
                display(Latex(r"$ \Huge \begin{align}" +latexify(eq) +r" \end{align} $"))
                display(Latex(r"$ \Large \text{What do you want to do next?} $"))
                display(Latex(r"$ \Large \text{a) multiply} $"))
                display(Latex(r"$ \Large \text{b) divide} $"))
                step = str(input())
                step = step.lower()
                if step == "a":
                    eq = mult(eq)
                if step == "b":
                    eq = div(eq)
                else:
                    display(Latex(r"$ \Large \text{Try again!} $"))     

        elif step == "b":
            cont = True
            cont1 = False
            while cont1 == False: 
                eq = sub(eq)  
                display(Latex(r"$ \Huge \begin{align}" +latexify(eq) +r" \end{align}$"))
                display(Latex(r"$ \Large \text{What do you want to do next?} $"))
                display(Latex(r"$ \Large \text{a) multiply} $"))
                display(Latex(r"$ \Large \text{b) divide} $"))
                step = str(input())
                step = step.lower()
                if step == "a":
                    eq = mult(eq)
                if step == "b":
                    eq = div(eq)
                else:
                    display(Latex(r"$ \Large \text{Try again!} $"))

        elif step =="c":
            cont = True
            cont1 = False
            while cont1 == False: 
                eq = mult(eq)  
                display(Latex(r"$ \Huge \begin{align}" +latexify(eq)+r"\end{align} $"))
                display(Latex(r"$ \Large \text{What do you want to do next?} $"))
                display(Latex(r"$ \Large \text{a) add} $"))
                display(Latex(r"$ \Large \text{b) subtract} $"))
                step = str(input())
                step = step.lower()
                if step == "a":
                    eq = add(eq)
                if step == "b":
                    eq = sub(eq)
                else:
                    display(Latex(r"$ \Large \text{Try again!} $"))

        elif step == "d":
            cont = True
            cont1 = False
            while cont1 == False: 
                eq = div(eq)  
                display(Latex(r"$ \Huge \begin{align}" +latexify(eq) +r" \end{align}$"))
                display(Latex(r"$ \Large \text{What do you want to do next?} $"))
                display(Latex(r"$ \Large \text{a) add} $"))
                display(Latex(r"$ \Large \text{b) subtract} $"))
                step = str(input())
                step = step.lower()
                if step == "a":
                    eq = add(eq)
                if step == "b":
                    eq = sub(eq)
                else:
                    display(Latex(r"$ \Large \text{Try again!} $"))
        else:
            display(Latex(r"$ \Large \text{Try again!} $"))
    display(Latex(r"$\Large \text{Good Job! Lets try another problem!}"))
def extractcoeff(str): 
    if len(str) ==1:
        if str[0] == "0" or  str[0] == "1" or  str[0] == "2" or  str[0] == "3" or  str[0] == "4" or  str[0] == "5" or  str[0] == "6" or  str[0] == "7" or  str[0]  == "8" or  str[0] == "9":
            return str
        #assuming its a variable with one for the coefficient
        else:
            return "1"
           
    k = 0
    coeff = ""
    while str[k] == "0" or  str[k] == "1" or  str[k] == "2" or  str[k] == "3" or  str[k] == "4" or  str[k] == "5" or  str[k] == "6" or  str[k] == "7" or  str[k]  == "8" or  str[k] == "9" or  str[k] == "/": 
        coeff = coeff+ str[k]
        k= k+1
        
        #special case for the last char  in the string
        if k == len(str)-1:
            if str[k] == "0" or  str[k] == "1" or  str[k] == "2" or  str[k] == "3" or  str[k] == "4" or  str[k] == "5" or  str[k] == "6" or  str[k] == "7" or  str[k]  == "8" or  str[k] == "9": 
                coeff = coeff+ str[k]
                break
            else:
                break
    return coeff
def add(eq):
    #ok what do you want to add to both sides?
    display(Latex(r"$ \Large \text{ok what do you want to add to  both sides?} $"))
    
    k=r"$\Huge \begin{align}"+latexify(eq)+r"\\ \color{blue}{+?} & \ \ \ \ \ \ \  \color{blue}{+?}  \end{align}$"
    display(Latex(k))
    
    
    # user input what to add to both sides
    add = str(input())
    nextstep = False
    while(nextstep == False):    
        if add == str(-1*Fraction(extractcoeff(eq[0][1]))):
            nextstep = True
            break
        
        #more advanced feedback later
        else:
            display(Latex(r"$ \Large \text{Try again! Get rid of the terms furthest from the x} $"))
            t=r"$\Huge \begin{align}"+ latexify(eq)+r"\\ \color{blue}{+?} & \ \ \ \ \ \ \  \color{blue}{+?}  \end{align}$"
            display(Latex(t))
            sub = str(input())
    
    
    nextstep = False
    display(Latex(r"$\Huge \color{green}{Good!}$"))
    
    #for reducing left hand side
    while nextstep == False:
        display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+r" \\ \color{blue}{+"+add+r"} & \ \ \ \ \ \ \  \color{blue}{+"+add+ r"}  \end{align}$"))         
        display(Latex(r"$\Huge \ \ \uparrow$"))
        display(Latex(r"$\Large \text{What does the left side reduce to?}$"))
    
        reduc = str(input())
        ## if correct
        case1 = eq[0][0]
        case2 = eq[0][0]
        if extractcoeff(eq[0][0]) == "-1":
            case1 = "-x"
        if extractcoeff(eq[0][0]) == "1":
            case2 = "x"
        
        #if they are correct
        if(reduc == extractcoeff(eq[0][0])+"x" or reduc == case1 or reduc == case2):
            eq= ((eq[0][0],),(eq[1][0],))
            
            display(Latex(r"$\Huge \color{green}{Good!}$"))   
            display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+r" \\  & \ \ \ \ \ \ \  \color{blue}{+"+add+ r"}  \end{align}$"))    
            nextstep == True      
            break
                    
        ## if wrong            
        else:
            display(Latex(r"$\Huge \text{Try again}$"))
    
    #for reducing right hand side
    
    while nextstep == False:    
        display(Latex(r"$\Huge  \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \;\uparrow$"))
        display(Latex(r"$\Large \text{What does the right side reduce to?}$"))
    
        reducright = str(input())
        ## if correct
        right = Fraction(Fraction(extractcoeff(eq[1][0])) + Fraction(add))
        
        #if they answer correctly
        if(reducright  == str(right)):

            eq = ((eq[0][0],), (str(right),))
            display(Latex(r"$\Huge \color{green}{Good!}$"))   
            display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+ " \end{align}$"))    
            nextstep == True
            return eq      
            break
                    
        ## if wrong            
        else:
            display(Latex(r"$\Huge \text{Try again}$"))
            display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+r" \\  & \ \ \ \ \ \ \  \color{blue}{+"+add+ r"}  \end{align}$"))       
def sub(eq):
    #ok what do you want to add to both sides?
    display(Latex(r"$ \Large \text{ok what do you want to subtract from  both sides?} $"))
    
    k=r"$\Huge \begin{align}"+latexify(eq)+r"\\ \color{blue}{-?} & \ \ \ \ \ \ \  \color{blue}{-?}  \end{align}$"
    display(Latex(k))
    
    
    # user input what to subtract from both sides
    sub = str(input())
    nextstep = False
    while(nextstep == False):    
        if sub == str(Fraction(extractcoeff(eq[0][1]))):
            nextstep = True
            break
        
        #more advanced feedback later
        else:
            display(Latex(r"$ \Large \text{Try again! Get rid of the terms furthest from the x} $"))
            t=r"$\Huge \begin{align}"+ latexify(eq)+r"\\ \color{blue}{-?} & \ \ \ \ \ \ \  \color{blue}{-?}  \end{align}$"
            display(Latex(t))
            sub = str(input())
    
    
    nextstep = False
    display(Latex(r"$\Huge \color{green}{Good!}$"))
    
    #for reducing left hand side
    while nextstep == False:
        display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+r" \\ \color{blue}{-"+sub+r"} & \ \ \ \ \ \ \  \color{blue}{-"+sub+ r"}  \end{align}$"))         
        display(Latex(r"$\Huge \ \ \uparrow$"))
        display(Latex(r"$\Large \text{What does the left side reduce to?}$"))
    
        reduc = str(input())
        ## if correct
        case1 = eq[0][0]
        case2 = eq[0][0]
        if extractcoeff(eq[0][0]) == "-1":
            case1 = "-x"
        if extractcoeff(eq[0][0]) == "1":
            case2 = "x"
        ### continue editing from here
        
        if(reduc == extractcoeff(eq[0][0])+"x" or reduc == case1 or reduc == case2):
            eq= ((eq[0][0],),(eq[1][0],))
            
            display(Latex(r"$\Huge \color{green}{Good!}$"))   
            display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+r" \\  & \ \ \ \ \ \ \  \color{blue}{-"+sub+ r"}  \end{align}$"))    
            nextstep == True      
            break
                    
        ## if wrong            
        else:
            display(Latex(r"$\Huge \text{Try again}$"))
    
    #for reducing right hand side
    
    while nextstep == False:    
        display(Latex(r"$\Huge  \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \; \;\uparrow$"))
        display(Latex(r"$\Large \text{What does the right side reduce to?}$"))
    
        reducright = str(input())
        ## if correct
        right = Fraction(Fraction(extractcoeff(eq[1][0])) - Fraction(sub))
        
        #if they answer correctly
        if(reducright  == str(right)):

            eq = ((eq[0][0],), (str(right),))
            display(Latex(r"$\Huge \color{green}{Good!}$"))   
            display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+ " \end{align}$"))    
            nextstep == True
            return eq      
            break
                    
        ## if wrong            
        else:
            display(Latex(r"$\Huge \text{Try again}$"))
            display(Latex(r"$\Huge \begin{align}"+ latexify(eq)+r" \\  & \ \ \ \ \ \ \  \color{blue}{-"+sub+ r"}  \end{align}$"))   
def mult(eq):
    pass    
def div(eq):
    pass
#n is the number of questions
#this is the main function that runs all of the questions
def startquestions(n):
    for i in range(n):
        doquestion()
n =1    

startquestions(n)