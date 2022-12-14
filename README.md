
# Project Desc

A example Docker powered boilerplate of using postgresql with python flask


## Tech Stack

**Software Language:** Python

**Framework:** Flask Framework

**Database Type:** PostgreSQL

**Extras:** Docker, JWT, Pytest


## License

[MIT](https://choosealicense.com/licenses/mit/)


## API Reference

#### Register

```http
  POST /api/v3/merchant/user/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**.  |
| `password`| `string` | **Required**.  |

## ##
## ##

#### Login

```http
  POST /api/v3/merchant/user/login
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**.  |
| `password`| `string` | **Required**.  |


Response:
```http
{
    "status": "APPROVED",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MTAxNjIwMiwianRpIjoiNDkwZDFlMmUtOTUyNS00YTExLTg2ODAtZDRiYWNlMWNiYjBlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IntcImNoZWNrX3Bhc3N3b3JkXCI6IG51bGwsIFwiZW1haWxcIjogXCJlbWFpbFwiLCBcImZpbmRfYnlfZW1haWxcIjogbnVsbCwgXCJmaW5kX2J5X2lkXCI6IG51bGwsIFwiaWRcIjogMiwgXCJwYXNzd29yZFwiOiBcInBhc3N3b3JkXCIsIFwicXVlcnlcIjogbnVsbCwgXCJxdWVyeV9jbGFzc1wiOiBudWxsLCBcInJlZ2lzdHJ5XCI6IG51bGwsIFwic2F2ZV90b19kYlwiOiBudWxsfSIsIm5iZiI6MTY3MTAxNjIwMiwiZXhwIjoxNjcxMDE2ODAyfQ.UwclY2gs4SfjROa8r3XW8NeDqdFLFM54JL4aJtGABb4"
}
```

## ##
## ##

#### Transaction

```http
  POST /api/items/${id}
```

**NEED JWT BEARER TOKEN (Required, in header)**

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `fromDate`      | `string` | **Required**. Ex: "2022-12-11" |
| `toDate`      | `string` | **Required**. Ex: "2022-12-14" |
| `merchant`      | `integer` | **Required**. Ex: 1 |
| `acquirer`      | `integer` | **Required**. Ex: 2 |

Response:
```http
{
    "response": [
        {
            "count": 2,
            "currency": "USD",
            "total": 33
        },
        {
            "count": 2,
            "currency": "GBP",
            "total": 85
        }
    ],
    "status": "APPROVED"
}
```
## ##


## Example DB

The sample database in the main file of the project in CSV format.

`example.csv`

