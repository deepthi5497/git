"""
finding 1/x
"""


def one_by_x(number):
    """returns 1/x"""
    try:
        return 1/number
    except TypeError:
        print "enter a valid integer value to find 1/x..."
        return "TypeError"
    except ZeroDivisionError:
        print "enter value other than zero for x.."
        return "ZeroDivisionError"
