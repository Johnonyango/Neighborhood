# NEIGHBORHOOD
###### By **[JOHN ONYANGO](https://github.com/Johnonyango/Neighbors)**


## Description
[NEIGHBORHOOD](https://hoodiez.herokuapp.com/)application allows users to connect with their fellows from the same hood and share experiences and updates.

## Setup/Installation Requirements
1. Live site at https://hoodiez.herokuapp.com/ 
2. Copy  and  Paste the clone button the link on your terminal
3. cd to the clone folder
4. Install requirements e.g:
_*pip install django==1.11 -- to install django _*
_*pip intsall django-bootstrap3._*
5. Run the app on server by command python3.6 manage.py runserver.

## Specifications
1. Users can view different businesses available around their hoods
2. Users can change their hoods any time they so wish to.
3. Users can edit their bio information.


## Activate virtual environment
Activate virtual environment using python3.6 as the default handler

virtualenv -p /usr/bin/python3.6 venv && source venv/bin/activate

## Create the Database
1. Run psql command
2. CREATE DATABASE award;
3. \c gallery to connect to your database

##Run initial Migration
python3.6 manage.py makemigrations instagram
python3.6 manage.py migrate

# Running Tests
* python3.6 manage.py test

## Run the app
python3.6 manage.py runserver
Open terminal on localhost:8000
copy paste to your preffered browser



## Known Bugs 
No bugs documented so far

##BDD
<table>
    <tr>
      <th>Behavior</th> 
      <th>Input</th> 
      <th>Output</th>   
    </tr>
    <tr>
        <td>Display all the neigborhoods available</td>
        <td>User clicks to add a neihgborhood</td>
        <td>redirected to a form where they add a neighborhood</td>
    </tr>
    
</table>

## Technologies & Resources/Tools Used
Technologies used include:
* Python3.6(Django==1.11) 
* HTML
* CSS
* Bootstrap
* Postgres Database
* Heroku - for app hosting live
* Git - for app details


## Contact for support:
For more info or assistance(If there is a bug in my code), please contact:
j.yayah7@gmail.com

## MIT License
Copyright (c) 2019 John Onyango

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2019 JOHN ONYANGO