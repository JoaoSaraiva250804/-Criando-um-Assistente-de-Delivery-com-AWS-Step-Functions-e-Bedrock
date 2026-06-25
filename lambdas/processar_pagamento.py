import json

def lambda_handler(event, context):
    """
    Simula a integração com um gateway de pagamento.
    """
    print("Processando pagamento para o pedido:", json.dumps(event))
    
    total_pedido = event.get("total", 0.0)
    
    # Regra mockada simples: se o total for maior que 0, aprova
    if total_pedido > 0:
        return {
            "pagamentoStatus": "SUCESSO",
            "transacaoId": "987654321-XYZ",
            "cliente_id": event.get("cliente_id"),
            "itens": event.get("itens")
        }
    else:
        return {
            "pagamentoStatus": "FALHA",
            "motivo": "Valor do pedido zerado ou inválido."
        }
