import pytest
from app.controllers.usuarios.validacao_perfis_conflitantes import (
    validar_perfis_conflitantes,
    ValidationError
)

PERFIS_CADASTRADOS = [1, 4]
NOVO_PERFIL_SEM_RELACAO_DE_CONFLITOS = 3
NOVO_PERFIL_COM_RELACAO_DE_CONFLITOS = 8
LISTA_PERFIS_CADASTRADOS_NAO_ITERAVEIS = [1, 5.5]
NOVOS_PERFIS_VS_NENHUM_PERFIL_CADASTRADO = [
    (3, []),
    (3, [None]),
    (9, []),
    (9, [None])
]
NOVOS_PERFIS_VS_CADASTRADOS_QUE_CONFLITAM = [
    (8, [1, 9]),
    (9, [8])
]


# Referências:
# https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions
# https://docs.pytest.org/en/7.1.x/example/parametrize.html
@pytest.mark.parametrize(
    "perfis_novos_com_relacao_de_conflito, perfis_cadastrados_que_conflitam_com_novo",
    NOVOS_PERFIS_VS_CADASTRADOS_QUE_CONFLITAM
)
def test_erro_de_validacao_levantado_para_perfis_que_conflitam(
    perfis_novos_com_relacao_de_conflito,
    perfis_cadastrados_que_conflitam_com_novo
):
    """
    Testa se ValidationError é levantado quando algum dos
    perfis cadastrados conflita com o novo perfil
    """
    with pytest.raises(ValidationError):
        validar_perfis_conflitantes(
            novo_perfil=perfis_novos_com_relacao_de_conflito,
            perfis_cadastrados=perfis_cadastrados_que_conflitam_com_novo
        )


# Referência:
# https://miguendes.me/how-to-check-if-an-exception-is-raised-or-not-with-pytest
def test_erro_de_validacao_nao_levantado_para_perfil_sem_conflito():
    """
    Testa se ValidationError não é levantado quando o novo
    perfil não possui relação de conflito
    """
    try:
        validar_perfis_conflitantes(
            novo_perfil=NOVO_PERFIL_SEM_RELACAO_DE_CONFLITOS,
            perfis_cadastrados=PERFIS_CADASTRADOS
        )
    except ValidationError:
        assert False, "'validar_perfis_conflitantes' levantou um ValidationError"


def test_erro_de_validacao_nao_levantado_para_perfil_que_tem_conflitos():
    """
    Testa se ValidationError não é levantado quando o novo
    perfil possui relação de conflito, mas não possui
    nenhum perfil conflitante cadastrado
    """
    try:
        validar_perfis_conflitantes(
            novo_perfil=NOVO_PERFIL_COM_RELACAO_DE_CONFLITOS,
            perfis_cadastrados=PERFIS_CADASTRADOS
        )
    except ValidationError:
        assert False, "'validar_perfis_conflitantes' levantou um ValidationError"


@pytest.mark.parametrize(
    "novo_perfil, nenhum_perfil_cadastrado",
    NOVOS_PERFIS_VS_NENHUM_PERFIL_CADASTRADO
)
def test_erro_de_validacao_nao_levantado_quando_nao_ha_perfis_cadastrados(
    novo_perfil,
    nenhum_perfil_cadastrado
):
    """
    Testa se ValidationError não é levantado quando não há perfis
    cadastrados independente do novo perfil possuir
    ou não relação de conflito
    """
    try:
        validar_perfis_conflitantes(
            novo_perfil=novo_perfil,
            perfis_cadastrados=nenhum_perfil_cadastrado
        )
    except ValidationError:
        assert False, "'validar_perfis_conflitantes' levantou um ValidationError"
