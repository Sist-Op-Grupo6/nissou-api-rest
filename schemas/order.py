def orderEntity(item) -> dict:
  return {
        "id": str(item["_id"]),
        "order_date": item["order_date"],
        "customer_name": item["customer_name"],
        "product_name": item["product_name"],
  }

def orderListEntity(entity) -> list:
  return [orderEntity(item) for item in entity]
