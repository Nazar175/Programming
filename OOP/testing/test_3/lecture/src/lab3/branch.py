def fun_with_if_else(x):
    result = "Zero"
    if x > 0:
        result = "Positive"
    
    if x < 0:
        result = "Negative"

    return result


def fun_with_if_only(x):
    result = "Non-positive"
    if x > 0:
        result = "Positive"
    return result
