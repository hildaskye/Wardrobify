# Wardrobify

Team:

* Dylan Winn - Shoes
* Kristen Lungstrum - Hats

## Design

## Shoes microservice

For the Shoes Microservices I made a BinVO and a Shoes model which used the BinVO as a ForeignKey. BinVO is being polled once every minute. The API can create shoes and view a list of all shoes at http://localhost:8080/api/shoes/ and can get the information for an individual shoe or delete it at http://localhost:8080/api/shoes/<id>. Finally, I added React functionality by creating a form, making a list page (with delete functionality), confirming all was working, and making nav links.

## Hats microservice

For the Hats microservice I created 2 models, Hat and LocationVO. LocationVO is polling from the Location model in the Wardrobe microservice. I created 2 views that allows a user to list, add, and delete, a hat. Then I created 2 forms using React, one to List the Hats, and the other to add a new hat. After that I integrated them into App.js and added the links to the Nav.js page.
