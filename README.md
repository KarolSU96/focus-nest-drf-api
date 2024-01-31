# Focus Nest API


## Description
Focus Nest API is a back-end side of my full stack portfolio project of the Code Institute Full Stack Web Development Course. It is Django Rest Framework based API, which uses Python as it's main language. The API has implemented authorisation, search and filter functionality. The user is able to create tasks, assign them to the collections and manage them. 

## Features
The users are able to create their profiles. There is full crud functionality assured for tasks and collections. The users can filter the tasks aswell as the collectinons.  

## Models
// Here will the data diagram go. Filter the apps and command the grav to make only my models, not whole data model that comes by default with django.

### ContactForm Model

-   **Fields:**
    
    -   `owner`: A one-to-one relationship with the built-in User model.
    -   `created_at`: The timestamp indicating when the profile was created.
    -   `name`: The name associated with the user's profile.
    -   `image`: An image associated with the user's profile.
    -   `total_tasks`: The total number of tasks associated with the user.
    -   `total_collections`: The total number of task collections associated with the user.
    -   `finished_tasks`: The number of tasks marked as finished by the user.
    -   `current_goals`: A field for the user to specify their current goals.
-   **Description:**
The Profile model represents user profiles within the system. It is linked to the standard User model, capturing information such as name, image, task statistics, and current goals. Signals are utilized to keep track of task and task collection counts associated with the user.
    

### TaskCollection Model

-   **Fields:**
    
    -   `title`: The title or name of the task collection.
    -   `owner`: A foreign key relationship with the User model.
    -   `due_date`: The due date for the entire task collection.
    -   `created_at`: The timestamp indicating when the task collection was created.
    -   `description`: A brief description of the task collection.
-   **Description:** 
The TaskCollection model represents collections or groups of tasks. It includes fields for the title, owner (user associated with the collection), due date, creation timestamp, and a brief description.
    

### Task Model

-   **Fields:**
    
    -   `owner`: A foreign key relationship with the User model.
    -   `task_name`: The name or title of the task.
    -   `priority`: The priority level of the task (High, Medium, Low).
    -   `is_done`: A boolean indicating whether the task is marked as done.
    -   `created_at`: The timestamp indicating when the task was created.
    -   `due_date`: The due date for the task.
    -   `notes`: Additional notes or details about the task.
-   **Description:**
The Task model represents individual tasks in the system. It includes fields for the task name, priority, completion status, creation timestamp, due date, and notes. The model supports organization by allowing tasks to be associated with specific collections. 

### Profile Model

-   **Fields:**

    - `owner`: A one-to-one relationship with the built-in User model.
    - `created_at`: The timestamp indicating when the profile was created.
    - `name`: The name associated with the user's profile.
    - `image`: An image associated with the user's profile.
    - `total_tasks`: The total number of tasks associated with the user.
    - `total_collections`: The total number of task collections associated with the user.
    - `finished_tasks`: The number of tasks marked as finished by the user.
    - `current_goals`: A field for the user to specify their current goals.
- **Description:**
The Profile model represents the user profiles within the system. It is linked to the standard User model, capturing information such as name, image, task statistics, and current goals. Signals are used 



## API Endpoints

