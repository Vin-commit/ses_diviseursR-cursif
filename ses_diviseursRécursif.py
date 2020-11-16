#!/usr/bin/python3
# coding : utf-8


def ses_diviseurs(divDeN, nDivisé, lstDiv):
  if (divDeN == 1):
    return lstDiv
  if (nDivisé % divDeN == 0):
    if (len(lstDiv) != 0):
      lstDiv += ","
    lstDiv += " "+str(divDeN)
  return ses_diviseurs(divDeN-1, nDivisé, lstDiv)


n = int(input("Entrez un nombre dont on cherche les diviseurs : "))
if (len(ses_diviseurs(n-1, n, "")) == 0):
  print ("Ce nombre n'a pas de diviseurs entiers différents de 1 et de lui-même.")
else:
  if (ses_diviseurs(n-1, n, "").count(',') == 0):
    print ("Son diviseur est :"+ses_diviseurs(n-1, n, ""))
  else:
    print ("Ses diviseurs sont :"+ses_diviseurs(n-1, n, ""))


----------------------------------------------------------------------- Résultat ------------------------------------------------------------------------------