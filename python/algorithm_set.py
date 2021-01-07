from vector import *
import math_tools as maths

def triangle_area(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    return 1/2 * abs(v1.cross(v2))

def orthonormal_basis(vectors, dimension=3):
    """ Gram-Schmidt Process """
    assert len(vectors) > dimension-1
    assert type(vectors[0]) is vector_3d
    results = []
    results.append(vectors[0].unit())
    i = 1
    while i < dimension:
        e = vectors[i]
        temp = vector_3d(0, 0, 0)
        for k in range(i):
            temp += e.proj(results[k])
        results.append( (e - temp).unit() )
        i += 1
    return results

def main():
    ERROR = 10**(-10)
    A = vector_3d(1, 2, 3)
    B = vector_3d(-2, 2, 4)
    C = vector_3d(7, -8, 6)
    print(triangle_area(A, B, C))
    K = [
            vector_3d(maths.Sqrt(2)/2, maths.Sqrt(2)/2, 0),
            vector_3d(-1, 1, -1),
            vector_3d(0, -2, -2)
        ]
    K_dash = orthonormal_basis(K)
    for i in K_dash:
        print(i)
    print( K_dash[0].dot(K_dash[1])  )
    print( ((A.dot(B))**2 + abs(A.cross(B))**2 - (abs(A)**2 * abs(B)**2)) < ERROR )
    print( (A.cross(B).cross(C)) == (A.dot(B)*B - (B.dot(C))*A) )

if __name__ == '__main__':
    main()
