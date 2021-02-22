# Shyft API
An API for tapping into the Shyft bike sharing marketplace.

### Links
- [Front End Repository](https://github.com/pvallerie/shyft-client)
- [Deployed API](https://git.heroku.com/shyft-api.git)
- [Deployed Frontend](pvallerie.github.io/shyft-client/)

### Technologies Used
- Python
- Django and Django REST Framework
- PostgreSQL
- Heroku
- CURL

### Setup and Installation
1. Setup your client for development
2. In your config file, set `production API url` to point to `https://aqueous-atoll-85096.herokuapp.com`

#### Authentication:
| Action | Method | Path |
| ----------- | ----------- | ----------- |
| Sign-Up | POST | `https://aqueous-atoll-85096.herokuapp.com/sign-up/`
| Sign-In | POST  | `https://aqueous-atoll-85096.herokuapp.com/sign-in/`
| Change-Password |  PATCH | `https://aqueous-atoll-85096.herokuapp.com/change-pw/`
| Sign-Out | DELETE | `https://aqueous-atoll-85096.herokuapp.com/sign-out/`

sample JSON for Sign-Up:
```JSON
'{
  "credentials": {
    "email": "johndoe@gmail.com",
    "password": "Pa$$word123",
    "password_confirmation": "Pa$$word123"
  }
}'
```

#### Bikes (Token Required):
| Views | Method | Path |
| ----------- | ----------- | ----------- |
| Create | POST | `https://aqueous-atoll-85096.herokuapp.com/bikes`
| Index All | GET | `https://aqueous-atoll-85096.herokuapp.com/bikes`
| Show | GET | `https://aqueous-atoll-85096.herokuapp.com/bikes/{bikeId}`
| Update | PATCH | `https://aqueous-atoll-85096.herokuapp.com/bikes/{bikeId}`
| Delete | DELETE | `https://aqueous-atoll-85096.herokuapp.com/bikes/{bikeId}`

sample JSON for Create bike:
```JSON
'{
  "bike": {
    "name": "Trek Remedy 3",
    "type": "Mountain",
    "size": "Medium",
    "location": "Portsmouth, NH"
  }
}'
```

### Loans (Token Required):
| Views | Method | Path |
| ----------- | ----------- | ----------- |
| Create | POST | `https://aqueous-atoll-85096.herokuapp.com/loans`
| Index All | GET | `https://aqueous-atoll-85096.herokuapp.com/loans`
| Update | PATCH | `https://aqueous-atoll-85096.herokuapp.com/loans/{loanId}`
| Delete | DELETE | `https://aqueous-atoll-85096.herokuapp.com/loans/{loanId}`

sample JSON for Create loan (date must be formatted as YYYY-MM-DD):
```JSON
'{
  "loan": {
    "pickup_date": "2021-10-14",
    "dropoff_date": "2021-10-16",
    "bike": "2"
  }
}'
```

### ERD
![Shyft ERD](https://i.imgur.com/wIHSf3F.jpg?1 "Shyft ERD")
