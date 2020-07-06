# Simple Recipe API
###Endpoint
####/api/recipe
#####GET
For getting a list of recipes
>/api/recipe

For getting an specific recipe
>/api/recipe/{id}

For filtering by recipe name
>/api/recipe/?name={searchText}


For creating a new recipe
>/api/recipe

```
payload = {
    "name": "Escudella",
    "description": "Nunca he sabido hacerlo... pero la de Iaia esta bien buena",
    "ingredients": [{"name": "Pelota"}, {"name": "Caldo"}]
}
```
#####PATCH
For updating the ingredients of a recipe
>/api/recipe/{id}
```
payload = {
    "ingredients": [{"name": "Some"}, {"name": "SomeOther"}]
}
```
#####DELETE
For deleting a recipe
>/api/recipe/{id}

### Execution instructions
The api is build with docker. To start the application run:
> docker-compose up

To execute the tests run:
>docker-compose run app sh -c "python manage.py test"
