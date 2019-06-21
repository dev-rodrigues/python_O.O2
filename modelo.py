
class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada

vingadores = Filme('vingadores', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.nome} '
      f' - Duração: {vingadores.duracao}')

atlanta = Serie('atlanta', 2017, 2)
print(f'Nome: {atlanta.nome} - Ano: {atlanta.nome} '
      f' - Duração: {atlanta.temporada}')