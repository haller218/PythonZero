"""
aula 37

"""

# python ide console online
# https://console.python.org/python-dot-org-console/

class Helpers:
  def inputIntData ( data = "" ):
    return int ( input ( data ) )


def exercicios (  ):

  def aula37 (  ) :

    import random

    __CONSTANTE_MATRIX = 4

    def generateMatrix (  ) :

      matriz = []

      lista = list(range(pow(__CONSTANTE_MATRIX,2)))

      for i in range(__CONSTANTE_MATRIX) : 

        linha = []

        for j in range(__CONSTANTE_MATRIX) :
          linha.append(random.choice(lista))
          lista.remove(linha[j])

        matriz.append(linha)

      return matriz

    def trocaRandom ( matrix ) :


      def trocaInMatriz ( p1, p2, matriz ) :

        aux = matriz[p1[0]][p1[1]]
        matriz[p1[0]][p1[1]] = matriz[p2[0]][p2[1]]
        matriz[p2[0]][p2[1]] = aux

      def escolheNumerosTupla (  ) :
        
        tuplado = []

        numeros = list(range(4))

        tuplado.append(random.choice(numeros))
        numeros.remove(tuplado[len(tuplado)-1])

        tuplado.append(random.choice(numeros))
        numeros.remove(tuplado[len(tuplado)-1])

        return tuple(tuplado)

      trocaInMatriz ( escolheNumerosTupla(), \
                    escolheNumerosTupla(), matrix )


    for i in range(64) :

      matrix = generateMatrix()

      # print (matrix)

      for i in range(9) :
        trocaRandom ( matrix )

      print (matrix)




  def aula35 (  ) :
    aula37 (  )

    print ( "aula 35" )

    def readLineText (  ):
      
      return int ( input ( "digite um numero (-1 to break)" ) )

    n = readLineText (  )

    tup = ()

    while n != -1:
      
      alt = readLineText (  )

      if n != -1:
      
        n = alt
      
      tup += n,

    def achaMaior (lista):

      maior = tup[0]

      for i in lista:

        if maior < i:

          maior = i

      return maior

    print("Maior numero: ", achaMaior ( tup ))


  def aula32 (  ) : 
    print ( "aula 32" )
    
    import random

    megasena = list(range(1,61))

    sorteado = [6,23,12,42,8,5]

    sorteado.sort()
    
    sorte = []

    mega_sort = megasena.copy()

    contador = 0

    while sorteado != sorte:

      for i in range(6):
        sorte.append(mega_sort[random.randint(0,59)])
        
      sorte.sort (  )
      print(sorte)
      # print ("{0:10} : {1:5}".format(str(sorteado),str(sorte)))

      contador += 1

    print ("Porcentagem {0:.5f} total de {1:10}".format(60/contador,contador))

  def aula31 (  ):

    print ("Aula 31")
    
    indicie = [1,2,3,6,5,4,9,8,5,6,47,23]

    valor = 0;
    while valor != -23:

      for i in range ( len(indicie) ):
        print ("%d : %d"%(i, indicie[i]))

      valor = int (input ("Digite o indice:"))

      while (valor < 0) or (valor > len(indicie)):
        valor = int (input ("Digite o indice:"))

      print (indicie[valor])

      indicie.remove(indicie[valor])





  def aula30 (  ):

    print ("Aula 30")

    # PESSOAS = 10

    # idade = []
    # altura = []

    # for idade in range ( PESSOAS ):
    #   for altura in range ( PESSOAS ):

    #     idade.append ( int ( input ( "Digite sua idade" ) ) )
    #     altura.append ( float ( input ( "Digite sua altura" ) ) )

    # for i in range

  def aula29 (  ):

    def votacao (  ):

      flag = -1

      # jogadores = []

      # while flag != 0:

      #   if flag <= 23 and flag > 0: 
      #     swap = int ( input ( "digite o numero do jogador" ) ) 
      #     jogadores.append ( swap )
      #   else:
      #     print ( "Digite um numero no intervado de 1 a 23" )

      # print ( "Total de Votos Computados: %d"%(len(jogadores)) )
      # for i in range ( 23 ):  
      #   print ( "Total de Votos do jogador %d: %d"%(i,jogadores.count( i )) )
      


    def lancaDados (  ):

      import random

      lancamento = []

      vezes = 10000000

      for i in range ( vezes ):
        lancamento.append(random.randint(1,7))

      print ( "lancamentos da face 1: %.2f%% "%((lancamento.count(1)/vezes)*100) )
      print ( "lancamentos da face 2: %.2f%% "%((lancamento.count(2)/vezes)*100))
      print ( "lancamentos da face 3: %.2f%% "%((lancamento.count(3)/vezes)*100))
      print ( "lancamentos da face 6: %.2f%% "%((lancamento.count(4)/vezes)*100))
      print ( "lancamentos da face 6: %.2f%% "%((lancamento.count(5)/vezes)*100))
      print ( "lancamentos da face 6: %.2f%% "%((lancamento.count(6)/vezes)*100))
      print ( "lancamentos da face 7: %.2f%% "%((lancamento.count(7)/vezes)*100))

    def main (  ):
      print ( "Aula 29" )
      # lancaDados (  )
      votacao (  )


    main (  )

  def aula28 (  ):

    def repeticao (  ):

      numeros = []

      flag = True

      while flag:

        numero = int ( input ( "Digite um Numero" ) )

        print ( numero )

        if numero != -1:

          inserir = True

          for i in range ( len ( numeros ) ):
        
            if numeros[i] == numero:
              inserir = False

          if inserir:
            numeros.append ( numero )

        else:
          flag = False

      print ( numeros )
        

    def main (  ):

      print ( "Aula 28" )
      repeticao (  )

    main (  )

  def aula27 (  ):


    def alocarMemoria (  ):
      a = 42
      b = a

      print ( a.bit_length (  ) )
      print ( b.bit_length (  ) )
      a = 1
      print ( a.bit_length (  ) )
      print ( b.bit_length (  ) )

      l1 = [4,3,2,1]
      l2 = l1

      print ( l1 )
      print ( l2 )

      l1 [ 0 ] = 800

      print ( l1 )
      print ( l2 )


    def main (  ):
      print ( "Aula 27" )
      alocarMemoria (  )
    
    main (  )


  def aula26 (  ):

    def listasDentroDeListas (  ):

      lista = [1,2,3,4,[1,2,3,4]]

      print ( lista )

      print ( lista [ 4 ] )

      print ( [[[[[1,2]]]]] )
      print ( [[[[[1,2],3,4,[[]]]]]] )

      print ( lista + [[[123]]] )

    def cincoNumeros (  ):

      numeros = []

      for i in range ( 5 ):

        numero = int ( input ( "Digite um numero %d"%(i + 1) ) )

        numeros.append ( numero )

      print ( numeros )

    def main (  ):

      print ( "Aula 26" )
      # listasDentroDeListas (  )
      cincoNumeros (  )

    main (  )

  def aula25 (  ):
    
    def listas (  ):

      lista = [ 0, 1, 2, 3, 4, 5, 6 ]

      print ( lista )

      for i in range ( len ( lista ) ):

        print ( lista [ i ] )

      print ( lista [ 5 ] + lista [ 3 ] )

      novaLista = [ 0,0,0,0 ]

      novaLista += lista

      print ( novaLista ) 
      print ( lista + novaLista )

      print ( novaLista [ 2 : 8 ] )
    
    def main (  ):
      print ( "Aula 25" )
      listas (  )


    main (  )


  def aula24 (  ):


    def randomize (  ):
      import random
      import time

      max = 60000

      def randRange (  ):
        print ( random.randrange ( i, max ), end = " ", flush = True )
      
      def randInt (  ):
        print ( random.randint ( i, max ), end = " ", flush = True )

      def randchoice (  ):
        print ( random.choice ( range ( max ) ), end = " ", flush = True )

      def randUniform (  ):
        print ( random.uniform ( 0, 1), end = " ", flush = True )

      for i in range ( max ):

        # randRange (  )
        # randInt (  )
        # randchoice (  )
        randUniform (  )

        # time.sleep ( 0.00001 )

    def quebraBanca (  ):
      import random

      print ( "jogo" )
      
      testes = int ( input ( "Digite o Numero de Testes" ) )

      troca = 0

      for i in range ( testes ):
        porta = random.randrange ( 1, 4 )
        premio = random.randint ( 1, 3 )

        if porta != premio:
          troca += 1

      print ( "É mais vantajoso trocar %.3g %% das vezes"%(troca*100/testes) )
      print ( "NÃO É mais vantajoso trocar %.3g %% das vezes"%((1 - troca/testes) * 100) )



    def main (  ):
      print ( "Aula 24" )
      # randomize (  )
      quebraBanca (  )

    main (  )



  def aula23 (  ):


    def usandoMath (  ):

      import math

      print ( math.sin ( 2 ) )
      print ( math.cos ( 3 ) )
      print ( math.tan ( 4 ) )
      print ( math.pow ( 2, 5 ) )
      print ( math.sqrt ( 6 ) )

    def uandoSin (  ):
  
      from math import sin

      print ( sin ( 2 ) )

    def simplificandoMath (  ):
  
      import math as m

      print ( m.pow ( 2, 54 ) )

    def simplificandoMetodo (  ):
  
      from math import sin as s

      print ( s ( 54 ) )

    def areaCirculo (  ):
  
      import math
  
      raio = float ( input ( "Digite o Raio do Circulo" ) )

      print ( "Area do Circulo: %.6f"%(math.pi * math.pow ( raio, 2 )) )

    def main (  ):
      print ( "Aula 23" )
      # usandoMath (  )
      # uandoSin (  )
      # simplificandoMath (  )
      # simplificandoMetodo (  )
      areaCirculo (  )

    main (  )


  def aula22 (  ):

    def funcaoPrint (  ):

      numeroReal = 100.0
      numero = 100

      print ( numeroReal )
      print ( numeroReal / 3 )
      print ( "%i"%(numeroReal) )
      print ( "%i"%numero )
      print ( "%f"%numeroReal )
      print ( "%10.7f"%(numeroReal/7) )
      print ( "%10.8f"%(numeroReal/7) )

    def temperaturas (  ):

      temperaturas = int ( input ( "Digite o numero de Temperaturas" ) )

      maior = 0
      menor = 0

      valor = float ( input ( "Digite a temperatura 1:" ) )

      maior = valor
      menor = valor

      soma = 0.0

      for temperatura in range ( 2, temperaturas+1 ):
        
        valor = float ( input ( "Digite a temperatura %d:"%temperatura) )

        if valor > maior:
          maior = valor
        elif valor < menor:
          menor = valor

        soma += valor

      print ( "Maior valor %.2f:"%maior )
      print ( "Menor valor %.2f:"%menor )
      print ( "Media das temperaturas %.2f:"%(soma/temperaturas) )

    def mediaAlunosTurma (  ):

      turmas = int ( input ( "digite o numero de turmas: " ) )

      media = 0

      for turma in range ( 1, turmas+1 ):

        alunos = int ( input ( "digite os alunos da turma %d: "%(turma) ) )

        while alunos > 40 or alunos < 0:
          
          print ( "Sala deve ter no maximo 40 alunos" )

          alunos = int ( input ( "digite os alunos da turma %d: "%(turma) ) )

        media += alunos

      print ( "media de alunos: %.10g"%(media/turmas) )

    def main (  ):
      print ( "exercicios: 22" )
      # funcaoPrint (  )
      # temperaturas (  )
      mediaAlunosTurma (  )

    main (  )


  def aula21 (  ):

    def realInteiro (  ):

      primeiroInteiro = int ( input ( "Digite um numero Inteiro" ) )
      segundoInteiro = int ( input ( "Digite um numero Inteiro" ) )
      terceiroReal = float ( input ( "Digite um numero Real" ) )

      prodSomaCubo = ( primeiroInteiro*2 ) * ( segundoInteiro / 2 )
      somaTriploSeg = ( primeiroInteiro*3 ) + ( terceiroReal )
      cubo = terceiroReal**3

      print ( prodSomaCubo )
      print ( somaTriploSeg )
      print ( cubo )

    def inteiroDecimal (  ):

      numero = float ( input ( "Informe um Numero" ) )

      if numero == int ( numero ):
        print ( "Numero", int ( numero ),"é Inteiro" )
      else: 
        # decimal = numero - int(numero)
        # if decimal >= 0.5:
        #   numero += 1
        numero = round ( numero )
        print ( "Numero",int ( numero ),"é Real" )
      # if type ( int ( numero ) ) is float
    
    def cosDeX (  ):
      
      serieN = int ( input ( "digite o numero da serie" ) )
      numero = int ( input ( "digite um numero" ) )

      resultado = 0

      def factorial ( fat ):
        result = 1;
        while fat >= 1:
          result = result * fat
          fat -= 1
        return result

      for n in range ( serieN ):
        
        resultado += ( ( ( -1 )**n )*( numero**(2*n) ) ) / ( factorial ( 2*n ) )

      print ( resultado )

  
    def main (  ):
      print ( "exercicios: 21" )
      # realInteiro (  )
      # inteiroDecimal (  )
      # cosDeX (  )

    main (  )


  def aula20 (  ):

    def SaldoSomatorio ( numero ):
      soma = 0
      for num in range ( 1, ( numero + 1), 1 ):
        soma = soma + ( num / ( numero - num + 1 ) )
        # soma += num / (numero - num + 1)
      print ( soma )


    def mediaAlunos ( ):

      media = 0.0

      for i in range ( 3 ):
        media += float ( input ( "Digite a nota 1" ) )
      
      media /= 3

      if media == 10:
        print ( "Aprovado com distinção" )
        print ( media )
      elif media < 7:
        print ( "Reprovado" )
        print ( media )
      elif media >= 7:
        print ( "Aprovado" )
        print ( media )

    def pesoIdeal (  ):

      sexo = input ( "Digite o seu sexo (M/F)" )

      altura = float ( input ( "Digite a sua Altura" ) )

      peso = 0

      if sexo == "M":
        peso = ( 72.7 * altura ) - 58 # homen
      elif sexo == "F":
        peso = ( 62.1 * altura ) - 44.7 # mulher

      print ( "Seu Peso ideal é: ", peso )
    



    def mainExec (  ):
      print ( "exercicios" )
      # mediaAlunos (  )
      pesoIdeal (  )
      # SaldoSomatorio ( 3 )

    mainExec (  )
        

  def aulas (  ):
    # aula20 (  )
    # aula21 (  )
    # aula22 (  )
    # aula23 (  )
    # aula24 (  )
    # aula25 (  )
    # aula26 (  )
    # aula27 (  )
    # aula28 (  )
    # aula29 (  )
    # aula30 (  )
    # aula31 (  )
    # aula32 (  )
    # aula35 (  )
    aula37 (  )



  aulas (  )



