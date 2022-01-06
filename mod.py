import math
def mala(a,b,c,d):
  mal=math.sqrt((c-a)**2)*((d-b)**2)
  return mal
def malad(a,b,c,d):
  mald=math.sqrt((c-a)**2)*((d-b)**2)
  return mald
def malat(a,b,c,d):
  malt=math.sqrt((c-a)**2)*((d-b)**2)
  return malt
def per(mala,malad,malat):
  perimetrs=(mala,malad,malat)/2
  return perimetrs
def form(per,mala,malad,malat):
  laukums=math.sqrt((per*(per-mala)*(per-malad)*(per-malat)))
  return laukums