# Book-Finder API (Python / Flask)

_To Start:_<br/> docker-compose up -d --build

## API Dcoumentation:

_Add author_<br/> Add new author to DB.

-   URL<br> /add-author
-   Method<br/> POST
-   URL Params<br/> None
-   Data Params<br/> name=[string], birth=[string]
-   Success Response:<br/> Code: 200 OK<br/> Content: {"message":"OK"}
-   Error Response:<br/> Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}

_Edit author_<br/> Edit author by id.

-   URL<br> /edit-author/:id
-   Method<br/> PUT
-   URL Params<br/> id=[string]
-   Data Params<br/> name=[string], birth=[string]
-   Success Response:<br/> Code: 200 OK<br/> Content: {"message":"OK"}
-   Error Response:<br/> Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}<br/>OR<br/>Code: 404 Not Found<br/> Content:
    {"message": "Author is not found"}

_Remove author_<br/> Remove author by id.

-   URL<br> /remove-author/:id
-   Method<br/> DELETE
-   URL Params<br/> id=[string]
-   Data Params<br/> None
-   Success Response:<br/> Code: 200 OK<br/> Content: {"message":"OK"}
-   Error Response: None

_Get authors_<br/> Get all authors page by page.

-   URL<br> /get-authors
-   Method<br/> GET
-   URL Params<br/> None
-   Data Params<br/> page=[int], per_page=[int]
-   Success Response:<br/> Code: 200 OK<br/> Content: { "authors": [ { "birth": "10.10.2000", "id": 1, "name": "author name 1" } ] }
-   Error Response: None

_Filter authors_<br/> Get authors filter by name/birth page by page.

-   URL<br> /filter-authors
-   Method<br/> GET
-   URL Params<br/> None
-   Data Params<br/> page=[int], per_page=[int],name=[string],birth=[string]
-   Success Response:<br/> Code: 200 OK<br/> Content: { "authors": [ { "birth": "10.10.2000", "id": 1, "name": "author name 1" } ] }
-   Error Response:<br/> Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}

_Get author_<br/> Get author by id.

-   URL<br> /get-author/:id
-   Method<br/> GET
-   URL Params<br/> id=[string]
-   Data Params<br/> None
-   Success Response:<br/> Code: 200 OK<br/> Content: { "author": { "birth": "10.10.2000", "id": 1, "name": "author name 1" } }
-   Error Response: Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}<br/>OR<br/>Code: 404 Not Found<br/> Content:
    {"message": "Author is not found"}

_Add book_<br/> Add new book to DB.

-   URL<br> /add-book
-   Method<br/> POST
-   URL Params<br/> None
-   Data Params<br/> title=[string], year_of_publication=[string], genre=[string], author_id=[int]
-   Success Response:<br/> Code: 200 OK<br/> Content: {"message":"OK"}
-   Error Response:<br/> Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}<br/>OR<br/>Code: 404 Not Found<br/> Content:
    {"message": "Author is not found"}

_Edit book_<br/> Edit book by id.

-   URL<br> /edit-book/:id
-   Method<br/> PUT
-   URL Params<br/> id=[string]
-   Data Params<br/> title=[string], year_of_publication=[string], genre=[string], author_id=[int]
-   Success Response:<br/> Code: 200 OK<br/> Content: {"message":"OK"}
-   Error Response:<br/> Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}<br/>OR<br/>Code: 404 Not Found<br/> Content:
    {"message": "Book is not found"}

_Remove author_<br/> Remove book by id.

-   URL<br> /remove-book/:id
-   Method<br/> DELETE
-   URL Params<br/> id=[string]
-   Data Params<br/> None
-   Success Response:<br/> Code: 200 OK<br/> Content: {"message":"OK"}
-   Error Response: None

_Get books_<br/> Get all books page by page.

-   URL<br> /get-books
-   Method<br/> GET
-   URL Params<br/> None
-   Data Params<br/> page=[int], per_page=[int]
-   Success Response:<br/> Code: 200 OK<br/> Content: { "books": [ { "author": { "birth": "10.10.2000", "id": 1, "name": "author name 1" },
    "genre": "genre 1", "id": 1, "yearOfPublication": "1020" } ] }
-   Error Response: None

_Filter authors_<br/> Get authors filter by name/birth page by page.

-   URL<br> /filter-authors
-   Method<br/> GET
-   URL Params<br/> None
-   Data Params<br/> page=[int], per_page=[int],title=[string], year_of_publication=[string], genre=[string], author_name=[int]
-   Success Response:<br/> Code: 200 OK<br/> Content: { "books": [ { "author": { "birth": "10.10.2000", "id": 1, "name": "author name 1" },
    "genre": "genre 1", "id": 1, "yearOfPublication": "1020" } ] }
-   Error Response:<br/> Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}

_Get book_<br/> Get book by id.

-   URL<br> /get-book/:id
-   Method<br/> GET
-   URL Params<br/> id=[string]
-   Data Params<br/> None
-   Success Response:<br/> Code: 200 OK<br/> Content: { "book": { "author": { "birth": "10.10.2000", "id": 1, "name": "author name 1" },
    "genre": "genre 1", "id": 1, "yearOfPublication": "1020" } }
-   Error Response: Code: 400 Bad Request<br/> Content: {"message": "Wrong parameters"}<br/>OR<br/>Code: 404 Not Found<br/> Content:
    {"message": "Book is not found"}
