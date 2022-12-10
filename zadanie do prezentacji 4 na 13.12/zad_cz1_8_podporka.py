'''
Program ze stacka sprawdzajacy czy punkt jest wewnatrz na podstawie:
https://www.geeksforgeeks.org/check-whether-a-given-point-lies-inside-a-triangle-or-not/

Skupiamy sie na przykladzie: https://www.medianauka.pl/zadanie-1126
'''

def area(x1, y1, x2, y2, x3, y3):
    return round(abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0),3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):
    # Calculate area of triangle ABC
    A = abs(area(x1, y1, x2, y2, x3, y3))

    # Calculate area of triangle PBC
    A1 = abs(area(x, y, x2, y2, x3, y3))

    # Calculate area of triangle PAC
    A2 = abs(area(x1, y1, x, y, x3, y3))

    # Calculate area of triangle PAB
    A3 = abs(area(x1, y1, x2, y2, x, y))

    # Check if sum of A1, A2 and A3
    # is same as A
    if (A == A1 + A2 + A3):
        return True                 #tzn. ze pkt lezy w srodku
    else:
        return False

if (isInside(1, 1, 4, -2, -0.1, -3.1, 2, -1.84)):
    print('Inside')
else:
    print('Not Inside')
