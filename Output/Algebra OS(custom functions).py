import math
attr_list = {"sin":math.sin,
"cos":math.cos,
"tan":math.tan,
"sinh":math.sinh,
"cosh":math.cosh,
"tanh":math.tanh,
"acos":math.acos,
"atan":math.atan,
"asinh":math.asinh,
"acosh":math.acosh,
"atanh":math.atanh,
"ceil":math.ceil,
"floor":math.floor,
"abs":abs,
"fact":math.factorial}
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
def custom_function(definition,x):
    if definition.find("@f(") != -1:
        function = definition[definition.find("@f(")+3:find_nth(definition,")",definition.count(")"))-1]
        set = function[find_nth(function,"(",1)+1:find_nth(function,")",1)]
        if set.find("^") != -1:
            if set[0:set.find("^")] != "x":
                ans = int(set[0:set.find("^")])**int(set[set.find("^")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
            else:
                ans = x**int(set[set.find("^")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
        elif set.find("+") != -1:
            if set[0:set.find("+")] != "x":
                ans = int(set[0:set.find("+")])+int(set[set.find("+")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
            else:
                ans = x+int(set[set.find("+")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
        elif set.find("-") != -1:
            if set[0:set.find("-")] != "x":
                ans = int(set[0:set.find("-")])-int(set[set.find("-")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
            else:
                ans = x-int(set[set.find("-")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
        elif set.find("*") != -1:
            if set[0:set.find("*")] != "x":
                ans = int(set[0:set.find("*")])*int(set[set.find("*")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
            else:
                ans = x*int(set[set.find("*")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
        elif set.find("/") != -1:
            if set[0:set.find("/")] != "x":
                ans = int(set[0:set.find("/")])/int(set[set.find("/")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
            else:
                ans = x/int(set[set.find("/")+1:len(set)+1])
                attr = function[0:find_nth(function,"(",1)]
                if attr in attr_list:
                    attr = attr_list[attr]
                    ans = attr(ans)
                else:
                    ans="Error"
        else:
            ans = "Error"
        return ans
    else:
        return("Error")
print(custom_function("@f(tanh(3/12)+sqrt(12)))",12))