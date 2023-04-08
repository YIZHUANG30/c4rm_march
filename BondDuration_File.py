
def getBondDuration(y, face, couponRate, m, ppy = 1):
  t=int(m*ppy)
  pvcf_t = 0
  bondPrice=0
  for i in range(1,t+1):
    pvcf_t += face*couponRate/ppy*i*(1+y/ppy)**(-i)
    bondPrice += face*couponRate/ppy*(1+y/ppy)**(-i)
  bondPrice+=face*(1+y/ppy)**(-m*ppy)
  pvcf_t+=face*t*(1+y/ppy)**(-m*ppy)
  bondDuration=pvcf_t/bondPrice
  return(bondDuration)

