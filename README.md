# Feedback API

This API allows users to retrieve and submit feedback for various subjects and teachers.


## Endpoints


```http
GET /feedback/
```
Retrieve all feedback entries.


#### Response
A JSON array of feedback objects.

##### Sample Response
```json
[
    {
        "user": {
            "username": "R200027",
            "year": "E3",
            "section": "E"
        },
        "subject": "OS",
        "teacher": "bro",
        "taken": true,
        "remarks": "bro is good",
        "created": "2024-07-24T09:48:52.079463+05:30"
    },
    {
        "user": {
            "username": "R200027",
            "year": "E3",
            "section": "E"
        },
        "subject": "SE",
        "teacher": "madam bro",
        "taken": true,
        "remarks": "madam is good",
        "created": "2024-07-24T09:48:52.079463+05:30"
    }
]
```

### Creating new feedback
``` http
POST /feedback/
```

#### Request Body
A JSON object representing the feedback to be submitted.
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id_number` | `string` | **Required**. CR's ID number |
| `subject` | `string` | **Required**. The subject |
| `teacher` | `string` | **Required**. The subject's teacher |
| `taken` | `boolean` | **Required**. If the class is taken or not |
| `remarks` | `string` | **Optional**.  |

##### sample body
```json
{
    "id_number": "RXXXXXX",
    "subject": "APIs",
    "teacher": "X sir",
    "taken": true, 
    "remarks": "good"
}
```

## Setup and Installation
Install the required dependencies.
   ```sh
   pip3 install -r requirements.txt
   ```

## Running the API
1. Run the application.
   ```sh
   python3 manage.py runserver
   ```
   
2. The API will be available at `http://localhost:8000/feedback/`.

## Registering a CR
Login using admin credentials
`http://localhost:8000/admin/`

To create an admin
```sh
python3 manage.py createsuperuser
```

