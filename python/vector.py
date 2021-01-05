class vector_3d(object):
    """create a vector in 3d"""

    def __init__(self, x, y, z, ifTransposed=False):
        super(vector_3d, self).__init__()
        self.x = x
        self.y = y
        self.z = z
        self.ifTransposed = ifTransposed

    def __str__(self):
        if self.ifTransposed:
            return "[{}\t{}\t{}]".format(self.x, self.y, self.z)
        else:
            return "[{}\n{}\n{}]".format(self.x, self.y, self.z)

    def __mul__(self, const):
        assert type(const) is not vector_3d
        return vector_3d(self.x*const, self.y*const, self.z*const, self.ifTransposed)

    def __rmul__(self, const):
        return self * const

    def __add__(self, vector):
        assert type(vector) is vector_3d
        assert vector.ifTransposed == self.ifTransposed
        return vector_3d(   self.x + vector.x,
                            self.y + vector.y,
                            self.z + vector.z,
                        self.ifTransposed)

    def __sub__(self, vector):
        assert type(vector) is vector_3d
        assert vector.ifTransposed == self.ifTransposed
        return vector_3d(   self.x - vector.x,
                            self.y - vector.y,
                            self.z - vector.z,
                        self.ifTransposed)

    def __eq__(self, another_vector):
        assert type(another_vector) is vector_3d
        assert another_vector.ifTransposed == self.ifTransposed
        if (self.x == another_vector.x
        and self.y == another_vector.y
        and self.z == another_vector.z):
            return True
        else:
            return False

    def transpose(self):
        self.ifTransposed = not self.ifTransposed

def main():
    P = vector_3d(1, 1, 1)
    Q = vector_3d(2, 2, 2)
    print( (P + Q) == (Q + P) )
    R = vector_3d(3, 3, 3)
    print( ((P + Q) + R) == (P + (Q + R)) )
    a = 2
    b = 3
    print( ((a*b) * P) == (a * (b*P)) )


if __name__ == '__main__':
    main()
