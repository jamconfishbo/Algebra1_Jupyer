from IPython.display import display, Latex


#a class that can allow user to more easily manipulate math expressions and reprint them in latex

class LWorks:
    ## takes in string and prints basic algebraic equation in Latex (could already have latex input)
    ## continue to edit as you make more comlicated equations
    def __init__(self):
        pass
    
    def printequation(str):

            #if str is already in latex syntax
        if "$" in str or r"\[" in str:
            display(Latex(str))
            return

            #puts it into latex syntax and displays
        else:   

            #if the equation is linear

            numvars = vars(str)[0]


    #search for number of variables and returns the varible
    def vars(str):
        str = str.lower()

        exceptions = ["cos", "sin", "tan", "cotan", "e^", "arcsin","arccos", "arctan", "sec","csc", "int", "sum", "prod", "lim", "inf"]
        for k in exceptions:
            str = str.replace(k,"")

        alphabet = ["a","b","c","d","e","f","g","h","i", "j","k","l","m", "n", "o", "p", "q","r","s","t","u","v","w","x","y","z"]
        numvars = 0
        vars = []
        for i in alphabet:
            if i in str:
                numvars = numvars+1
                vars.append(i)
        return numvars, vars
