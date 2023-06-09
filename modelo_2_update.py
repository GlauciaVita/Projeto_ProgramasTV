class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome}  Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
friends = Serie('friends', 1994, 10)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

friends.dar_like()
friends.dar_like()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {friends.nome} - Likes: {friends.likes}')

filmes_e_series = [vingadores, friends]

for programa in filmes_e_series:
    print(programa)