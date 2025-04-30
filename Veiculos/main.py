from models.veiculos import veiculos

gol = veiculos("Gol Copa", "Volkswagen", "IND-1010", 
               2006, "Amarelo", 0, -29.668241, -51.111896)


gol.mostrarInfos()
gol.acelerar()
gol.mostrarInfos()
gol.frear()
gol.mostrarInfos()