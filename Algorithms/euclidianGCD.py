def gcd(A,B):
    #A > B => A = B*Q + R
    if A < B:
        C = A
        A = B
        B = C
    R = A % B
    if R == 0:
        return B
    else:
        return gcd(B, R)
        
print(gcd(1680, 640))