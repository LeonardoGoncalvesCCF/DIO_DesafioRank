"""" 
Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze 
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal
"""
print("-------------------------------------------------")
vitorias = int(input("Qauantas vitorias você teve? "))
derrotas = int(input("Qauantas derrotas você teve? "))
print("-------------------------------------------------")

def mmr(vitorias, derrotas):
        pontos = vitorias - derrotas
        return pontos

result_mmr = mmr(vitorias, derrotas)

if result_mmr <= 10:
        print(" Seu Rank é Ferro ")

elif result_mmr >= 11 and result_mmr <= 20:
        print(" Seu Rank é Bronze ")

elif result_mmr >= 21 and result_mmr <= 50:
        print(" Seu Rank é Prata ")

elif result_mmr >= 51 and result_mmr <= 80:
        print(" Seu Rank é Ouro ")

elif result_mmr >= 81 and result_mmr <= 90:
        print(" Seu Rank é Diamante ")

elif result_mmr >= 91 and result_mmr <= 100:
        print(" Seu Rank é Diamante ")

elif result_mmr >= 101:
        print(" Seu Rank é Imortal ")
            
print("-------------------------------------------------")