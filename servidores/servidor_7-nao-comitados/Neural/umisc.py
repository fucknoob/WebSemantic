

def trim(vl):
  str=""
  lett_init=False
  for i in vl:
   if i != ' ' or lett_init:
    str+=i
    lett_init=True
  i=len(str)
  #
  lett_init=False
  str2=""
  i=len(str)-1
  while i >=0 :
   if str[i] != ' ' or lett_init:
    str2=str[i]+str2
    lett_init=True
   i-=1
  return str2