# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:15:17 2022

@author: Jon

Find the radius of the circle inside the unit square 
that has the property that the average distance of points 
inside the circle to the center of the square is the same 
as the average distance of points outside the circle to the 
nearest edge of the square.  

"""

import numpy as np

def finddistance(cords):
     ex = cords[0]
     ey = cords[1]
     d = np.sqrt(((ex)**2)+((ey)**2))
     return d
 

ds = []
for y in np.arange(0,.5, step=.01):
    d = finddistance([.5, y])
    ds.append(d/2)
print(np.mean(ds))

#added values
averagein,averageout= 9,0
d = .2027
passed = 0


while passed != 100:
    
   xay = np.zeros((100,2))
   xay = np.random.uniform(0,0.5,size = (200,2))
    
   d2center = []
   d2edge = []
   inside= 0
   
   for i in range(200):
       if np.sqrt(xay[i][0]**2+xay[i][1]**2) <= d  :
            inside+=1
            d2center.append(finddistance(xay[i]))
       else:
            d2edge.append(min(.5-xay[i][0],.5-xay[i][1]))
            
   print(np.mean(d2center))
   averagein =np.mean(d2center)
   print(np.mean(d2edge))
   averageout =np.mean(d2edge)
   
   if abs(averagein - averageout)< 0.0001:
        passed = 100
        break
   elif averagein< averageout:
        d+=.000001
   elif averagein > averageout:
        d-=.000001
        
   print("failed")
   print(f"d is now {d}")
   
print('\n\n' , f"d is now {d}")
