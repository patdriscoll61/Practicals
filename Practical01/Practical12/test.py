

def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    return_str = []
    for i in range(1,n+1,1):
        return_str.append(s)
    return "-".join(return_str)
    #return s * n


print(repeat_string("Python",2))
#print("-".join(["Python","Python"]))