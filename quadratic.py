# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    d=(b**2-4*a*c)
    if d<0:
        return "( )"
    else:
     raiz=d**0.5
     r1=(-b+raiz)/2*a
     r2=(-b-raiz)/2*a
     if r1==r2:
        return f"({r1})"
     else:
        return f"({r1}, {r2})"



def value_y(a, b, c, x):
    y=a*x**2+b*x+c
    return y


def to_string(a, b, c):
    f=""
    if a==0:
        if b==0:
            f = f"f(x) = {c}"
        else:
            f = f"f(x) = {b} * X + {c}"
    elif b==0:
        f = f"f(x) = {a} * X^2 + {c}"
    elif c==0:
        f = f"f(x) = {a} * X^2 + {b} * X"
    else:
        f=f"f(x) = {a} * X^2 + {b} * X + {c}"
    return f


def derivation(a, b, c):
    f=""
    term1=" "
    term2=" "
    if a !=0:
        if b !=0:
          f=f"f'(x) = {a*2} * X + {b}"
        else:
            f=f"f'(x) = {a*2} * X"
    elif b != 0:
             f=f"f'(x) = {b}"
    else:
        f="f'(x) = 0"
    return f

var=roots(1, -3, 2)
print(var)
