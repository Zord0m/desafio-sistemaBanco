def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n**** Operação falhou! O valor informado é inválido. ****")

    return saldo, extrato