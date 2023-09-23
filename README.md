# On the Record - Project 4 Backend
- Project By: Nicholas Smith
- [Github](https://github.com/nicholasjamessmith/ontherecord-backend)
- [Deployed Site](https://ontherecord-backend.onrender.com/)
- [Trello board](https://trello.com/b/BON8XkBD/project4)
- Technologies used:
  - Python
  - Django
  - Django REST framework
  - Postman

## Description
On the Record is a music and art review site where users are able to create, read, update, and delete reviews. Users can view a list of reviews on the home page of the site, and interact with each review by clicking on it. Clicking on a review takes users to a page where they can then view that individual reveiew and by clicking choose to update the review's information or delete the review. Updating the review requires the user to fill out text forms and click a submit button, triggering the page to reload with the updated information dispaled. Deleting a review takes the user back to home page to an updated list of reviews.

The backend server and API is built using the Django web framework, and specifically the Django REST framework. The backend code is written in Python.

The data for this project is stored using a PostgreSQL database via Neon.

The data model for each type of post on the site is a 'review', where each review includes 'artist', 'title', 'image', and 'review', each of which are string values.

The site is designed with RESTful routes architecture, giving functionality to the user experience on the frontend.

##List of Backend Endpoints

| Endpoint          | Method | Purpose                                                          |
| ----------------- | ------ | ---------------------------------------------------------------- |
| /reviews/          | GET    | displays all reviews
| /reviews/create/   | POST   | displays form for new review      |
| /reviews/:id/      | GET    | display individual show page of a review                       |
| /reviews/delete/:id/| DELETE | delete current review                                             |
| /reviews/update/:id/ | PUT    | displays form for editing review |

<img src="./media/erd.pdf" alt="ERD Diagram of Review Model">