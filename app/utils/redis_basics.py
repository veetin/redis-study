# import redis

# redis_connection = redis.Redis(
#     host="localhost",
#     port=6379,
#     db=0,
# )

# # - Registros unicos
# ## - adicionar um dicicionario com uma unica chave e valor - {"chave_1": "valor_1"}
# redis_connection.set("chave_1", "valor_2")

# ## - buscar um valor de uma chave
# valor = redis_connection.get("chave_1") # retorna uma string binaria - retorno: b'valor_1'
# valor = valor.decode("utf-8") # decodifica a string binaria para uma string utf-8 - retorno valor_1
# print(valor)

# ## - deletar um valor de uma chave
# redis_connection.delete("chave_1")
# print(redis_connection.get("chave_1")) # retorna None
# print("chave_1 deletada")

# ## - deletar todos os registros do redis
# redis_connection.flushall()
# print(redis_connection.get("chave_1")) # retorna None
# print("todas as chaves deletadas")


# # - Registro multiplos (hash)

# ## - adicionar um dicionario com multiplas chaves e valores - "hash_1": {"chave_1": "valor_1", "chave_2": "valor_2"}
# redis_connection.hset("hash_1", "nome", "joao")
# redis_connection.hset("hash_1", "idade", 21)
# redis_connection.hset("hash_1", "email", "joao@example.com")

# ## - buscar um item de um hash

# nome = redis_connection.hget("hash_1", "nome").decode("utf-8")
# idade = redis_connection.hget("hash_1", "idade").decode("utf-8")
# email = redis_connection.hget("hash_1", "email").decode("utf-8")
# print(nome, idade, email)

# ## - buscar todos os items de um hash

# todos_items = redis_connection.hgetall("hash_1")
# print(todos_items)

# ## deletar um hash
# redis_connection.delete("hash_1")
# print(redis_connection.hget("hash_1", "nome")) # retorna None
# print("hash_1 deletado")


## - Verificando se uma chave existe

# chave_existe = redis_connection.exists("chave_1") # retorna 1 se a chave existe, 0 se não existe
# hash_existe = redis_connection.exists("hash_1") # retorna 1 se o hash existe, 0 se não existe
# hash_1_nome_existe = redis_connection.hexists("hash_1", "nome") # retorna 1 se o item existe, 0 se não existe
# print(hash_1_nome_existe)
# print(chave_existe) 
# print(hash_existe) 

# criando hash de hash usando chaves compostas
# "hashes": {"hash_1:nome": "joao", "hash_1:idade": "21", 
#            "hash_2:nome": "maria", "hash_2:idade": "22"}
# redis_connection.hset("hashes", "hash_1:nome", "joao")
# redis_connection.hset("hashes", "hash_1:idade", "21")
# redis_connection.hset("hashes", "hash_1:email", "joao@example.com")
# redis_connection.hset("hashes", "hash_2:nome", "maria")
# redis_connection.hset("hashes", "hash_2:idade", "22")
# redis_connection.hset("hashes", "hash_2:email", "maria@example.com")

# # buscar um item de um hash de hash
# nome = redis_connection.hget("hashes", "hash_1:nome")
# if nome:
#     print(nome.decode("utf-8"))


from app.infra.depends import get_redis_repo
redis_repo = get_redis_repo()

redis_repo.set("ola", "mundo")
print(redis_repo.get("olas"))

redis_repo.hset("hash_1", "nome", "joao")
redis_repo.hset("hash_1", "idade", 21)
redis_repo.hset("hash_1", "email", "joao@example.com")

print(redis_repo.hget("hash_1", "nome"))
print(redis_repo.hget("hash_1", "idade"))
print(redis_repo.hget("hash_1", "email"))