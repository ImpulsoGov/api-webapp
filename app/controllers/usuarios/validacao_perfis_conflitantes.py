from typing import Iterable

RELACAO_DE_CONFLITOS_POR_PERFIL = {
    8: set([9]),
    9: set([8])
}


class ValidationError(Exception):
    pass


def validar_perfis_conflitantes(
    novo_perfil: int,
    perfis_cadastrados: Iterable,
) -> None:
    """Levanta um erro se houver perfis cadastrados que conflitam com o novo perfil

    Parameters
    ----------
    novo_perfil : int
        Número do novo perfil a ser cadastrado
    perfis_cadastrados : Iterable
        Iterável com números dos perfis já cadastrados

    Raises
    ------
    ValidationError
        Lança um ValidationError quando algum dos perfis cadastrados
        é conflitante com o novo perfil a ser cadastrado
    """

    perfis_conflitantes = RELACAO_DE_CONFLITOS_POR_PERFIL.get(novo_perfil, set())
    conflitos = set(perfis_cadastrados).intersection(perfis_conflitantes)

    if conflitos:
        raise ValidationError(f"""
        O perfil {novo_perfil} não pode ser adicionado pois os perfis
        conflitantes {conflitos} já estão cadastrados
        """)
