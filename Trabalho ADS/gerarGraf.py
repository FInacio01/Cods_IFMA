import pandas
from matplotlib import pyplot as plt


vet = {1 : "ARD_SOLO.CSV", 2 : "ARD_MULT.CSV", 3 : "ADS.CSV", 4 : "ADS_MULT.CSV"}
choise = 1
while True:
    print("Selecione o gráfico")
    print("ArdMega Solo------1")
    print("ArdMega Mult------2")
    print("ESP32 Solo--------3")
    print("ESP32 Mult--------4")
    print("EXIT--------------0")

    choise = int(input("Opção: "))
    if choise == 0: break
    forced = pandas.read_csv(vet[choise], header=None)
    print(forced)


    fig, grafh = plt.subplots()
    grafh.plot(forced[0], forced[1])
    grafh.set_xlabel("Tempo")
    grafh.set_ylabel("Tensão")
    grafh.set_title(vet[choise].replace(".CSV", ""))

    plt.show()

