from untils import *
from fastapi import FastAPI, Query, HTTPException

app = FastAPI()

@app.get("/")
def main_page():
    return "Добро пожаловать в наш ресторан"

@app.get("/all_orders")
def all_orders():
    return read_json()

@app.get("/order")
def zakazes(status: Optional[OrderState] = Query(None, description="Филтрация заказов по статусу")):
    orders = read_json()
    if status is None:
        return orders

    filtered_orders = [order for order in orders if order.get("status") == status.value]
    return filtered_orders

@app.get("/order/{id}")
def get_zakaz(id : int):
    zakazi = read_json()
    for zakaz in zakazi:
        if zakaz.get("id") == id:
            return zakaz
    raise HTTPException(status_code = 404, detail = "Не удалось найти такой заказ")

@app.put("/order/change_order")
def change_order(id : int, status : OrderState):
    orders = read_json()
    for order in orders:
        if order.get("id") == id:
            order["status"] = status.value
            write_json(orders)
            return {"message" : "Статус заказа изменён.", "status" : order}
    raise HTTPException(status_code = 404, detail = "Статус заказа не был изменён из за ошибки")

@app.post("/order/add_order")
def add_order(order : Order):
    orders = read_json()

    for zakaz in orders:
        if zakaz.get("id") == order.id:
            raise HTTPException(status_code= 409, detail="Не смогли добавить заказ")

    orders.append(order.model_dump())
    write_json(orders)
    return {"message" : "Заказ успешно добавлен. Ожидайте", "order" : order}

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

