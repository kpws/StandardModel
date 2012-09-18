import pylab as pl
import numpy as np
from partonPDF import pdf, partons
from scipy.integrate import quad
import particles

alpha=7.2973525698e-3
barnPerInvGeV2 = 0.000389379203
mz=91.
Gz=2.5

col=['b','r']
i=0
for Ecm2 in [16000000,64000000]:
    dsigmadM2 = []
    dsigmadM2Z = []
    M2s =  np.exp(np.linspace(np.log(10), np.log(Ecm2*2), 1000))
    for M2 in M2s:
        ZFactor=1+M2*(2*M2-mz**2)/((M2-mz**2)**2+mz**2*Gz**2)
        dsigmadM2.append(
                quad(lambda x: 4.*np.pi*alpha**2/(3*M2*Ecm2*x)*
                    sum(pdf[Ecm2][q](x)*pdf[Ecm2][q+'bar'](M2/(Ecm2*x))*particles.quarkCharge[q]**2
                        for q in particles.quarks)
                    ,M2/Ecm2,1)[0]*barnPerInvGeV2)
        dsigmadM2Z.append(dsigmadM2[-1]*ZFactor)
    pl.loglog(M2s, dsigmadM2,'--', label='$\\sqrt{s}='+str(np.sqrt(Ecm2)/1e3)+'\\ \\mathrm{TeV}$, no Z',color=col[i])
    pl.loglog(M2s, dsigmadM2Z,'-', label='$\\sqrt{s}='+str(np.sqrt(Ecm2)/1e3)+'\\ \\mathrm{TeV}$',color=col[i])
    i+=1
pl.xlabel('$M^2\\ \\mathrm{[GeV^2]}$')
pl.ylabel('$\mathrm{d}\sigma/\mathrm{d}M^2\\ \\mathrm{[b/GeV^2]}$')
pl.legend(loc=1)
pl.savefig('cc.pdf', bbox_inches=0)
pl.show()
