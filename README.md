# WH Backend Code Review Test

## Introduction

Welcome to the code review test. Over the course of the next 45 minutes, you will be presented with 5 tasks that will challenge your ability to solve problems, debug, and write efficient and effective code. This test is designed to not just evaluate your coding ability, but also your problem-solving skills, your resourcefulness, and how you approach tasks in a time-constrained environment.

We believe in the power of collective knowledge and understand the importance of external resources in day-to-day development. Therefore, you are free to use any resources at your disposal during this test. You can seek help from Google, StackOverflow, or any other forum or knowledge base that you usually rely on while coding.

As this is a live test, you will be required to share your screen and keep your webcam turned on throughout the duration. This is to provide us with a firsthand view of your approach and thought process while solving the tasks.

It's important to note that you are not alone during this process. You can ask for help or clarification at any point. However, please be aware that assistance may not always be provided; the purpose of this is to simulate real-world circumstances where immediate help might not be readily available.

Your performance will be primarily evaluated based on the tasks you manage to complete, so we strongly encourage you to attempt as many tasks as possible. The order of completion is entirely up to you. If a task seems overly challenging, feel free to move on to the next one and return later if time permits.

The objective here is not necessarily to complete all tasks but to demonstrate your coding proficiency, resourcefulness, and problem-solving capabilities. We are interested in seeing your approach to these tasks, your adaptability, and your resilience when faced with challenges.

Good luck, and may this test be an opportunity to showcase your skills and strengths!

## TASK 1

Requirements:

1. Find the route that is driven by vehicle_id=2 from the routes array.
2. Find the fastest (the route with the smalest duration) route from the routes array.
3. Find the shortest (the route with the smalest distance between locations) route from the routes array.

```python:
from typing import TypedDict, List

class LocationDef(TypedDict):
    lon: float
    lat: float

class RouteStepDef(TypedDict):
    id: int
    location: LocationDef
    arrival: int

class RouteDef(TypedDict):
    vehicle_id: int
    steps: List[RouteStepDef]

routes: List[RouteDef] = […]
```

## TASK 2

Given the following hexadecimal representation of binary data: 021500000000000039b00e0066005748a3111f67121a1818141212141616151616191818bb100000

Parse as much information given the information below:

* index: 0 | Variable identifier: header_version (MSB) | Size in string (bytes): 2 | Datatype: uint8
* index: 1 | Variable identifier: header_version (LSB) | Size in string (bytes): 2 | Datatype: uint8
* index: 2 | Variable identifier: status code (MSB) | Size in string (bytes): 2 | Datatype: uint8 (Bit 0 = sensor start, bit 1 = watchdog, bit 2 = BOR reset, bit 3 = OTA, bit 4 = RTC update, bit 5 = Error flag)
* index: 3 | Variable identifier: status code (LSB) | Size in string (bytes): 2 | Datatype: uint8

## TASK 3

Requirements:

1. Annotate on Container query if it has a DeviceToContainer (annotate true, false, or the id of the DeviceToContainer)
2. Annotate on Container query the imei or device_eui from the DeviceToContainer.device for a Container.

```python:
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields

class MobileDevice(models.Model):
    imei = models.CharField(max_length=256)

class LorawanDevice(models.Model):
    device_eui = models.CharField(max_length=32)

class Container(models.Model):
    name = models.CharField(max_length=32)

class DeviceToContainer(models.Model):
    container = models.ForeignKey(
        Container,
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    device = fields.GenericForeignKey()
```

## TASK 4

You are the manager of a popular restaurant chain. You have two warehouses that service your restaurants. You've been tasked to go through the inventory at both warehouses and provide a sorted, comprehensive list of all of your items between the two warehouses.
Your assistant has written a function complete_inventory that takes 2 integer arrays (warehouse_1 and warehouse_2) and 2 integers (x and y) and returns an array. The arrays warehouse_1 and warehouse_2 contain the product IDs of your inventory in warehouse 1 and warehouse 2 respectively, in sorted fashion. The integers x and y represent the number of initialized items in warehouse_1 and warehouse_2 respectively. Also note that warehouse_1 will be large enough to hold all values of both warehouse_1 and warehouse_2.
The goal of the function is to combine warehouse_1 and warehouse_2 into warehouse_1 in a way that you get a sorted array of product IDs from both warehouses. You found some issues with the function your assistant made and it's up to you to debug the function.

Examples:

```code
Input:
warehouse_1 = [2,3,4,0,0,0], x = 3
warehouse_2 = [1,5,9], y = 3
Output: [1,2,3,4,5,9]


Input:
warehouse_1 = [1,8,0,0,0], x = 2
warehouse_2 = [1,1,5], y = 3
Output: [1,1,1,5,8]
```

Tip: You can think of the trailing 0's in warehouse_1 as "empty shelves" or placeholders for items from warehouse_2

```python:
def complete_inventory(warehouse_1, x, warehouse_2, y):
    back_index = len(warehouse_1)
    first_pointer = x
    second_pointer = y
    while second_pointer > 0:
        if first_pointer > 0 and warehouse_1[first_pointer] > warehouse_2[second_pointer]:
            warehouse_1[back_index] = warehouse_1[first_pointer]
        else:
            warehouse_1[back_index] = warehouse_2[second_pointer]

    return warehouse_1
```

## TASK 5

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

### Bonus

* Add a search functionality to find books by title or author.
* Include pagination in the read operation for the Book model.
* Implement unit tests for the views, ensuring all edge cases are covered.
* Create a simple UI using Django templates to display the list of books and the form for creating and updating a book.

Please provide the code for the models, views, forms, URLs, and templates (if applicable). Also, include any other instructions required to get your Django app up and running.
