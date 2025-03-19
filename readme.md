# Новый тестовый апи но круче

## Здесь реализованно больше функций и сложнее структура типо бд

Короче тут уже тоже всё **_СТРОГО ЛОКАЛЬНО_** <div>
Вот так це чудо запускаеться кста по коду
```aiignore
uvicorn app.main:app
```
Кста по коду

Вот моё:
```python
@app.delete("/order/order_delete/{id}")
def delete_order(id : int):
    orders = read_json()
    for order in orders:
        if order["status"] != "Подан":
            if order.get("id") == id:
                orders.remove(order)
                write_json(orders)
                return {"message" : "Заказ успешно удалён", "order" : order}
            else:
                raise HTTPException(status_code = 403, detail = "Заказа с статусом 'Поадн' не может быть удалён")
    raise HTTPException(status_code = 401, detail = "Заказ не найден")
```
Так вот тут типо чё то не красиво так что чат гпт предложил сделать круче вот его варик:
```python
@app.delete("/order/order_delete/{id}")
def delete_order(id: int):
    orders = read_json()
    # Ищем заказ с заданным id
    order_to_delete = None
    for order in orders:
        if order.get("id") == id:
            order_to_delete = order
            break

    if order_to_delete is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    # Проверяем, что заказ со статусом 'Подан' нельзя удалить
    if order_to_delete.get("status") == "Подан":
        raise HTTPException(status_code=403, detail="Заказ со статусом 'Подан' не может быть удалён")

    orders.remove(order_to_delete)
    write_json(orders)
    return {"message": "Заказ успешно удалён", "order": order_to_delete}
```
Он круче, но там моё, а тут не моё

Кста чо узнал структура бд крутая у меня ну типо там крутой список в списке

```json
{
        "id": 0,
        "table_number": 0,
        "items": {
            "first_meal": "string",
            "second_meal": "string",
            "drink": "string"
        },
        "total_price": 0,
        "status": "string"
}
```
Так вот и я сделав это как классы короче крутая шняга:
```python
class Item(BaseModel):
    first_meal : str
    second_meal : str
    drink : str

class Order(BaseModel):
    id : int
    table_number : int
    items : Item
    total_price : int
    status : OrderState = OrderState.empty
```
Вот на эту ``status : OrderState = OrderState.empty`` не оброщате внимание, 
оно типо ссылается на список но там класс и типо выбор крутой
