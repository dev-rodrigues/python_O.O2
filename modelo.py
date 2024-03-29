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


class Play_list:

    
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho_playlist(self):
        return len(self.programas)

##testes
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
todo_mundo_em_panico = Filme('Todo Mundo em Panico', 2012, 120)
homem_aranha = Filme('Homem Aranha', 2013, 150)
atlanta = Serie('Atlanta', 2017, 2)
tbbt = Serie('The Big Bang Theory', 2011, 500)
oitnb = Serie('Orange is the new black', 2017, 4)

vingadores.dar_like()
atlanta.dar_like()
tbbt.dar_like()
tbbt.dar_like()
tbbt.dar_like()
tbbt.dar_like()
atlanta.dar_like()

filmes_e_serie = [vingadores, atlanta, todo_mundo_em_panico, tbbt, oitnb]

play_list_fim_de_semana = Play_list('fim de semana',filmes_e_serie)

for programa in play_list_fim_de_semana.programas:
    print(programa)