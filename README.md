![orders6](https://github.com/user-attachments/assets/fb41ca3e-593f-4c52-9063-eb004def4f8f)
![portfolio5](https://github.com/user-attachments/assets/cdf3862b-4630-4bfd-80a8-185ecda65172)
![trades4](https://github.com/user-attachments/assets/1dcbb544-b5d6-4144-9f95-8330d864a5ea)
![3](https://github.com/user-attachments/assets/56b79bb5-53f8-4897-93c2-8fd0218d0bd2)
![orders2](https://github.com/user-attachments/assets/dcc2b1d9-fe4b-40ae-8f71-5be8662ff0a7)
![instruments](https://github.com/user-attachments/assets/59a1a9e2-85d0-4e0e-88a4-8416585ae68b)

Bajaj Broking – Trading API Wrapper SDK (Simulation)

*Overview*

This project is a simulated Trading Backend SDK built as part of the Bajaj Broking Campus Hiring Assignment.
It demonstrates the design and implementation of RESTful APIs that mimic core trading workflows used in online stock broking platforms.

The system allows users to:

View tradable instruments

1)Place BUY/SELL orders

2)Check order status

3)View executed trades

4)View portfolio holdings

This is a simulation only. No real market or Bajaj Broking live API integration is used.

*Technology Stack:*

Language: Python 3

Framework: Flask

API Format: REST (JSON)

Data Storage: In-memory (Python lists & dictionaries)

Authentication: Mocked (single hardcoded user)

Project Structure:
bajaj-trading-sdk/
│
├── app.py              
# Main Flask application
├── requirements.txt   
 # Python dependencies
└── README.md          
 # Project documentation

*Setup & Run Instructions:*

1)Clone / Download the Project
git clone <your-github-repo-link>
cd bajaj-trading-sdk Or extract the ZIP file and open the folder.

2)Create Virtual Environment 
python -m venv venv
source venv/bin/activate    # macOS / Linux
venv\Scripts\activate       # Windows

3)Install Dependencies
pip install -r requirements.txt

4)Run the Application
python app.py


Server will start at:

http://127.0.0.1:5000

 API Endpoints
*1) Get Instruments*

Endpoint
GET /api/v1/instruments

Response

[
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

*2) Place Order*
Endpoint
POST /api/v1/orders
Request Body

{
  "symbol": "TCS",
  "quantity": 2,
  "orderType": "BUY",
  "orderStyle": "MARKET"
}


Response

{
  "orderId": "uuid",
  "symbol": "TCS",
  "quantity": 2,
  "orderType": "BUY",
  "orderStyle": "MARKET",
  "price": null,
  "status": "EXECUTED"
}


Validations

Quantity must be > 0

Price is mandatory for LIMIT orders

*3) Get Order Status*

Endpoint

GET /api/v1/orders/{orderId}


Response

{
  "orderId": "uuid",
  "status": "EXECUTED"
}

*4) Get Trades*

Endpoint

GET /api/v1/trades


Response

[
  {
    "tradeId": "uuid",
    "orderId": "uuid",
    "symbol": "TCS",
    "quantity": 2,
    "price": 3500
  }
]

*5) Get Portfolio**

Endpoint

GET /api/v1/portfolio


Response

[
  {
    "symbol": "TCS",
    "quantity": 2,
    "averagePrice": 3500,
    "currentValue": 7000
  }
]

*Order Execution Logic:**

• MARKET Orders: Executed immediately

• LIMIT Orders: Accepted with validation (execution simulated)

Trades are generated automatically for executed orders

Portfolio is updated based on BUY and SELL operations

*Assumptions Made:**

• Single hardcoded user (no authentication)

• Market price is static (mocked)

• Orders execute immediately for MARKET type

• No persistence (data resets when server restarts)

• No real exchange connectivity

API Testing:

• APIs were tested using:

• Browser (GET requests)

• Postman (GET & POST requests)

*Key Highlights:**

• Clean RESTful API design

• In-memory trading simulation

• Proper validations & error handling

• Beginner-friendly and readable code

• Covers all functional requirements of the assignment

*Future Enhancements: **

Swagger / OpenAPI documentation

Persistent database (SQLite / H2)

User authentication

Order cancellation support

Unit tests

Dockerization

**Conclusion:**

This project demonstrates a clear understanding of:

 • Backend API design

• Trading system fundamentals

• REST principles

• Clean and maintainable code structure

It fulfills all the mandatory requirements specified in the Bajaj Broking assignment.



