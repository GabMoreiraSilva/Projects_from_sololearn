players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

E_medio = sum(players)/len(players)

players_variance = [(i - E_medio)**2 for i in players]
players_variance = sum(players_variance)/len(players_variance)

Desvio = players_variance**(1/2)

num = [x for x in players if x >= (E_medio-Desvio) and x <= (E_medio+Desvio)]

print(len(num))

##Essa parte é apenas para Visualização dos resultados
print('Média: %.2f, Variancia: %.2f, Desvio: %.2f, Players: %s' % (E_medio,players_variance,Desvio,num))
