# Crumbs Backend
Backend for crumbs, made for the GreatUniHack '22.

## API endpoints:
* POST /signup
  * For the signup endpoint, you will get User Registered Message
* POST /donate
  * For the Donate Endpoint you will get "Food Collected" message
* POST /order
  * For the order endpoint you will get a json object with the food details, eg. {"Food": "milk", "Type": "non cooked", "Diet": "veg", "Expiry": "14/11"}
  * The API deletes the food from the STOCK collection if there is a match and in the front-end just display that the food is delivered, indicating the food is in the STOCK and will be delivered.
* POST /userinfo
  * For the userinfo endpoint you will get the user details as a json object, eg. {"email": "user@gmail.com", "no": "000", "address": "Manchester", "points": 110}

## Spec
Here is [the POSTMAN link](https://www.getpostman.com/collections/6c68318fab122825affa) for calling the endpoints with query parameters.

You could also [use this link](https://galactic-station-424755.postman.co/workspace/1abafe91-8e52-4a1b-8b16-0cfe1ea84070/collection/21894869-74695489-2458-4234-8d86-3712a123215c?action=share&creator=21894869) for running tests against the API.