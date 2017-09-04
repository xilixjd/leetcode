# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

import math
def IsPrimeNumber(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# print IsPrimeNumber(113)
# {
#     if (n==2)
#     {
#         return true;
#     }
#  
#     if (n%2==0)
#     {
#         return false;
#     }
#  
#     int sqrtn=(int)sqrt((double)n);
#     bool flag=true;
#  
#     for (int i=3;i<=sqrtn;i+=2)
#     {
#         if (n%i==0)
#         {
#             flag=false;
#         }
#     }
#     return flag;
# }

def GetAn(a1, a2, a3, n):
    for i in range(n - 3):
        an = a1 + a2 + a3
        # print an
        a1 = a2
        a2 = a3
        a3 = an
    return an % 10000

print GetAn(1234, 5678, 9012, 100)

# for (i=2;i<=n;i++) {
#          while (n != i) {
#              if (0 == n%i) {
#                  printf("%d*",i);
#                  n=n/i;
#              }
#              else
#                  break;
#          }
#      }
#      printf ("%d\n",n);

# def MaxFactor(n):
#     array = []
#     for i in range(2, n+1):
#         while n != i:
#             if 0 == n % i:
#                 array.append(i)
#                 n /= i
#             else:
#                 break
#     array.append(n)
#     return max(array)
#
# print MaxFactor(123456)