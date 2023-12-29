# sample webservice

## Get list of customers

``` shell
jasonray@Jason-MacBook-2021 python-sample-webservice % curl -i http://127.0.0.1:8081/customers/
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.11.6
Date: Fri, 29 Dec 2023 19:31:30 GMT
Content-Type: application/json
Content-Length: 129
Connection: close

[
  {
    "id": 1,
    "name": "Alice"
  },
  {
    "id": 2,
    "name": "Bob"
  },
  {
    "id": 3,
    "name": "Charlie"
  }
]
```

## Get single customer

``` shell
jasonray@Jason-MacBook-2021 python-sample-webservice % curl -i http://127.0.0.1:8081/customers/1
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.11.6
Date: Fri, 29 Dec 2023 19:32:07 GMT
Content-Type: application/json
Content-Length: 33
Connection: close

{
  "id": 1,
  "name": "Alice"
}
```