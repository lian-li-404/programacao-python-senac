## Uma empresa de análise de dados forneceu uma API para receber as informações dos escritórios de call center.
## No entanto, foi orientado que esses dados não devem ser enviados individualmente (linha por linha), pois isso sobrecarrega o banco de dados da empresa.
## A recomendação é que o envio seja feito em lote.

# Exemplo em código:

#Função responsável por enviar os dados para a API da empresa de análise de dados
def envio_dados_api(data_ligacao, cpf_cliente, ocorrencia_ligacao):
    executar_conexao_api(data_ligacao, cpf_cliente, ocorrencia_ligacao)

#Conexão com o banco de dados local para coletar as informações no formato exigido pela API
dados = cursor.execute("select data_ligacao, cpf_cliente, ocorrencia_ligacao", con=conexao_string)
dataframe_formatado = pd.DataFrame(dados)

#Forma incorreta de envio, pois envia uma requisição por linha utilizando um loop "for":
for _, l in dataframe_formatado.iterrows():
    linha_data_ligacao = l['data_ligacao']
    linha_cpf_cliente = l['cpf_cliente']
    linha_ocorrencia_ligacao = l['ocorrencia_ligacao']
    envio_dados_api(linha_data_ligacao, linha_cpf_cliente, linha_ocorrencia_ligacao)

#Como esse envio linha a linha não é permitido, a pergunta é: como realizar o envio em lote, conforme solicitado pela empresa de análise de dados?