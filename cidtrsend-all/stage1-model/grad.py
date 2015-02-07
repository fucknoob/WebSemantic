import sys
import mdFuzzy


a='hary'
b='Harry'
c="BoEm"


def compare_arr(a1,arr):
 if type(a1) != type(''): return False
 if type(arr) != type([]): return False;
 for c in arr:
   if type(c) == type(0): c=str(c)
   if type(c) == type(0.0): c=str(c)
   if mdFuzzy.compare_n(a1,c) > 0:
    return True
 return False   

 
print 'compare:',a,b 
rt=mdFuzzy.compare(a,b)
print 'rt:',rt,'\n'

print 'compare:',a,

print 'compare:',a,[0,c]
#=============
rt2=compare_arr(a,[0,c])
print 'rt2:',rt2,'\n'


