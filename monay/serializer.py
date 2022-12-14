from .models import Usuario, Cliente, PgtoEmprestimo, Emprestimo
from .models import Endereco, Contato, Conta, Favorito, Extrato
from .models import Transacao, Cartao, Fatura
from rest_framework import serializers
from pictures.contrib.rest_framework import PictureField

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'cpfUsuario', 'senhaUsuario', 'statusUsuario']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nomeCliente', 'dataNascimento', 'usuario', 'email']
    # fotoCliente = PictureField()

# esse só permite que o admin cadastre a foto
# class FotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FotosCliente
#         fields = ['id', 'nome', 'foto']
#     foto = PictureField()

# esse permite o usuario cadastrar a foto
# class FotoInSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cliente
#         fields = ['fotoCliente']

class PgtoEmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PgtoEmprestimo
        fields = ['valorPgto','dataPgto', 'dataVenc', 'emprestimo']
        def create(self, validated_data):
            if self.validated_data['valorPgto'] <= 0 :
                return Response ({
                        'erro' : 'no puedes transferir'
                    })
            return super().create(validated_data)


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ['statusEmprest', 'dataEmprest', 'valorEmprest', 'qtdParcelas', 'jurosEmprest', 'contaCliente']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['numero', 'rua', 'bairro', 'cidade', 'estado', 'cep', 'cliente']

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ['telefoneCliente', 'emailCliente', 'cliente']

class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['agencia', 'numeroConta', 'tipoConta', 'cliente', 'saldoConta']

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = ['nomeContato', 'chaveTipo', 'chaveValor', 'contaDestinatario', 'contaRemetente']

class ExtratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extrato
        fields = ['contaExtrato', 'valorExtrato', 'dataExtrato', 'todasOperacoes']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['valorTransacao', 'dataTransacao','destinatario','remetente']
        # def create(self, validated_data):
        #     if self.validated_data['valorTransacao'] > 'saldoConta':
        #         return Response ({
        #             'erro' : 'no puedes transferir'
        #         })
        #         #destinatario - (validated_data['valorTransacao'])
        #     return super().create(validated_data)
    
class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['numeroCartao','tipoCartao','contaCliente','validadeCartao', 'cvcCartao']

class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = ['dataVencimento','valorFatura', 'dataPagamento','cartao']
    