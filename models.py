from peewee import *
# Importar bibliotecas de data e hora para preencher automaticamente
from datetime import datetime, date 

meu_bd = SqliteDatabase("meus_dados.db")

class MinhaBase(Model):
    class Meta:
        database = meu_bd

class Usuario(MinhaBase):
    nome = CharField()
    email = CharField(unique=True)
    senha = CharField()
    
    def __str__(self):
        return f"[{self.id}] {self.nome} ({self.email})"

class Tema(MinhaBase):
    nome = CharField()
    def __str__(self):
        return f"[{self.id}] {self.nome}"

class Arte(MinhaBase):
    artista = ForeignKeyField(Usuario)
    tipo = ForeignKeyField(Tema)
    descricao = CharField()
    def __str__(self):
        return f"[{self.id}] {self.artista} --- {self.tipo} --- {self.descricao}"


# Depois de criar todas as suas classes
# Vamos criar o banco de dados e as tabelas
meu_bd.connect()
# meu_bd.create_tables([Estudante, TipoProtocolo, Protocolo])
meu_bd.create_tables([Usuario, Tema, Arte])
