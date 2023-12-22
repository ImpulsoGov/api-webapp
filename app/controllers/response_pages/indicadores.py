content = """"
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Impulso - Indicadores Resumo</title>
    <style>
        table, th, td {
          border:1px solid black;
          border-collapse: collapse;
          text-align: center;
          padding: 10px;
        }
    </style>
</head>
<body>
    <div>
        <h1>API Impulso - Indicadores Resumo</h1>
        <h2>Orientações para o endpoint /impulsoprevine/indicadores/</h2>
    </div>
    <div>
        <h3>Retorno</h3>
        <p>Dados resumidos de Indicadores de desempenho para o Parametro selecionado</p>
        <hr>
        <h3>Parametros</h3>
        <p>id_sus : Codigo de identificação do SUS para o município</p>
        <p>municipio_nome : Nome do município normalizado (Sem acentos, espaço substituidos por traço, todas as letras minúsculas) </p>
        <p>estado_nome : Nome do estado(Unidade Federativa) normalizado (Sem acentos, espaço substituidos por traço, todas as letras minúsculas) </p>
        <p>estado_sigla : Sigla do estado(Unidade Federativa) </p>
        <p>indicadores_parametros_id : Codigo de Identificação do Indicador</p>
        <p>indicadores_nome : Nome do Indicador Normalizado</p>
        <table>
            <tr>
                <th>indicadores_parametros_id</th>
                <th>indicadores_parametros_nome</th>
                <th>indicadores_parametros_nome_normalizado</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Pré-Natal (6 consultas)</td>
                <td>pre-natal-6-consultas</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Pré-Natal (Sífilis e HIV)</td>
                <td>pre-natal-sifilis-hiv</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Gestantes Saúde Bucal</td>
                <td>gestantes-saude-bucal</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Cobertura Citopatológico</td>
                <td>citopatologico</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Cobertura Polio e Penta</td>
                <td>polio</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Hipertensão (PA Aferida)</td>
                <td>hipertensao</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Diabetes (Hemoglobina Glicada)</td>
                <td>diabetes</td>
              </tr>
  
        </table>
    </div>
    <div>
        <hr>
        <h3>Exemplos</h3>
        <p><b>Requisição </b>/impulsoprevine/indicadores/?id_sus=520005 ou /impulsoprevine/indicadores/?municipio_nome=abadia-de-goias</p>
        <p><b>Observação:</b> <i>Retorna dados de todos indicadores para o municipio selecionado</i></p>
        <p><b>Observação:</b> <i>Se houverem duas cidades com o mesmo nome o endpoint retornará os dados de ambas, para retorno unico especifique o parametro estado_sigla em conjunto; exemplo /suporte/municipios/?municipio_nome=abadia-de-goias&estado_sigla=go</i></p>
        <p><b>Retorno </b>
            [
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 1,
                    "indicadores_parametros_nome_normalizado": "pre-natal-6-consultas",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 16.0,
                    "estado_nome_normalizado": "goias",
                    "id": 1071,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Pré-Natal (6 consultas)",
                    "indicadores_parametros_ordem": 1,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 19
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 2,
                    "indicadores_parametros_nome_normalizado": "pre-natal-sifilis-hiv",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 21.0,
                    "estado_nome_normalizado": "goias",
                    "id": 5339,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Pré-Natal (Sífilis e HIV)",
                    "indicadores_parametros_ordem": 2,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 17
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 3,
                    "indicadores_parametros_nome_normalizado": "gestantes-saude-bucal",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 14.0,
                    "estado_nome_normalizado": "goias",
                    "id": 10778,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Gestantes Saúde Bucal",
                    "indicadores_parametros_ordem": 3,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 20
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 4,
                    "indicadores_parametros_nome_normalizado": "citopatologico",
                    "indicadores_parametros_meta": 40.0,
                    "indicadores_resultados_porcentagem": 6.0,
                    "estado_nome_normalizado": "goias",
                    "id": 16212,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Cobertura Citopatológico",
                    "indicadores_parametros_ordem": 4,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 1015
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 5,
                    "indicadores_parametros_nome_normalizado": "polio",
                    "indicadores_parametros_meta": 95.0,
                    "indicadores_resultados_porcentagem": 34.0,
                    "estado_nome_normalizado": "goias",
                    "id": 21717,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Cobertura Polio e Penta",
                    "indicadores_parametros_ordem": 5,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 87
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 6,
                    "indicadores_parametros_nome_normalizado": "hipertensao",
                    "indicadores_parametros_meta": 50.0,
                    "indicadores_resultados_porcentagem": 3.0,
                    "estado_nome_normalizado": "goias",
                    "id": 21869,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Hipertensão (PA Aferida)",
                    "indicadores_parametros_ordem": 6,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 930
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 7,
                    "indicadores_parametros_nome_normalizado": "diabetes",
                    "indicadores_parametros_meta": 50.0,
                    "indicadores_resultados_porcentagem": 1.0,
                    "estado_nome_normalizado": "goias",
                    "id": 30536,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Diabetes (Hemoglobina Glicada)",
                    "indicadores_parametros_ordem": 7,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 281
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 2,
                    "indicadores_parametros_nome_normalizado": "pre-natal-sifilis-hiv",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 36.0,
                    "estado_nome_normalizado": "goias",
                    "id": 39574,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Pré-Natal (Sífilis e HIV)",
                    "indicadores_parametros_ordem": 2,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 11
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 1,
                    "indicadores_parametros_nome_normalizado": "pre-natal-6-consultas",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 22.0,
                    "estado_nome_normalizado": "goias",
                    "id": 40825,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Pré-Natal (6 consultas)",
                    "indicadores_parametros_ordem": 1,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 17
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 3,
                    "indicadores_parametros_nome_normalizado": "gestantes-saude-bucal",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 29.0,
                    "estado_nome_normalizado": "goias",
                    "id": 50891,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Gestantes Saúde Bucal",
                    "indicadores_parametros_ordem": 3,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 14
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 4,
                    "indicadores_parametros_nome_normalizado": "citopatologico",
                    "indicadores_parametros_meta": 40.0,
                    "indicadores_resultados_porcentagem": 9.0,
                    "estado_nome_normalizado": "goias",
                    "id": 56388,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Cobertura Citopatológico",
                    "indicadores_parametros_ordem": 4,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 948
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 5,
                    "indicadores_parametros_nome_normalizado": "polio",
                    "indicadores_parametros_meta": 95.0,
                    "indicadores_resultados_porcentagem": 36.0,
                    "estado_nome_normalizado": "goias",
                    "id": 62776,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Cobertura Polio e Penta",
                    "indicadores_parametros_ordem": 5,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 75
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 5,
                    "indicadores_parametros_nome_normalizado": "polio",
                    "indicadores_parametros_meta": 95.0,
                    "indicadores_resultados_porcentagem": 8.0,
                    "estado_nome_normalizado": "goias",
                    "id": 67340,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Cobertura Polio e Penta",
                    "indicadores_parametros_ordem": 5,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 127
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 2,
                    "indicadores_parametros_nome_normalizado": "pre-natal-sifilis-hiv",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 58.0,
                    "estado_nome_normalizado": "goias",
                    "id": 67395,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Pré-Natal (Sífilis e HIV)",
                    "indicadores_parametros_ordem": 2,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 1
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 6,
                    "indicadores_parametros_nome_normalizado": "hipertensao",
                    "indicadores_parametros_meta": 50.0,
                    "indicadores_resultados_porcentagem": 5.0,
                    "estado_nome_normalizado": "goias",
                    "id": 67415,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Hipertensão (PA Aferida)",
                    "indicadores_parametros_ordem": 6,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 896
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 7,
                    "indicadores_parametros_nome_normalizado": "diabetes",
                    "indicadores_parametros_meta": 50.0,
                    "indicadores_resultados_porcentagem": 6.0,
                    "estado_nome_normalizado": "goias",
                    "id": 72865,
                    "municipio_nome": "Abadia de Goias",
                    "indicadores_parametros_nome": "Diabetes (Hemoglobina Glicada)",
                    "indicadores_parametros_ordem": 7,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 254
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 4,
                    "indicadores_parametros_nome_normalizado": "citopatologico",
                    "indicadores_parametros_meta": 40.0,
                    "indicadores_resultados_porcentagem": 9.0,
                    "estado_nome_normalizado": "goias",
                    "id": 77429,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Cobertura Citopatológico",
                    "indicadores_parametros_ordem": 4,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 988
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 6,
                    "indicadores_parametros_nome_normalizado": "hipertensao",
                    "indicadores_parametros_meta": 50.0,
                    "indicadores_resultados_porcentagem": 5.0,
                    "estado_nome_normalizado": "goias",
                    "id": 77430,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Hipertensão (PA Aferida)",
                    "indicadores_parametros_ordem": 6,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 885
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 7,
                    "indicadores_parametros_nome_normalizado": "diabetes",
                    "indicadores_parametros_meta": 50.0,
                    "indicadores_resultados_porcentagem": 12.0,
                    "estado_nome_normalizado": "goias",
                    "id": 77431,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Diabetes (Hemoglobina Glicada)",
                    "indicadores_parametros_ordem": 7,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 215
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 1,
                    "indicadores_parametros_nome_normalizado": "pre-natal-6-consultas",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 37.0,
                    "estado_nome_normalizado": "goias",
                    "id": 77433,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Pré-Natal (6 consultas)",
                    "indicadores_parametros_ordem": 1,
                    "indicadores_parametros_peso": 1.0,
                    "diff_numerador_para_meta": 13
                },
                {
                    "estado_sigla": "GO",
                    "estado_nome": "Goiás",
                    "municipio_id_sus": "520005",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "indicadores_parametros_id": 3,
                    "indicadores_parametros_nome_normalizado": "gestantes-saude-bucal",
                    "indicadores_parametros_meta": 60.0,
                    "indicadores_resultados_porcentagem": 34.0,
                    "estado_nome_normalizado": "goias",
                    "id": 77434,
                    "municipio_nome": "Abadia de Goiás",
                    "indicadores_parametros_nome": "Gestantes Saúde Bucal",
                    "indicadores_parametros_ordem": 3,
                    "indicadores_parametros_peso": 2.0,
                    "diff_numerador_para_meta": 15
                }
            ]        </p>
        <hr>
        <p><b>Requisição</b> /impulsoprevine/indicadores/?estado_nome=goias ou /impulsoprevine/indicadores/?estado_sigla=go</p>
        <p><b>Retorno</b> Mesmo objeto do exemplo anterior para cada cidade do estado informado</p>
        <hr>
        <p><b>Requisição</b> /impulsoprevine/indicadores/?indicadores_parametros_id=5 ou /impulsoprevine/indicadores/?indicadores_nome=polio</p>
        <p><b>Retorno</b> Mesmo objeto do primeiro exemplo com todos os dados para o indicador informado</p>

    </div>
</body>
</html>
"""


def html():
    return content
