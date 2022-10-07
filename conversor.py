def Cm_p_Pol (v):
  Cm_p_Pol = v*0.39
  print(Cm_p_Pol)
  file = open('arquivo.txt', 'w+')
  file.write(f"o valor {v} em centímetros corresponde a {Cm_p_Pol} valor em polegadas.")
  file.seek(0,0)
  file.read()
  file.seek(0,0)
  file.close()
 