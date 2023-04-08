


def getBondPrice(y, face, couponRate, m, ppy=1):
  t=int(m*ppy)
  bondPrice=0
  for i in range(1,t+1):
    bondPrice+=face*couponRate/ppy*(1+y/ppy)**(-i)
  bondPrice+=face*(1+y/ppy)**(-m*ppy)
  return(bondPrice)


