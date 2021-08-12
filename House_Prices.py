import numpy as np

Data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

Data_Mean = np.mean(data)
Data_Standard_Deviation = np.std(data)

Houses = [x for x in data if x >= (data_mean-data_standard_deviation) and x <= (data_mean+data_standard_deviation)]
Porcentagem = (len(Houses)/data.size)*100

print(Porcentagem)
