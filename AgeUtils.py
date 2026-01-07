def AgeVerification(a):
    try:
        a = int(a)
    except (ValueError):
        return "Only integers are allowed"
    
    if (a < 18 and a >= 0):
        return "You are a child"
    elif (a == 69):
        return "Nice!"
    elif (a >= 18 and a < 70):
        return "You are an adult"
    elif (a >= 70):
        return "You are retired"
    else:
        return "Please enter a positive number"
    
# JANNE VILJANEN TKM24
