algoritmo "fila_FIFO"

var
   fila: vetor[1..10] de inteiro
   inici, fim, i, opcao, valor: inteiro

inicio
   inici <- 1
   fim <- 0

   repita
      escreval("")
      escreval("1 - Enfileirar")
      escreval("2 - Desenfileirar")
      escreval("3 - Mostrar fila")
      escreval("0 - Sair")
      escreva("Opcao: ")
      leia(opcao)

      escolha opcao

         caso 1
            se fim < 10 entao
               escreva("Digite um valor: ")
               leia(valor)
               fim <- fim + 1
               fila[fim] <- valor
            senao
               escreval("Fila cheia!")
            fimse

         caso 2
            se inici <= fim entao
               escreval("Removido: ", fila[inici])
               inici <- inici + 1
            senao
               escreval("Fila vazia!")
            fimse

         caso 3
            se inici <= fim entao
               escreval("Fila:")
               para i de inici ate fim faca
                  escreval(fila[i], " ")
               fimpara
               escreval("")
            senao
               escreval("Fila vazia!")
            fimse

      fimescolha

   ate opcao = 0

fimalgoritmo

