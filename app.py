from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# -------------------- MOCK DATA --------------------

USER_ID = "demo_user"

instruments = [
    {
        "symbol": "TCS",
        "exchange": "NSE",
        "instrumentType": "EQUITY",
        "lastTradedPrice": 3500
    },
    {
        "symbol": "INFY",
        "exchange": "NSE",
        "instrumentType": "EQUITY",
        "lastTradedPrice": 1500
    }
]

orders = {}
trades = []
portfolio = {}

# -------------------- INSTRUMENT APIs --------------------

@app.route("/api/v1/instruments", methods=["GET"])
def get_instruments():
    return jsonify(instruments), 200

# -------------------- ORDER APIs --------------------

@app.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.json

    quantity = data.get("quantity")
    order_type = data.get("orderType")   # BUY / SELL
    order_style = data.get("orderStyle") # MARKET / LIMIT
    symbol = data.get("symbol")
    price = data.get("price")

    if quantity is None or quantity <= 0:
        return jsonify({"error": "Quantity must be greater than 0"}), 400

    if order_style == "LIMIT" and price is None:
        return jsonify({"error": "Price is required for LIMIT orders"}), 400

    order_id = str(uuid.uuid4())

    order = {
        "orderId": order_id,
        "symbol": symbol,
        "quantity": quantity,
        "orderType": order_type,
        "orderStyle": order_style,
        "price": price,
        "status": "PLACED"
    }

    # Simulate immediate execution for MARKET orders
    if order_style == "MARKET":
        order["status"] = "EXECUTED"
        trade = {
            "tradeId": str(uuid.uuid4()),
            "orderId": order_id,
            "symbol": symbol,
            "quantity": quantity,
            "price": get_ltp(symbol)
        }
        trades.append(trade)
        update_portfolio(symbol, quantity, trade["price"], order_type)

    orders[order_id] = order
    return jsonify(order), 201

@app.route("/api/v1/orders/<order_id>", methods=["GET"])
def get_order_status(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

# -------------------- TRADE APIs --------------------

@app.route("/api/v1/trades", methods=["GET"])
def get_trades():
    return jsonify(trades), 200

# -------------------- PORTFOLIO APIs --------------------

@app.route("/api/v1/portfolio", methods=["GET"])
def get_portfolio():
    result = []
    for symbol, data in portfolio.items():
        current_price = get_ltp(symbol)
        result.append({
            "symbol": symbol,
            "quantity": data["quantity"],
            "averagePrice": data["averagePrice"],
            "currentValue": data["quantity"] * current_price
        })
    return jsonify(result), 200

# -------------------- HELPER FUNCTIONS --------------------

def get_ltp(symbol):
    for inst in instruments:
        if inst["symbol"] == symbol:
            return inst["lastTradedPrice"]
    return 0

def update_portfolio(symbol, quantity, price, order_type):
    if order_type == "BUY":
        if symbol not in portfolio:
            portfolio[symbol] = {
                "quantity": quantity,
                "averagePrice": price
            }
        else:
            old_qty = portfolio[symbol]["quantity"]
            old_price = portfolio[symbol]["averagePrice"]
            new_qty = old_qty + quantity
            new_avg = ((old_qty * old_price) + (quantity * price)) / new_qty
            portfolio[symbol]["quantity"] = new_qty
            portfolio[symbol]["averagePrice"] = new_avg

    elif order_type == "SELL":
        if symbol in portfolio:
            portfolio[symbol]["quantity"] -= quantity
            if portfolio[symbol]["quantity"] <= 0:
                del portfolio[symbol]

# -------------------- MAIN --------------------

if __name__ == "__main__":
    app.run(debug=True)

