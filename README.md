# Library Management Application
<!--
![image](https://github.com/shaikh-ma/LibraryManagement/assets/88078876/2ee9af48-241d-4396-a354-b8365119e165)
-->

To launch project,
1.Make sure Python 3.6 is installed and saved in system variables.


2. Run below command in libman folder
   
```
python main.py
```
OR
3. Run main.exe

## Additional Info:
<h1>Below are the classes used in this project</h1>

```
class Book
    book_id
    title
    author
    issued_to
    is_available
    issued_date
    returned_date
    date_book_added
    book_code
    summary
    image
```
<br/>
```
class Request
    request_id
    request_user
    request_book
    request_book_title
    request_book_code
    request_date
    return_date
    is_approved
```
<br/>
```
class ReturnRequest
    request_id
    request_user
    request_book
    request_book_title
    request_book_code
    request_date
    is_approved
```
<br/>
```
class Profile
    user
    image
    roll_no
    icard_no
    class_div
```
<br/>
