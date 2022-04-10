import math
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
def like(expression,format):
    if format == "c(c)":
        return int(expression[0:expression.find("(")])*int(expression[expression.find("(")+1:-1])
    if format == "c(ax+c)":
        return str(int(expression[0:expression.find("(")])*int(expression[expression.find("(")+1:expression.find("+")-1]))+"x+"+str(int(expression[0:expression.find("(")])*int(expression[expression.find("+")+1:-1]))
    if format == "(ax+c)(bx+c)":
        exp=[]
        if int(expression[expression.find("(")+1:expression.find("+")-1])*int(expression[expression.find(")")+2:expression.find("+",expression.find("+")+1)-1]) != 1:
            exp.append(str(int(expression[expression.find("(")+1:expression.find("+")-1])*int(expression[expression.find(")")+2:expression.find("+",expression.find("+")+1)-1]))+"x^2")
        else:
            exp.append("x^2")
        exp.append(str(int(expression[expression.find("(")+1:expression.find("+")-1])*int(expression[expression.find("+",expression.find("+")+1):expression.find(")",expression.find(")")+1)])+int(expression[expression.find(")")+2:expression.find("+",expression.find("+")+1)-1])*int(expression[expression.find("+"):expression.find(")")]))+"x")
        exp.append(str(int(expression[expression.find("+"):expression.find(")")])*int(expression[expression.find("+",expression.find("+")+1):expression.find(")",expression.find(")")+1)])))
        return exp[0]+"+"+exp[1]+"+"+exp[2]
    if format == "ax+bx":
        add=[]
        tot=0
        add.append(expression[0:find_nth(expression,"+",0)-1])
        for i in range (0,expression.count("+")):
            add.append(expression[find_nth(expression,"+",i+1)+1:find_nth(expression,"x",i+2)])
        for i in range (len(add)):
            tot+=int(add[i])
        return str(tot)+"x"
    if format == "ax-bx":
        add=[]
        tot=0
        add.append(expression[0:find_nth(expression,"-",0)-1])
        for i in range (0,expression.count("-")):
            add.append(expression[find_nth(expression,"-",i+1)+1:find_nth(expression,"x",i+2)])
        tot+=int(add[0])
        for i in range (1,len(add)):
            tot-=int(add[i])
        return str(tot)+"x"
    if format == "ax*bx":
        add=[]
        tot=0
        add.append(expression[0:find_nth(expression,"*",0)-1])
        for i in range (0,expression.count("*")):
            add.append(expression[find_nth(expression,"*",i+1)+1:find_nth(expression,"x",i+2)])
        tot+=int(add[0])
        for i in range (1,len(add)):
            tot*=int(add[i])
        return str(tot)+"x^"+str(expression.count("x"))
    if format == "(ax)/(bx)":
        add=[]
        tot=0
        add.append(expression[1:find_nth(expression,"/",0)-2])
        for i in range (0,expression.count("/")):
            add.append(expression[find_nth(expression,"/",i+1)+2:find_nth(expression,"x",i+2)])
        tot+=int(add[0])
        for i in range (1,len(add)):
            tot/=int(add[i])
        return str(tot)+"x^"+str(expression.count("x")-2)
print(like("3(5x+12)","c(ax+c)"))