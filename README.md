Steps:

Start the local server in docker.
```
1. Clone the repository.
2. Open Terminal
3. "cd" inside the cloned repository
4. Run "docker-compose up"
```

Test the apis using Postman
```
1. POST api to create an invoice.
method: POST
endpoint: "http://127.0.0.1:8000/invoices/"
example body: 
{
	"customer_name": "vishal",
	"date": "2022-03-22"
}

---
example response: 
{
    "id": 2,
    "date": "2022-03-22",
    "created_at": "2022-03-03T10:53:27.715855Z",
    "customer_name": "vishal"
}
status code: (when success) 201
---

2. POST api to create an invoice item.
method: POST
endpoint: "http://127.0.0.1:8000/invoiceitem/"
example body:
{
	"invoice": 1,
	"units": 4,
	"description": "Microphones",
	"amount": 6
}

---
example response:
{
    "id": 2,
    "units": 4,
    "description": "Microphones",
    "amount": 6,
    "invoice": 1
}
status code: (success) 201
---

3. GET api to get a full invoice (along with invoice items).
method: GET
endpoint: "http://127.0.0.1:8000/invoices/<invoice_id>/"

---
example response:
{
    "id": 1,
    "date": "2022-03-22",
    "created_at": "2022-03-03T10:47:04.479864Z",
    "customer_name": "vishal",
    "items": [
        {
            "id": 1,
            "units": 4,
            "description": "Microphones",
            "amount": 6,
            "invoice": 1
        },
        {
            "id": 2,
            "units": 4,
            "description": "Microphones",
            "amount": 6,
            "invoice": 1
        }
    ],
    "total": 12
}
---
status code: 200 (when success)

4. Get all the invoices (without the invoice items)
method: GET
endpoint: "http://127.0.0.1:8000/invoices/"

example response:
[
    {
        "id": 1,
        "date": "2022-03-22",
        "created_at": "2022-03-03T10:47:04.479864Z",
        "customer_name": "vishal"
    },
    {
        "id": 2,
        "date": "2022-03-22",
        "created_at": "2022-03-03T10:53:27.715855Z",
        "customer_name": "vishal"
    }
]
```