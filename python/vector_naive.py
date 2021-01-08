import math_tools as maths

class Vector_3d(object):
    """create a vector in 3d"""

    def __init__(self, x=0, y=0, z=0, ifTransposed=False):
        super(Vector_3d, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.ifTransposed = ifTransposed

    def __str__(self):
        if self.ifTransposed:
            return "[{} {} {}]".format(round(self.x, 3), round(self.y, 3), round(self.z, 3))
        else:
            return "[{}\n{}\n{}]".format(round(self.x, 3), round(self.y, 3), round(self.z, 3))

    def __neg__(self):
        return Vector_3d(-self.x, -self.y, -self.z, self.ifTransposed)

    def __add__(self, vector):
        assert type(vector) is Vector_3d
        assert vector.ifTransposed == self.ifTransposed
        return Vector_3d(   self.x + vector.x,
                            self.y + vector.y,
                            self.z + vector.z,
                        self.ifTransposed)

    def __sub__(self, vector):
        assert type(vector) is Vector_3d
        assert vector.ifTransposed == self.ifTransposed
        return Vector_3d(   self.x - vector.x,
                            self.y - vector.y,
                            self.z - vector.z,
                        self.ifTransposed)

    def __mul__(self, const):
        assert type(const) is int or float
        return Vector_3d(self.x*const, self.y*const, self.z*const, self.ifTransposed)

    def __rmul__(self, const):
        return self * const

    def __truediv__(self, const):
        return self * (1/const)

    def __eq__(self, another_vector):
        assert type(another_vector) is Vector_3d
        assert another_vector.ifTransposed == self.ifTransposed
        error = 10 ** (-10)
        if (abs(self.x - another_vector.x) < error
        and abs(self.y - another_vector.y) < error
        and abs(self.z - another_vector.z) < error):
            return True
        else:
            return False

    def __abs__(self):
        return maths.Sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def transpose(self):
        self.ifTransposed = not self.ifTransposed

    def unit(self):
        return self/abs(self)

    def dot(self, another_vector):
        assert type(another_vector) is Vector_3d
        assert another_vector.ifTransposed == False
        return  self.x * another_vector.x + \
                self.y * another_vector.y + \
                self.z * another_vector.z

    def cross(self, another_vector):
        assert type(another_vector) is Vector_3d
        return  Vector_3d(
                    self.y*another_vector.z - self.z*another_vector.y,
                    self.z*another_vector.x - self.x*another_vector.z,
                    self.x*another_vector.y - self.y*another_vector.x
                )

    def proj(self, project_to):
        assert type(project_to) is Vector_3d
        return self.dot(project_to)/abs(project_to) * project_to.unit()

    def perp(self, perpendicular_to):
        assert type(perpendicular_to) is Vector_3d
        return self - self.proj(perpendicular_to)

def main():
    ERROR = 10**(-10)
    # Verify Vector properties
    P = Vector_3d(1, 1, 1)
    Q = Vector_3d(2, 3, 3)
    print( (P + Q) == (Q + P) )
    R = Vector_3d(3, 4, 5)
    print( ((P+Q) + R) == (P + (Q+R)) )
    a = 2
    b = 3
    print( ((a*b) * P) == (a * (b*P)) )
    print( (a * (P+Q)) == (a*P + a*Q) )
    print( ((a+b) * P) == (a*P + b*P) )
    print("-"*10)
    # Verify the abs of vector
    V = Vector_3d(3, 4, 0)
    print(abs(V))
    print(abs(a*V) == abs(a)*abs(V))
    print(abs(P+Q) <= abs(P) + abs(Q))
    print("-"*10)
    # Verify the dot product
    print( P.dot(Q) == Q.dot(P) )
    print( (a*P).dot(Q) == a*(Q.dot(P)) )
    print( P.dot(Q+R) == P.dot(Q) + P.dot(R) )
    print( abs(P.dot(P) - abs(P)**2) < ERROR )
    print( abs(P.dot(Q)) <= abs(P)*abs(Q) )
    print("-"*10)
    # Verify unit vector
    S = Vector_3d(2, 0, 0)
    print(S.unit())
    print("-"*10)
    # Verify vector projection and perpendicularity
    print(Q.proj(S))
    print(Q.perp(S))
    print("-"*10)
    # Verify the cross product
    T = Vector_3d(0, 1, 0)
    print(S.cross(T))
    print(T.cross(S))
    print( abs(P.cross(Q).dot(P) - 0) <  ERROR )
    print( abs(P.cross(Q).dot(Q) - 0) <  ERROR )
    print( Q.cross(P) == -(P.cross(Q)) )
    print( (a*P).cross(Q) == a*(P.cross(Q)) )
    print( P.cross(Q+R) == P.cross(Q) + P.cross(R) )
    Z = Vector_3d(0, 0, 0)
    print( P.cross(P) == Z )
    print( P.cross(Q).dot(R) == R.cross(P).dot(Q) == Q.cross(R).dot(P) == -Q.cross(P).dot(R) )
    print( P.cross(Q.cross(P)) == P.cross(Q).cross(P) == (P.dot(P)*Q - P.dot(Q)*P) )
    print( P.cross(Q).cross(R) != P.cross(Q.cross(R)) )
    print("-"*10)

if __name__ == '__main__':
    main()
