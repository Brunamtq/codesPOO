from src.banco.banco import Banco
from src.conta.conta import Conta


class Criarbanco:
    if __name__ == '__main__':
        banco = Banco()
        conta1 = Conta('22.342-7')
        conta2 = Conta('22.345-9')
        banco.cadastrar(conta1)
        banco.cadastrar(conta2)
        banco.creditar(conta1.get_numero(), 700)
        banco.debitar(conta2.get_numero(), 200)
        banco.transferir(conta1.get_numero(), conta2.get_numero(), 50.00)
        print(conta1.get_saldo())
        print(banco.saldo(conta2.get_numero()))