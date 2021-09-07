# dummy-api
A dummy API to validate QR codes.

# Installation:

clone this repo:

  ```git clone git@github.com:robinvanleeuwen/dummy-api.git```
  
Create virtual environment and install dependencies:
  ```
  cd dummy-api
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```
  
Run the API:

  ```
  python3 app.py
  ```


The web interface will be available under http://127.0.0.1:5050/api/v1/browse

Do a validate_ticket request in the web browsable API. Check out how a JSON RPC is formatted

Check the source code for valid stuff that you have to submit, for a working example:
```
   {
      "jsonrpc": "2.0",
      "method": "validate_ticket",
      "params": {
        "email": "jantje@beton.nl",
        "token": "09KfFta3MmtBFiTz55lzqG8WcOR_IZPb8s1F4LHpZ0b1iuw",
        "qr_data:" {
          "token": "yrT5HNgXIM7x4snjtYLdNpsYUqvph7X--2uQpjGhybl9N78"
        },
      "id": "12ac8a66-7763-4a24-a9c1-02857d3f59cb"
   }
```
