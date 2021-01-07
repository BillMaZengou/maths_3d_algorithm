from vector import *
import math_tools as maths

class Matrix_3d(object):
    """create a matrix in 3d"""

    def __init__(self, c1=Vector_3d(), c2=Vector_3d(), c3=Vector_3d()):
        super(Matrix_3d, self).__init__()
        assert  type(c1) is Vector_3d and \
                type(c2) is Vector_3d and \
                type(c3) is Vector_3d
        assert c1.ifTransposed == c2.ifTransposed == c3.ifTransposed

        self.c1 = c1
        self.c2 = c2
        self.c3 = c3

        if self.c1.ifTransposed:
            self.ifTransposed = True
        else:
            self.ifTransposed = False

    def __str__(self):
        if self.ifTransposed:
            result = "[{} {} {}\n {} {} {}\n {} {} {}]"\
                    .format(self.c1.x, self.c1.y, self.c1.z,\
                            self.c2.x, self.c2.y, self.c2.z,\
                            self.c3.x, self.c3.y, self.c3.z)
        else:
            result = "[{} {} {}\n {} {} {}\n {} {} {}]"\
                    .format(self.c1.x, self.c2.x, self.c3.x,\
                            self.c1.y, self.c2.y, self.c3.y,\
                            self.c1.z, self.c2.z, self.c3.z)
        return result

    def __neg__(self):
        return Vector_3d(-self.c1, -self.c2, -self.c3)

    def __add__(self, matrix):
        assert type(matrix) is Matrix_3d
        assert matrix.ifTransposed == self.ifTransposed
        return Matrix_3d(   self.c1 + matrix.c1,
                            self.c2 + matrix.c2,
                            self.c3 + matrix.c3)

    def __sub__(self, matrix):
        assert type(matrix) is Matrix_3d
        assert matrix.ifTransposed == self.ifTransposed
        return Matrix_3d(   self.c1 - matrix.c1,
                            self.c2 - matrix.c2,
                            self.c3 - matrix.c3)

    def __mul__(self, *args):
        print(args)
        if self.ifTransposed == False:
            assert len(args) == 1
            r = args[0]
            if isinstance(r, int) or isinstance(r, float):
                return Matrix_3d(self.c1*r, self.c2*r, self.c3*r)
            elif    isinstance(r, Vector_3d) and \
                    r.ifTransposed == False:
                return self.c1*r.x + self.c2*r.y + self.c3*r.z

    def __rmul__(self, *args):
        assert len(args) == 1
        r = args[0]
        if isinstance(r, int) or isinstance(r, float):
            return self * r
        elif    isinstance(r, Vector_3d) and \
                r.ifTransposed == True   and \
                self.ifTransposed == True:
            return self.c1*r.x + self.c2*r.y + self.c3*r.z

    def __truediv__(self, const):
        return self * (1/const)

    def __eq__(self, another_matrix):
        assert type(another_matrix) is Matrix_3d
        if another_matrix.ifTransposed == self.ifTransposed:
            if (self.c1 == another_matrix.c1
            and self.c2 == another_matrix.c2
            and self.c3 == another_matrix.c3):
                return True
            else:
                return False
        else:
            if another_matrix.ifTransposed == True:
                return transposed_matrix(another_matrix) == self
            elif self.ifTransposed == True:
                return another_matrix == transposed_matrix(self)

def transposed_matrix(m):
    assert m.ifTransposed == True
    c1 = Vector_3d(m.c1.x, m.c2.x, m.c3.x)
    c2 = Vector_3d(m.c1.y, m.c2.y, m.c3.y)
    c3 = Vector_3d(m.c1.z, m.c2.z, m.c3.z)
    return Matrix_3d(c1, c2, c3)

def identity(ifTransposed=False):
    c1 = Vector_3d(1, 0, 0, ifTransposed)
    c2 = Vector_3d(0, 1, 0, ifTransposed)
    c3 = Vector_3d(0, 0, 1, ifTransposed)
    return Matrix_3d(c1, c2, c3)

def main():
    i = Vector_3d(0, 1, 0)
    j = Vector_3d(0, 0, 1)
    k = Vector_3d(1, 0, 0)
    M = Matrix_3d(i, j, k)
    print(M)
    i = Vector_3d(0, 0, 1)
    j = Vector_3d(1, 0, 0)
    k = Vector_3d(0, 1, 0)
    N = Matrix_3d(i, j, k)
    print(N)
    I = identity()
    print(I)
    print( M + I == I + M )
    print( (M+I) + N == M + (I+N) )
    a = 2
    b = 3
    print(b*M)
    print( a * (b*M) == (a*b) * M )
    print( a * (M+I) == a*M + a*I )
    print( (a+b) * M == a*M + b*M )
    v = Vector_3d(3, 4, 0)
    print( I*v )
    I_trans = identity(True)
    print( I == I_trans )
    print(I * i)
    i = Vector_3d(1, 0, 0, True)
    j = Vector_3d(0, 1, 0, True)
    k = Vector_3d(0, 0, 1, True)
    I_trans2 = Matrix_3d(i, j, k)
    print(j)
    print(I_trans2)
    # k = (I_trans2.__rmul__(j))
    k = j * I_trans2
    print( k )


if __name__ == '__main__':
    main()
