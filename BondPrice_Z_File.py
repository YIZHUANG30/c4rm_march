

def getBondPrice_Z(face, couponRate, times, yc):
  bondPrice=0
  for i,y in zip(times,yc):
    bondPrice+=face*couponRate*(1+y)**(-i)
  n=len(times)
  bondPrice+=face*(1+yc[n-1])**(-times[n-1])
  return(bondPrice)


