content="""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Impulso - Municípios</title>
</head>
<body>
    <div>
        <h1>API Impulso - Municípios</h1>
        <h2>Orientações para o endpoint /suporte/municipios/</h2>
    </div>
    <div>
        <h3>Retorno</h3>
        <p>Retorna informações do Município dado parametro</p>
        <hr>
        <h3>Parametros</h3>
        <p>id_sus : Codigo de identificação do SUS para o município</p>
        <p>municipio_nome : Nome do município normalizado (Sem acentos, espaço substituidos por traço, todas as letras minúsculas) </p>
        <p>estado_nome : Nome do estado(Unidade Federativa) normalizado (Sem acentos, espaço substituidos por traço, todas as letras minúsculas) </p>
        <p>estado_sigla : Sigla do estado(Unidade Federativa) </p>
    </div>
    <div>
        <hr>
        <h3>Exemplos</h3>
        <p><b>Requisição </b>/suporte/municipios/?id_sus=520005 ou /suporte/municipios/?municipio_nome=abadia-de-goias</p>
        <p><b>Observação:</b> <i>Se houverem duas cidades com o mesmo nome o endpoint retornará os dados de ambas, para retorno unico especifique o parametro estado_sigla em conjunto exemplo /suporte/municipios/?municipio_nome=abadia-de-goias&estado_sigla=go</i></p>
        <p><b>Retorno </b>
            [
                {
                    "estado_sigla": "GO",
                    "municipio_id_ibge": "5200050",
                    "mesorregiao_id_ibge": "5203",
                    "regiao_imediata_nome": "Goiânia",
                    "estado_nome": "Goiás",
                    "municipio_nome": "Abadia de Goiás",
                    "mesorregiao_nome": "Centro Goiano",
                    "regiao_intermediaria_id_ibge": "5201",
                    "municipio_nome_normalizado": "abadia-de-goias",
                    "microrregiao_id_ibge": "52010",
                    "regiao_intermediaria_nome": "Goiânia",
                    "estado_nome_normalizado": "goias",
                    "slug": "go-abadia-de-goias",
                    "microrregiao_nome": "Goiânia",
                    "estado_id_ibge": "52",
                    "ddd": 62,
                    "regiao_saude_id": "52001",
                    "municipio_eh_capital": false,
                    "municipio_comarca_id_judiciario": "5209200",
                    "regiao_saude_nome": "Central",
                    "id": 5306,
                    "municipio_id_sus": "520005",
                    "macrorregiao_nome": "Centro-Oeste",
                    "regiao_imediata_id_ibge": "520001",
                    "macrorregiao_id_ibge": "5"
                }
            ]
        </p>
        <hr>
        <p><b>Requisição</b> /suporte/municipios/?estado_sigla=go ou /suporte/municipios/?estado_nome=goias</p>
        <p><b>Retorno</b> Mesmo objeto do exemplo anterior para cada cidade do estado informado</p>
    </div>
</body>
</html>
"""
def html():
    return content