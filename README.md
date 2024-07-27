# Feedback API

This API allows users to retrieve and submit feedback for various subjects and teachers.


### Endpoint
```
https://src.pythonanywhere.com
```

```http
GET /feedback/
```
Retrieve all feedback entries.


#### Response
A JSON array of feedback objects.


#### Query Parameters

| Parameter      | Description                                                      | Example           |
|----------------|------------------------------------------------------------------|-------------------|
| `section` | Filter by Student's Section | `A`, `E`, ...        |
| `batch`      | Filter by Batch      | `E1`, `E2`, ...               |
| `subject`      | Filter by Subject's name                           | `CLA`, `MEFA`, ...              |
| `teacher` | Filter by Teacher's name                                   | `Harinadha bro`             |
| `taken`        | Filter by taken | `true`, `false`            |
| `year` | Filter by year  | `2024` |
| `month` | Filter by month | `07` |
| `day` | Filter by day  | `23` |
| `date` | Filter by date | `2024-07-23` |

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
    "subject": "Math",
    "teacher": "sir",
    "taken": true, 
    "remarks": "sir is good"
}
```

## Registering a CR
Login using admin credentials at  `/admin/`


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
   
2. The API endpoint will be available at `http://localhost:8000`.


To create an admin locally
```sh
python3 manage.py createsuperuser
```

