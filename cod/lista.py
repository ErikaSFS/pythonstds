movies =[ 'her', 2014, 'Black Partner', 2017, 'Queen', 2018, 'Nasce uma estrela', 2017, ['Capita Marvel', 2019]]


"""não esta funcionando"""
"""este é o modulo "lista.py" e fornece uma função chamada print_lol()
que imprime listas que podem ou não incluir listas aninhadas"""

def print_lol(the_list):
   """uma função que requer um argumento posicional chamado "the_list", q eh qlqr lista Python. Cda item
      de dados na lista fornecida é recursivamente impresso na tela em sua propria linha"""

for each_item in the_list:
    if isinstance(each_item, list):
         print_lol(each_item)        
    else:
        print(each_item)    

print_lol(movies)        