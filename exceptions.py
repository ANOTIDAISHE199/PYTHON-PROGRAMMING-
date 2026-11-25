def safer_float(object):
    return_value = 0

    try:
        if ((type(object) != str and type(object) != int) ):
            ex = invalid_type("incorrect type","cant convert invalid type")
            raise ex
        return_value = float(object)
    except invalid_type:
        return_value = ex.error
    except ValueError:
        return_value = "your string is not valid"
    else: 
        print("no errors")
    return return_value

class invalid_type(Exception):
    def __init__(self, message,errors):

        super().__init__(message)

        self.error = errors

#safer_float(21)
#safer_float(45)
safer_float("xyz")
safer_float([1,3,4])