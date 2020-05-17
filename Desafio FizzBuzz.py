# progrmador: wesley davi zanon novaes
# Linguagem de programção: Python
#iniciando com classe para organizar o codigo
#herdar as varia numeros e FizzBuzz para as funçoes
class FizzBuzz:
    def __init__(self, numeros, fizz, buzz, fizzbuzz):
        self.numeros = numeros
        self.fizz = fizz
        self.buzz = buzz
        self.fizzbuzz = fizzbuzz
        
    #funcao responsavel de calcular os numeros e realocar FizzBuzz
    def realocaNumeros(self):
        
        #variavel ira receber todos os numeros do vetor
        for x in self.numeros:

            #condiçoes se vai retornar os numeros ou FizzBuzz
            #variaveis para somar fizzbazz
            if x%3 == 0 and x%5 != 0:
                novonumeros.append("Fizz")
                self.fizz = self.fizz +1
                
            elif x%5  == 0 and x%3 != 0:
                novonumeros.append("Buzz")
                self.buzz = self.buzz + 1
                
            elif x%3 == 0 and x%5 == 0:
                novonumeros.append("FizzBuzz")
                self.fizzbuzz = self.fizzbuzz + 1
                
            else:
                novonumeros.append(x)
                
                
    def mostraNumeros(self):
        for l in novonumeros:
            print(l)
            
        print("\n quantidade de fizzbuzz:\n")
        print(self.fizz, "fizz")
        print(self.buzz, "buzz")
        print(self.fizzbuzz, "fizzbuzz")
                

#________________________________________

#variaveis para auxiliar a quantia de fizzbuzz
fizz = 0 
buzz = 0
fizzbuzz = 0

quantia = int(input("Digite a quantidade de numeros que deseja receber: "))

print("Digite um sequencial de numeros de 1 a 1000")

#vetor vazio para colocar os numeros
numeros = []

#vetor vazio que ira receber os Fizz e Buzz
novonumeros = []

#loop para digitar a quantidade num de numeros
for l in range(quantia):
    
    #variavel para receber os numeros
    nume = int(input())
    #colocando os numeros dentro do vetor
    numeros.append(nume)
    
#definir r chamar a classe e funçoes da classe object
fb = FizzBuzz(numeros, fizz, buzz, fizzbuzz)
fb.realocaNumeros()

#Uso '\n' no meio dos programas para pular uma linha na hora de compilar
#ajuda no entendimento
print("\n")

#funcao para mostrar os numeros linhadamente    
fb.mostraNumeros()
