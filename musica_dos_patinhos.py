#try e except para o caso do input do usuário não ser válido
try:
  #input do usuário e armazenamento desse numero em outra variável para contagem regressiva
  total_patinhos = int(input("Digite o número de patos para música: "))
  patos = total_patinhos

  print("♪")
  #repetir refrão reduzindo um patinho a cada iteração até chegar em 0
  while patos > 0:
    #primeira frase no singular ou plural
    if patos == 1:
      print(f"{patos} patinho foi passear")
    else:
      print(f"{patos} patinhos foram passear")
    
    #frases que são sempre iguais
    print("além das montanhas para brincar,")
    print("a mamãe gritou QUÁ QUÁ QUÁ QUÁ")

    patos -= 1
    #frase final adaptada para um ou nenhum patinho após redução do contador
    if patos == 0:
      print(f"mas nenhum patinho voltou de lá")
    elif patos == 1:
      print(f"mas só {patos} patinho voltou de lá")
    else:
      print(f"mas só {patos} patinhos voltaram de lá")
    
    #linha em branco entre refrões p/ melhorar a visualização
    print()

  #estrofe final a ser mostrada apenas uma vez (por isso está fora do loop)
  print("A mamãe patinho foi procurar")
  print("além das montanhas, na beira do mar,")
  print("a mamãe gritou QUÁ QUÁ QUÁ QUÁ")
  print(f"e os {total_patinhos} patinhos voltaram de lá")
  print("♪")

#se o input do usuário não for um número inteiro mostra essa mensagem
except:
  print("Tente novamente digitando um número inteiro.")