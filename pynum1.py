#!/usr/bin/python3

import numpy as np
import sys
choice=int(input("For array press1 orr to exit press 0"))
while True:
    if choice==1 :
        
            m=np.random.randint(low=1,high=10,size=(3,2))
            print(m)
            np.savetxt("a.txt",m)
            np.loadtxt("a.txt")
            
    else :
        sys.exit