| URL                        | HTTP Method | CRUD Operation | View Type | POST/Put Data Format Example                                                                                                                                                                        | Sample Response                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------- | ----------- | -------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Profiles endpoints         |             |                |           |                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /profiles/                 | GET         | Read           | List      |                                                                                                                                                                                                     | [<br>{<br>"id": 3,<br>"owner": "gandalf",<br>"created_at": "2024-01-27T17:25:47.385938Z",<br>"name": "",<br>"image": "https://res.cloudinary.com/dnblfoxuu/image/upload/v1/media/../default_profile_d7stiw",<br>"total_tasks": 0,<br>"total_collections": 0,<br>"finished_tasks": 0,<br>"current_goals": "",<br>"is_owner": false<br>},<br>]                                                                                                                                                                                                                                                        |
| /profiles/id               | GET         | Read           | Detail    |                                                                                                                                                                                                     | {<br>"id": 3,<br>"owner": "gandalf",<br>"created_at": "2024-01-27T17:25:47.385938Z",<br>"name": "",<br>"image": "https://res.cloudinary.com/dnblfoxuu/image/upload/v1/media/../default_profile_d7stiw",<br>"total_tasks": 0,<br>"total_collections": 0,<br>"finished_tasks": 0,<br>"current_goals": "",<br>"is_owner": false<br>}                                                                                                                                                                                                                                                                   |
| /profiles/id               | PUT         | Update         | Detail    | Admin use only.<br>{<br>"name":"string",<br>"image":"ImageField",<br>"total_tasks":"Int",<br>"total_collections":"Int",<br>"finished_tasks":"int",<br>"current_goals":"Max 500 word charfield"<br>} |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Tasks endpoints            |             |                |           |                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /tasks/                    | GET         | Read           | List      |                                                                                                                                                                                                     | {<br>"count": 1,<br>"next": "http://8000-karolsu96-focusnestdrfa-pffz5glr0n3.ws-eu107.gitpod.io/tasks/?page=1",<br>"previous": null,<br>"results": [<br>{<br>"id": 1,<br>"owner": "admin",<br>"profile_id": 1,<br>"created_at": "16 Jan 2024",<br>"task_name": "Eee Makarena Edited",<br>"priority": "high",<br>"is_done": false,<br>"due_date": "30 Jan 2024",<br>"notes": "Dale a tu cuerpo alegría Macarena",<br>"is_owner": true<br>},<br>}                                                                                                                                                     |
| /tasks/                    | POST        | Create         | List      | {<br><br>"task_name":"First Task",<br><br>"priority":"High/Medium/Low",<br><br>"is_done":"bool",<br><br>"due_date":"DD-MM-YY",<br><br>"notes":"Text field"<br><br>}                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /tasks/id                  | GET         | Read           | Detail    |                                                                                                                                                                                                     | {<br>"id": 1,<br>"owner": "admin",<br>"profile_id": 1,<br>"created_at": "16 Jan 2024",<br>"task_name": "Eee Makarena Edited",<br>"priority": "high",<br>"is_done": false,<br>"due_date": "30 Jan 2024",<br>"notes": "Dale a tu cuerpo alegría Macarena",<br>"is_owner": true<br>}                                                                                                                                                                                                                                                                                                                   |
| /tasks/id                  | PUT         | Update         | Detail    | {<br><br>"task_name":"First Task",<br><br>"priority":"High/Medium/Low",<br><br>"is_done":"bool",<br><br>"due_date":"DD-MM-YY",<br><br>"notes":"Text field"<br><br>}                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /tasks/id                  | DELETE      | Delete         | Details   |                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Task collections endpoints |             |                |           |                                                                                                                                                                                                     |
| /task_collections/         | GET         | Read           | List      |                                                                                                                                                                                                     | {<br>"count": 2,<br>"next": null,<br>"previous": null,<br>"results": [<br>{<br>"id": 1,<br>"owner": "admin",<br>"title": "First Test Task Collection Edit",<br>"due_date": "29 Feb 2024",<br>"created_at": "18 Jan 2024",<br>"description": "Description is working.",<br>"tasks": [<br>1,<br>2,<br>3,<br>4,<br>5<br>],<br>"is_owner": true<br>},<br>{<br>"id": 2,<br>"owner": "admin",<br>"title": "Collection 2",<br>"due_date": "31 Mar 2024",<br>"created_at": "18 Jan 2024",<br>"description": "Second collection without tasks",<br>"tasks": [<br>13<br>],<br>"is_owner": true<br>}<br>]<br>} |
| /task_collections/         | POST        | Create         | List      | {<br>"title":"string",<br>"due_date":"date field",<br>"description":"text field, max 500 char",<br>"tasks":"list of tasks, foreign key"<br>}                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /task_collections/id       | GET         | Read           | Detail    |                                                                                                                                                                                                     | {<br>"id": 1,<br>"owner": "admin",<br>"title": "First Test Task Collection Edit",<br>"due_date": "29 Feb 2024",<br>"created_at": "18 Jan 2024",<br>"description": "Description is working.",<br>"tasks": [<br>1,<br>2,<br>3,<br>4,<br>5<br>],<br>"is_owner": true<br>}                                                                                                                                                                                                                                                                                                                              |
| /task_collections/id       | PUT         | Update         | Detail    | {<br>"title":"string",<br>"due_date":"date field",<br>"description":"text field, max 500 char",<br>"tasks":"list of tasks, foreign key"<br>}                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /task_collections/id       | DELETE      | Delete         | Detail    |                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Contact forms endpoints    |             |                |           |                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| /contact_forms/            | GET         | Read           | List      |                                                                                                                                                                                                     | {<br>"count": 2,<br>"next": null,<br>"previous": null,<br>"results": [<br>{<br>"id": 1,<br>"name": "Karol",<br>"email": "abc@cba.com",<br>"subject": "Contact subject test",<br>"message": "Contact message test",<br>"created_at": "2024-01-19T15:00:40.364359Z"<br>},<br>{<br>"id": 2,<br>"name": "Non Logged In User",<br>"email": "Nonlogo@logo.com",<br>"subject": "Contact form subject text... ::: I want to log in.",<br>"message": "Message text.",<br>"created_at": "2024-01-20T10:55:20.824925Z"<br>}<br>]<br>}                                                                          |
| /contact_forms/            | POST        | Create         | List      | {<br>"name":"string",<br>"email":"email field";<br>"subject":"string",<br>"message":"string /text field max 500 char"<br>}                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
## Technologies used
-   **Django:** The foundation of the project, Django is a web framework that helps in building and managing web applications.
    
-   **Cloudinary:** This service allows seamless storage and management of media files (like images) in the cloud.
    
-   **dj-database-url:** Simplifies the configuration of the database connection, making it easier to deploy and manage.
    
-   **dj-rest-auth:** Manages authentication processes, ensuring that users can securely access the application.
    
-   **Django Allauth:** An authentication system that provides features like social account authentication and overall account management.
    
-   **Django Cloudinary Storage:** Integrates Cloudinary with Django's storage system, aiding in efficient file handling.
    
-   **Django CORS Headers:** Handles Cross-Origin Resource Sharing (CORS), making sure that the API can securely communicate with frontend applications.
    
-   **Django Rest Framework:** A toolkit for building Web APIs with Django, providing essential features like serialization and authentication.
    
-   **DRF Simple JWT:** Manages JSON Web Tokens (JWT) for user authentication and authorization within Django Rest Framework.
    
-   **Gunicorn:** A server that handles the deployment of the application in a production environment.
    
-   **OAuthlib:** Implements the OAuth request-signing logic, contributing to secure user authentication.
    
-   **Pillow:** A library for handling images and their manipulation.
    
-   **Psycopg2:** An adapter for connecting Django with the PostgreSQL database, ensuring seamless integration.
    
-   **PyJWT:** Manages JSON Web Tokens for secure communication between the frontend and backend.
    
-   **Python3 OpenID:** Facilitates secure and decentralized user authentication.
    
-   **pytz:** A library for managing time zones, ensuring accurate and standardized time handling.
    
-   **Requests OAuthlib:** A library for supporting OAuth, facilitating secure interactions with OAuth-enabled services.
    
-   **SQLparse:** Assists in processing and manipulating SQL queries for effective database operations.


## Testing


### PEP8 
The files were tested were validated with Code Institute Python Linter.
Results: 

- contact_forms/models.py: All clear, no errors found.
- contact_forms/serializers.py: All clear, no errors found.
- contact_forms/urls.py: All clear, no errors found.
- contact_forms/views.py: All clear, no errors found.
- drf_api/permissons.py: All clear, no errors found.
- drf_api/serializers.py: All clear, no errors found.
- drf_api/urls.py: All clear, no errors found.
- drf_api/views.py: All clear, no errors found.
- profiles/models.py: All clear, no errors found.
- profiles/serilizers.py: All clear, no errors found.
- profiles/urls.py: All clear, no errors found.
- profiles/views.py: All clear, no errors found.
- task_collections/models.py: All clear, no errors found.
- task_collections/serializers.py: All clear, no errors found.
- task_collections/urls.py: All clear, no errors found.
- task_collections/views.py: All clear, no errors found.
- tasks/models.py: All clear, no errors found.
- tasks/serializers.py: All clear, no errors found.
- tasks/urls.py: All clear, no errors found.
- tasks/views.py: All clear, no errors found.


### Manual Test

The manual testing of the API of the project were made to assure the correctly working backend for the whole project.
Here are the results: 

| Test Case                               | Expected                                           | Testing                                      | Result                                              |
| --------------------------------------- | -------------------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| \*\*Profiles\*\*                        |                                                    |                                              |                                                     |
| Create a new user profile               | User profile is created successfully               | Created a new user profile                   | User profile created as expected                    |
| Update profile information              | Profile information is updated successfully        | Updated name, image, and current goals       | Profile information updated as expected             |
| Test profile ordering                   | Profiles are ordered based on creation time        | Created multiple profiles at different times | Profiles ordered correctly                          |
|                                         |                                                    |                                              |                                                     |
| \*\*Tasks\*\*                           |                                                    |                                              |                                                     |
| Create a new task                       | Task is created successfully                       | Created a new task                           | Task created as expected                            |
| Update an existing task                 | Task is updated successfully                       | Modified task name, priority, and due date   | Task updated as expected                            |
| Mark a task as done                     | Task status is updated to done                     | Marked a task as done                        | Task status updated as expected                     |
| Delete a task                           | Task is deleted, and counts are updated            | Deleted a task                               | Task deleted, counts updated as expected            |
|                                         |                                                    |                                              |                                                     |
| \*\*Task Collections\*\*                |                                                    |                                              |                                                     |
| Create a new task collection            | Task collection is created successfully            | Created a new task collection                | Task collection created as expected                 |
| Update an existing task collection      | Task collection is updated successfully            | Modified title, due date, and description    | Task collection updated as expected                 |
| Delete a task collection                | Task collection is deleted, and counts are updated | Deleted a task collection                    | Task collection deleted, counts updated as expected |
|                                         |                                                    |                                              |                                                     |
| \*\*Contact Form\*\*                    |                                                    |                                              |                                                     |
| Test Case                               | Expected                                           | Testing                                      | Result                                              |
| Submit a contact form with valid data   | Form entry is saved correctly                      | Submitted contact form with valid data       | Form entry saved as expected                        |
| Submit a contact form with invalid data | Form shows appropriate error handling              | Submitted contact form with missing email    | Error displayed                                     |

## Deployment

### 1. Get the Code
- Fork or clone this repository from GitHub. 

### 2. Cloudinary Account Setup
- You'll need a Cloudinary to host the profile images. If you don't have an account you can sign up at [Cloudinary](https://cloudinary.com/).

### 3. Cloudinary API Key
- Log in to Cloudinary and head to the 'dashboard'
- Find the 'API Enviroment variable' and copy the value starting with 'cloudinary://'. You will need this value for deployment.

### 4. Heroku App Setup
- Log in to your Heroku account. 
- Click 'Create new app' from 'New' menu at the top right. 
- Enter name for your app and choose the region.
- Click 'create app'

### 5. ElephantSQL Setup
- Log in to Elephant SQL
- Click 'Create new instance' on the dashboard.
- Name the plan, choose 'Tiny Turlte(free) and select the nearest data center.
- Click 'Review'
- Copy the ElephantSQL databse URL (starts with 'postgres://')

### 6. Configure Heroku APP
- Go back to Heroku dashboard. 
- Click on 'Settings'.
- Find and click 'reveral config vars'
- Add following config vars:
    -   `CLOUDINARY_URL`: Paste the Cloudinary URL.
    -   `DATABASE_URL`: Paste the ElephantSQL postgres database URL.
    -   `SECRET_KEY`: Your secret key.
    -   `ALLOWED_HOST`: Your Heroku app's URL.

### 7. Deploy to Heroku
- Click the 'Deploy' tab.
- Under 'Deployment Method' select 'GitHub' and connect to your repo.
- In the 'Manual Deploy' section choose 'main' as the branch and click 'Deploy Branch'

### 8. Open the deployed site

- Your APi will be deployed shortly. Once complete, you'll get link to the deployed site. 

## Acknowledgements

