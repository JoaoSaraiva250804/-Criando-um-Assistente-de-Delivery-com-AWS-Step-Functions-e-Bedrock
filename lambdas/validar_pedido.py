import json

def lambda_handler(event, context):
    """
    Simula a validação do pedido recebido do cliente.
    """
    print("Recebendo evento do Step Functions:", json.dumps(event))
    
    # Simulação de validação de dados obrigatórios
    if "cliente_id" in event and "itens" in event:
        return {
            "statusCode": 200,
            "status": "VALIDADO",
            "cliente_id": event["cliente_id"],
            "itens": event["itens"],
            "total": event.get("total", 0.0)
        }
    else:
        raise Exception("Dados do pedido inválidos ou incompletos.")
