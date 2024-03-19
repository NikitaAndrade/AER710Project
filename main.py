import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import sympy as sp

#variable declaration
oblique_shock = 3
normal_shock = 1
M1 = 3.2
M4 = 1.3 
gamma = 1.4 

# B1, B2, B3, M2, M3 = sp.symbols('B1 B2 B3 M2 M3')

# #Normal Upstream Mach Numbers
# Mn1 = M1*sp.sin(B1); Mn2 = M2*sp.sin(B2); Mn3 = M3*sp.sin(B3)

# #Flow Turning Angles
# theta1 =  sp.atan((((2*(1/sp.cot(B1))))*(M1**2*sp.sin(B1)**2-1))/((gamma-1)*M1**2-(2*(M1**2*sp.sin(B1)-1))))
# theta2 =  sp.atan((((2*(1/sp.cot(B2))))*(M2**2*sp.sin(B2)**2-1))/((gamma-1)*M2**2-(2*(M2**2*sp.sin(B2)-1))))
# theta3 =  sp.atan((((2*(1/sp.cot(B3))))*(M3**2*sp.sin(B3)**2-1))/((gamma-1)*M3**2-(2*(M3**2*sp.sin(B3)-1))))

# #Mach number
# M2_down = sp.sqrt(((gamma-1)*Mn1**2+2)/(2*gamma*Mn1**2-(gamma-1)))*(1/(sp.sin(B1-theta1)))
# M3_down = sp.sqrt(((gamma-1)*Mn2**2+2)/(2*gamma*Mn2**2-(gamma-1)))*(1/(sp.sin(B2-theta2)))
# M4_down = sp.sqrt(((gamma-1)*Mn3**2+2)/(2*gamma*Mn3**2-(gamma-1)))*(1/(sp.sin(B3-theta3)))

# equations =  [Mn1 - Mn2, Mn1 - Mn3, M2 - M2_down, M3 - M3_down, M4 - M4_down]

# solution = sp.solve(equations, (B1, B2, B3, M2, M3))
# print(solution)


def beta_check(i,M,Mnshock,shocknumber):
    B = np.deg2rad(i)
    theta =  np.arctan((((2*(1/np.tan(B))))*(M**2*(np.sin(B)**2)-1))/((gamma+1)*M**2-(2*(M**2*np.sin(B)**2-1))))
    if M == 0:
        M = np.sqrt(((gamma-1)*Mnshock**2+2)/(2*gamma*Mnshock**2-(gamma-1)))*(1/(np.sin(B-theta)))
    Mn = round(M*np.sin(B),4)
    B = np.rad2deg(B)
    theta = np.rad2deg(theta)
    return(B, theta, M, Mn)

correctness_check = 100

while correctness_check == 100:
    for i in range(0,90):
        Beta1,Theta1, M1, Mn1 = beta_check(i, M1, 0, 1)
        for j in range(0,90):
            Beta2, Theta2, M2, Mn2 = beta_check(j, 0, Mn1, 2)
            for k in range(0,90):
                Beta3, Theta3, M3, Mn3 = beta_check(k, 0, Mn2, 3)
                if abs(Mn1 - Mn2) < 0.001 and abs(Mn1 - Mn3) < 0.001:
                    print('The values found were:',Mn1, Mn2, Mn3)
                    print('M2 is:', M2, 'M3 is:', M3,  'Shockwave Angle 1:', Beta1, 'Shockwave Angle 2:', Beta2, 'Shockwave Angle 3:', Beta3)
                    correctness_check = 0
            