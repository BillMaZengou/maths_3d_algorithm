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
    A = vector_3d(1, 2, 3)
    B = vector_3d(-2, 2, 4)
    C = vector_3d(7, -8, 6)
    print(triangle_area(A, B, C))
    B = [
            vector_3d(maths.Sqrt(2)/2, maths.Sqrt(2)/2, 0),
            vector_3d(-1, 1, -1),
            vector_3d(0, -2, -2)
        ]
    B_dash = orthonormal_basis(B)
    for i in B_dash:
        print(i)
    print( B_dash[0].dot(B_dash[1])  )

if __name__ == '__main__':
    main()
