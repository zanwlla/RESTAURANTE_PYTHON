import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():

    '''Essa função é responsável por exibir o nome do programa 

    Inputs:
    - Nome do programa
    '''
    print(
        '''
    Restaurante Expresso Camila
    '''
    )


def exibir_opcoes():
    '''Essa função é responsável por exibir as opções do restaurante 

    Inputs:
    - Cadastrar 
    - Listar restaurantes 
    - Alternar estado do restaurante
    Outputs:
    - Sair 
    '''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n') 
    
    
def finalizar_app():
     '''Essa função é responsável por finalizar o app 

    Outputs:
    - Sair 
    '''
     exibir_subtitulo('Finalizando app')

    

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    '''Essa função é responsável por exibir a opção inválida 

    Inputs:
    - Opção inválida 
    '''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo 

    Inputs:
    - Texto 
    '''
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    

def cadastrar_novo_restaurante():
    
    '''Essa função é responsável por cadastrar 
       um novo restaurante

    Inputs:
    - Nome do restaurante
    - Categoria
    Outputs:
    - Adiciona um novo restaurante à lista de restaurantes  
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes 

    Inputs:
    - Nome do restaurante 
    - Categoria do restaurante

    Outputs:
    - Restaurante ativado/desativado 
    '''
    exibir_subtitulo('Listando restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar o estado do restaurante 

    Inputs:
    - Nome do restaurante
    - Desativado
    Outputs:
    - Ativado 
    '''
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem) 
           
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu_principal()

def escolher_opcao():

    '''Essa função é responsável por escolher as opções do restaurante 

     Inputs:
    - Escolha uma opção 
    - Cadastrar 
    - Listar restaurantes 
    - Alternar estado do restaurante
    Outputs:
    - Finalizar app 
    - Opção inválida 
    '''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''
    Essa função é responsavel por ervir como ponto de patida para a execução do programa

    outputs:
    -exibi nome do app
    -exibir opções disponíveis
    -pede ao usuario que escolha uma opção
    '''
    #10 clear
    os.system('clear')
    #6 chamar o nome do app
    exibir_nome_do_programa()
    #7 chamar a escolha de opções
    exibir_opcoes()
    #9 chamar a opção digitada
    escolher_opcao()


if __name__ == '__main__':
    main()
