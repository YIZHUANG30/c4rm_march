

def getBondPrice_E(face, couponRate, yc):
  bondPrice=0
  m=len(yc)
  for i,y in enumerate(yc):
    bondPrice+=face*couponRate*(1+y)**(-i-1)
  bondPrice+=face*(1+yc[m-1])**(-m)
  return(bondPrice)


