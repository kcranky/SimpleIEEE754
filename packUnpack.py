#Converter for arbitrary base floating points
from struct import *
from parameterDefinitions import Word32, Word16

def parse_bin_frac(s):
   return int(s[1:], 2) / 2.**(len(s) - 1)


def get_dec_value(binVal, struct):
   """Convert a n-bit floating binary value to decimal"""
   sign = binVal[0]
   exponent = binVal[1:struct["EXPONENT_MSB"]+2]
   mantissa = binVal[struct["EXPONENT_MSB"]+2:struct["WORD_MSB"]+1]
   #print(sign, exponent, mantissa)
   s = int(sign, 2)
   e = int(exponent, 2)
   m = parse_bin_frac("." + mantissa)
   #print(s, e, m)
   result = pow(-1, s) * (1+m) * pow(2, e-struct["EXPONENT_BIAS"])  
   print("{} converted to   {}").format(binVal, result)
   return result
   
   
def get_bin_value(decVal, struct):
   """Convert a decimal numner to n-bit floating point representation"""
   #print("\nNEW CONVERSION\n")
   integer, frac = decVal.split(".")
   frac=float(frac)/pow(10,len(frac))
   
   i = bin(int(integer))[2:]
   f = ""
   
   #get the fractional part
   for j in range(struct["MANTISSA_MSB"]):
      frac = float(frac*2)
      t = ("{0:f}").format(float(frac)).split(".")
      print(t, f)
      f = str(f) + t[0]
      #print(f, frac)
      frac = float(t[1])/pow(10,len(t[1]))
      if(int(float(t[1]))==0):
         break
   
   # Normalise
   mantissa = i+f
   c = 0
   while mantissa[0] != "1":
      mantissa=mantissa[1:]
      c = c-1
       
   # Bias the exponent
   if (c != 0):
         print("expc={}").format(c + struct["EXPONENT_BIAS"])
         exp = bin(c + struct["EXPONENT_BIAS"])
         exp = str(str(exp)[2:]).rjust(struct["EXPONENT_MSB"]+1,"0")
         print("expc={}").format(exp)

   else:
      exp = bin(len(i)-1+struct["EXPONENT_BIAS"])[2:]
     
   # Fill
   mantissa = str(str(mantissa)[1:]).ljust(struct["MANTISSA_MSB"]+1,"0")
   if (float(decVal) > 0):
      result = ("0"+exp+mantissa)[0:struct["WORD_MSB"]+1]
   else:
      result = ("1"+exp+mantissa)[0:struct["WORD_MSB"]+1]
      
   print("{} converted from {}").format(result, decVal)
   return result
   
  
if __name__ == "__main__":
   get_bin_value("-0.235", Word32)
   get_dec_value("10111110011100001010001111010111", Word32)   
   
   get_bin_value("-0.09375", Word16)
   get_dec_value("1010111000000000", Word16)   
   
   print("Finished")
   