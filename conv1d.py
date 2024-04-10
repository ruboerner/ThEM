def conv1d(y,z):
    N=len(y)
    M=len(z)
    erg=np.zeros(N+M-1)
    for k in range(0,N+M-1):
        sum=0
        for j in range (0,N-1):
            if ((k-j>=0) & (k-j<M)):
                sum=sum+y[j]*z[k-j]
        erg[k]=sum
    return erg