from particles import *

sin2ThetaW=0.2312
colors=3

nu=.5**2
vis= 3*( (-.5-sin2ThetaW*-1)**2  +(sin2ThetaW)**2)
for q in quarks:
    if mass[q]*2<mass['Z']:
        vis+=colors*((.5 if q in upType else -.5)-sin2ThetaW*charge[q])**2
        vis+=colors*(-sin2ThetaW*charge[q])**2
totExp=2490. #MeV
visExp=1992. #MeV
print (totExp-visExp)/(nu*(visExp/vis))
