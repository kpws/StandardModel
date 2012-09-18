import pylab as pl
import numpy as np
from partonPDF import pdf, partons
from scipy.integrate import quad

quarkCharge={'up':2./3,
             'upbar':-2./3,
             'down':-1./3,
             'downbar':1./3,
             'strange':-1/3,
             'charm':2./3,
             'top':2./3,
             'bottom':-1./3,
             'gluon':0}
for q in [0.001,1,100,10000]:
    #x=np.linspace(0,1,1000)
    #for p in partons:
    #    pl.plot(x, pdf[q][p](x)/x, label=p)
    #pl.legend()
    #pl.show()

    totProb=dict()
    meanX=dict()
    nvq=['up','down']
    for p in partons:
        if p in nvq:
            totProb[p]=quad(lambda x: (pdf[q][p](x)-pdf[q][p+'bar'](x))/x, 0, 1)
        meanX[p]=quad(lambda x: pdf[q][p](x), 0, 1)
    print(q)
    print('Parton & t asymmetry & Charge contribution & Energy contribution\\\\')
    print('\\hline')
    for p in partons:
        if 'bar' in p:
            name='$\\bar{'+p[0]+'}$'
        elif p in ['charm', 'bottom', 'strange']:
            name='$'+p[0]+', \\bar{'+p[0]+'}$'
        else:
            name='$'+p[0]+'$'
        if p in nvq:
            print(name+' & %.4f'%totProb[p][0]+' & %.4f'%(totProb[p][0]*quarkCharge[p])+' & %.4f'%meanX[p][0]+' \\\\')
        else:
            print(name+' & - & - & %.4f'%meanX[p][0]+'\\\\')
    print('Total & %.4f'%sum(totProb[p][0] for p in nvq)+' & %.4f'%sum(totProb[p][0]*quarkCharge[p] for p in nvq)+
            ' & %.4f'%sum(meanX[p][0]*(2 if p in ['charm', 'bottom', 'strange'] else 1) for p in partons))
    #print sum(meanX[p][0] for p in partons+['charm','strange','bottom'])
    #print sum(totProb[p][0]*quarkCharge[p] for p in ['up','down','upbar','downbar'])

