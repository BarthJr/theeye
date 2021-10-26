# Installation
```
git clone git@github.com:BarthJr/theeye.git
```
```
cd theeye
```
```
docker-compose up
```
# Documentation
To access the official documentation, please use this link: http://127.0.0.1:8000/

To interact with The Eye, use this documentation: http://127.0.0.1:8000/docs/

If you prefer Swagger, use this link: http://127.0.0.1:8000/swagger/

# Endpoints
- **Base URL:** http://127.0.0.1:8000/api/
## Events
**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
GET|/events|Returns all events
GET|/events/{id}|Returns event by id
POST|/events|Creates event
PUT|/events/{id}|Updates event
DELETE|/events/{id}|Deletes event by id

### Filters
Those filters apply only for the events list endpoint (GET)
**Field Name**|**Description**|**Type**
:--|:--|:--
session_id|It expects the UUID format|UUID
category|It allows to search for the category|Text
name|It allows to search for the name|Text
start_date|It allows to search for results from the specified date|Date or Timestamp
end_date|It allows to search for results up to the specified date|Date or Timestamp

_To filter the events for a specific date (2021-10-24), you should follow this pattern:_
- _start_date=2021-10-24T00:00:00&end_date=2021-10-24T23:59:59_
- _start_date=2021-10-24&end_date=2021-10-25_


## Errors
**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
GET|/errors|Returns all errors
GET|/errors/{id}|Returns error by id
POST|/errors|Creates error
PUT|/errors/{id}|Updates error
DELETE|/errors/{id}|Deletes error by id

### Filters
Those filters apply only for the errors list endpoint (GET)
**Field Name**|**Description**|**Type**
:--|:--|:--
start_date|It allows to search for results from the specified date|Date or Timestamp
end_date|It allows to search for results up to the specified date|Date or Timestamp

_To filter the errors for a specific date (2021-10-24), you should follow this pattern:_
- _start_date=2021-10-24T00:00:00&end_date=2021-10-24T23:59:59_
- _start_date=2021-10-24&end_date=2021-10-25_

### Validations
All the fields are mandatory. The POST will be successful, but the event will go to the errors list. 

1. session_id:
   - must be a valid UUID
1. data:
   - data field is empty
   - data field is not a valid JSON
1. timestamp:
   - invalid format
   - timestamp field is in the future

# API Examples
You can copy the commands below to use The Eye by command line using the CURL package.
## Create Event
```console
curl -X POST "http://localhost:8000/api/events/" -H  "Content-Type: application/json" -d "{    \"session_id\": \"e2085be5-9137-4e4e-80b5-f1ffddc25428\",    \"category\": \"form interaction\",    \"name\": \"submit\",    \"data\": {        \"session_id\": \"e2085be5-9137-4e4e-80b5-f1ffddc25423\",        \"category\": \"page interaction\",        \"name\": \"pageview\",        \"data\": {            \"host\": \"www.consumeraffairs.com\",            \"path\": \"/\"        },        \"timestamp\": \"2021-01-01 09:15:27.243860\"    },    \"timestamp\": \"2021-10-24 09:15:27.243860\"}"
```

## Get Events filtered by specific time range
```console
curl -X GET "http://localhost:8000/api/events/?start_date=2021-10-24&end_date=2021-10-25"
```

## Get Errors
```console
curl -X GET "http://localhost:8000/api/errors/"
```

# Assumptions
- For this project, the data field does not have a pre-defined format based on the type of event.
- The tests scenarios represent the actions that could be generated by a client application.
- The Task Queue solution was used to meet the needs related to the amount of the data received by the application (~100 events/second).
