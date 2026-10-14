# Family Static API

A **Python Flask** REST API that manages members of the "Jackson" family using a custom class instead of a database.

**Tech:** Python · Flask · object-oriented data structure · Postman for testing

## How it works

- `FamilyStructure` class ([`src/datastructures.py`](src/datastructures.py)) holds members in a private list and exposes `add_member`, `delete_member`, `get_member` and `get_all_members`, generating an ID for each new member
- Flask routes ([`src/app.py`](src/app.py)) call those methods and return JSON

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/members` | All family members |
| GET | `/member/<id>` | One member |
| POST | `/member` | Add a member: `{ "first_name": "Tommy", "age": 23, "lucky_number": [34, 65] }` |
| DELETE | `/member/<id>` | Remove a member |

## Run it

```bash
pipenv install
pipenv run start     # http://localhost:3000
```

Built as part of the 4Geeks Academy Full Stack Software Development program (2023), starting from the academy's exercise template (original notes in [`docs/BOILERPLATE_README.md`](docs/BOILERPLATE_README.md)).
