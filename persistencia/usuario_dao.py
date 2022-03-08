from persistencia.abstract_dao import AbstractDAO
from entidade.usuario import Usuario

class UsuarioDAO(AbstractDAO):

    def __init__(self):
        super().__init__('usuario.pkl')

    def persist(self, usuario: Usuario):
        if self.__usuario_valido(usuario):
            super().persist(usuario.codigo, usuario)

    def remove(self, usuario: Usuario):
        if self.__usuario_valido(usuario):
            super().remove(usuario.codigo)

    def __usuario_valido(self, usuario):
        return (usuario is not None) and (isinstance(usuario, Usuario)) and (isinstance(usuario.codigo, int))