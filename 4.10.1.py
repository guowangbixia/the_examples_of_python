#this function accept a list and translate to another format.
spam=['apples','bananas','tofu','cats']
def fun(aList):
    aList[-1]='and '+aList[-1]
    string="'"
    for i in range(len(aList)-1):
        string=string+aList[i]+','
    string=string+aList[-1]+"'"
    return string
print(fun(spam))
        
