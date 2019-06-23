class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

## filme ## - filha
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

## serie ## filha
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

##teste
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f' - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

##teste
atlanta = Serie('atlanta', 2017, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta._nome} '
      f' - Duração: {atlanta.temporada} - Likes: {atlanta.likes}')

filmes_e_serie = [vingadores, atlanta]

for programa in filmes_e_serie:
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporada
    print(f'{programa.nome} - {detalhes}')