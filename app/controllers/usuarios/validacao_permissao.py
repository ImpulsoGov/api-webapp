class PermissionError(Exception):
    pass


def validar_permissao(perfis_usuario: list, perfil_permitido: int):
    if perfil_permitido not in perfis_usuario:
        raise PermissionError("Usuário não possui permissão para executar esta ação")
