# -*- coding: utf-8 -*-
"""
Calcolo del determinante attraverso la regola di Laplace

Esercizi per l'esame di calcolo numerico
"""

import numpy as np

def mydet(A):
    (m,n)=A.shape
    if m!=n:
        print("A non e' quadrata")
        return
    if n==1:
        return A
    else:
        d=0
        for j in range(0,n):
            temp=np.delete(A,0,axis=0)
            temp=np.delete(temp,j,axis=1)
            d=d+(-1)**(1+(j+1))*A[0,j]*mydet(temp)
        return d
