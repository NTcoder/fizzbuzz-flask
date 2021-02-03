
### How do I get set up? ###
* setup env varibles as per your choice
* configure .env for productions deployment if required

### How to run ###
* docker-compose -d up

### Unit tests ###
*  python test_unit.py

### How to test API ###

Method : POST

endpoint : localhost:9000/fizzbuzz

Request : 

```
{
    "input":4
}
```
Reponse :

```
"4"
```

### Test results ###
*  test.log

### Improvements ###
* Swagger UI for documentation