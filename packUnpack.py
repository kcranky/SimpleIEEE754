#Converter for arbitrary base floating points
from struct import *
# Parameters
Word32 = {
   "WORD_MSB": 31,
   "EXPONENT_MSB" : 7,
   "MANTISSA_MSB" : 22,
   "EXPONENT_BIAS" : (pow(2,8)/2-1)
}

Word16 = {
   "WORD_MSB": 15,
   "EXPONENT_MSB" : 4,
   "MANTISSA_MSB" : 9,
   "EXPONENT_BIAS" : (pow(2,5)/2-1)
}


def parse_bin_frac(s):
   return int(s[1:], 2) / 2.**(len(s) - 1)


def getValue(binVal, struct):
   print("Converting")
   sign = binVal[0]
   exponent = binVal[1:struct["EXPONENT_MSB"]+2]
   mantissa = binVal[struct["EXPONENT_MSB"]+2:struct["WORD_MSB"]+1]
   print(sign, exponent, mantissa)
   s = int(sign, 2)
   e = int(exponent, 2)
   m = parse_bin_frac("." + mantissa)
   value = pow(-1, s) * (1+m) * pow(2, e-struct["EXPONENT_BIAS"])  
   print(value)
   
if __name__ == "__main__":
   binaryIN = "01000001110011111110001101010111"
   getValue(binaryIN, Word32)
   binaryIN= "0100111001111111"
   getValue(binaryIN, Word16)
   
