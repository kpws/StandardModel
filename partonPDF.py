import csv
from scipy.interpolate import InterpolatedUnivariateSpline

q2s=[0.001,1,100,10000,16000000,64000000]

pdf=dict()
for q2 in q2s:
    reader=csv.reader(open('partonPDFData/protonQQ'+str(q2), 'rb'), delimiter=' ')
    header=reader.next()
    partons=header[2:]
    x=[]
    f=[[] for i in range(len(partons))]
    for row in reader:
        x.append(row[2])
        for i in range(len(partons)):
            f[i].append(row[2+2+2+i*2])
    pdf[q2]=dict([(partons[i], InterpolatedUnivariateSpline(x,f[i],k=1)) for i in range(len(partons))])
    
    pdf[q2]['top']=lambda x: 0

    for p,d in pdf[q2].items():
        if not 'bar' in p and not p+'bar' in pdf:
            pdf[q2][p+'bar']=pdf[q2][p]