def loopsPython (  ):
  def loopWhile ( fat ):
    result = 1;
    while fat >= 1:
      result = result * fat
      fat -= 1
    print ( result )
  
  def loopFor (  ):

    def forLoop ( fact ):
      result = 1
      for i in range ( fact, 0, -1 ):
        result = result * i
      print ( result )

    def rangeIs (  ):
      print ( range ( 4 ) )
      print ( range ( 2, 4 ) )
      print ( range ( 5, 2, -1 ) )

    forLoop ( 60 )
    # rangeIs (  )
    

  loopWhile ( 30 )
  loopFor (  )


def testes (  ):

  def imputData (  ):
    inteiroNumero = int ( input ( "Test" ) )
    print ( inteiroNumero )

  def testInvoClass (  ):
    h = Helpers (  )
    numero = h.inputIntData ( "digite um numero" )
    print ( "VA TE CATAR ", numero )

  def voidFun (  ):
    print ( "GOTOHELLLLLL" )

  def mainTestes (  ):
    voidFun (  )
    # testInvoClass (  )
    # imputData (  )

  mainTestes (  )


def variaveisReais (  ):
  a = 3/4
  b = 3.14
  def mostrarValores ( a, b ):
    print ( a )
    print ( b )

  mostrarValores ( a, b )

  a = int ( "3" )
  b = float ( "32.2" )

  mostrarValores ( a, b )

def main (  ):
  print ( "Hello, World!" )
  # testes (  )
  # loopsPython (  )
  # variaveisReais (  )
  exercicios (  )


main (  )

