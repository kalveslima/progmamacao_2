# quadro inputs funcao que recebe inputs do usuário e retorna investe ou n investe
##valor minimo valor investimento mes retido 

#mes retido == quantidade de meses do investimento
#valor investimento == valor do investimento
#v_lucro = o valor que voce pretender ter apos o investimento
# pelo oque eu entendi, serao 6 entradas, a3 clientes 3 locadora
# sao 3 funcoes, primeriro a funcao investe, que recebe os inputs do usuario 
# segundo funcao corretora que recebe os valores da proposta da corretora, depois a investe or no,
#que calcula se o investimento é valido ou não, e retorna a resposta para o usuario.
#isso segue os principos solid, pois cada funcao tem uma responsabilidade unica, e nao se mistura com outras funcoes.


def investe():
    v_investimento=float(input("Digite o valor do investimento: "))
    mes_retido=int(input("Digite o mês de retorno do investimento: "))
    v_lucro=float(input("Digite o valor do lucro esperado: "))
    return v_investimento, mes_retido, v_lucro


def imobiliria():
    v_investimento_minimo=float(input("Digite o valor do investimento mínimo: "))
    mes_retido_minimo=int(input("Digite o mês de retorno do investimento: "))
    porcentagem=float(input("Digite o valor do lucro esperado: "))
    return v_investimento_minimo, mes_retido_minimo, porcentagem


def calculate(mes_retido, mes_retido_minimo, v_investimento, v_lucro, porcentagem):
    #minha duvida e, esse negocio do copilot irritante, o rendimento mensal total em doze meses e pocentagem, ou seja se for 30,5
    #  sera 12 mese tera essa porcentagem encima do valor de lucro, ou seja ele recebe porcentagem, qnt de meses e for 12 meses sera apenas 30,5 do valor de lucro, seguindo uma
    #  logica mei estranha em 24 meses seria 61% do valor, oque e loucura,mas e essa conta que vou fazer, por que nao me deram o valor exato de nada  como os inputs sao de apenas 12 meses ent qualquer investimento com mais ou menos disso eu nao vou faer.
    #vim me corrigir tem bem mais tem de 6 12 e 24 ent vou descobrir o rendimento mensavel dividindo a porcentasgem pelo mes retido, 
    if mes_retido >= mes_retido_minimo:
        rendimento_mensal = porcentagem / mes_retido
        lucro_total = v_investimento * (rendimento_mensal / 100) * mes_retido
        if lucro_total >= v_lucro:
            return "Investimento válido"
        else:
            return "Investimento inválido"
        

def main():
    v_investimento, mes_retido, v_lucro = investe()
    v_investimento_minimo, mes_retido_minimo, porcentagem = imobiliria()
    resultado = calculate(mes_retido, mes_retido_minimo, v_investimento, v_lucro, porcentagem)
    print(resultado)



main()

