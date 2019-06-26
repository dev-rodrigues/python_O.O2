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

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} -  Likes: {self._likes}'

## filme ## - filha
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.duracao} min -  Likes: {self._likes}'

## serie ## filha
class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.temporada} temporadas -  Likes: {self._likes}'

##teste
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

##teste
atlanta = Serie('atlanta', 2017, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_serie = [vingadores, atlanta]

for programa in filmes_e_serie:
    print(programa)