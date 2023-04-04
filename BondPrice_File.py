

def getBondPrice(y, face, couponRate, m, ppy=1):
    cf = face * couponRate
    pvcfsum = 0
    for i in range(1,m+1):
        py=(1+y)**(-i)
        pvcf=pv*cf
	pvcfsum+=pvcf 
    
    pvcfsum+=face*pv
    return(pvcfsum)