from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import Usuario

def listar_todos_usuarios():
    return Usuario.query.order_by(Usuario.id.desc()).all()


def obter_usuario(usuario_id):
    return Usuario.query.get_or_404(usuario_id)

def salvar_usuario(nome,email,senha = None,usuarios_id = None):
    if not nome or not email:
        return False, "nome e email são campos obrigatorios "
    
    try:
        if usuarios_id:
            usuario = obter_usuario(usuarios_id)
            usuario.nome = nome
            usuario.email = email

            if senha and senha.strip():
                   usuario.set_senha(senha)
            
            mensagem = "usuario atualizado"
        
        else: #MODO DE CADASTRO DE USUARIOS
            if not senha:
                return False, "a senha e obrigatoria"
            
            usuario = Usuario(nome=nome,email=email)
            usuario.set_senha(senha)
            db.session.add(usuario)
            mensagem = "usuarios cadastrado com sucesso"
        
        db.session.commit()
        return True, mensagem
    
    except IntegrityError:
        db.sesseion.rollback()
        return False, "erro: este email ja esta cadastrado!!"
    
    except Exception as e:
        db.session.rollback()
        return False, f"erro interno: {str[e]}"
    
def excluir_usuarios(usuario_id):
    usuario = obter_usuario(usuario_id)
    try: 
        db.session.delete(usuario)
        db.session.commit()
        return True, "usuario deletado"
    except Exception as e:
        db.session.callback()
        return False, f"erro ao excluir o usuario: {str[e]}"