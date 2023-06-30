# TASK_5

Create a Django app that manages a library of books. The primary functionality includes creating books, fetching a book's details, updating book information, and deleting books.

Requirements:

1. Create a Django model Book with the following fields:

    * id (This should be an auto-incrementing integer and the primary key)
    * title (A character field to store the book's title)
    * author (A character field to store the author's name)
    * publication_date (A date field to store the book's publication date)
    * isbn (A character field to store the book's ISBN number)
    * price (A decimal field to store the price of the book)
    * synopsis (A text field to store a brief synopsis of the book)
2. Implement CRUD (Create, Read, Update, Delete) operations for the Book model using Django views.
3. Implement URL routes for the CRUD operations in the urls.py file. The routes should follow RESTful API conventions.
4. Implement appropriate Django forms for creating and updating book instances.
5. Include appropriate validations for all fields in the Book model.

## Solution

To create a Django app that manages a library of books with the given requirements, follow the steps below:

### Step 1: Set up the Django Project

Create a new Django project by running the following command:

```code
django-admin startproject library_manager
```

Change to the project directory:

```code
cd library_manager
```

Create a new Django app called "library":

```code
python manage.py startapp library
```

Update the project settings in `'library_manager/settings.py'`:

* Add 'library' to the INSTALLED_APPS list.
* Set the database configurations in DATABASES according to your preferences.

### Step 2: Define the Book model

Open the file `'library/models.py'` and replace its content with the following code.

Run the following command to create the corresponding database tables:

```code
python manage.py makemigrations library
python manage.py migrate
```

### Step 3: Implement CRUD Operations

1. Open the file `'library/views.py'` and replace its content with the following code.

2. Create the directory `'library/templates/library'` and add the following HTML templates inside it:

    * book_list.html
    * book_detail.html
    * book_create.html
    * book_update.html
    * book_confirm_delete.html

3. Open the file `'library/forms.py'` and add the following code to define the BookForm

### Step 4: Configure URL Routes

1. Open the file `'library/urls.py'` and replace its content with the following code.

2. Open the file `'library_manager/urls.py'` and add the following code inside the urlpatterns list:

```python
path('', include('library.urls')),
```

### Step 5: Run the Django Development Server

Start the Django development server:

```code
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your web browser to access the
