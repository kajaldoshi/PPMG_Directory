# Teacher Directory application in Python/Django

<h2>Problem Statement:</h2> <br>
Create a Directory app containing all the Teachers in a given school.<br>
Each teacher should have the following information:<br>
<ul>First Name</ul>
<ul>Last Name</ul>
<ul>Profile picture</ul>
<ul>Email Address</ul>
<ul>Phone Number</ul>
<ul>Room Number</ul>
<ul>Subjects taught</ul>

1. Teachers can have the same first name and last name but their email address should be unique.
2. A teacher can teach no more than 5 subjects.
3. The directory should allow Teachers to filtered by first letter of last name or by subject.
4.  You should be able to click on a teach in the directory and open up the profile page. From there you can see all details for the teacher.
5.  An Importer will be needed to allow Teachers details to be added to the system in bulk. This should be secure so only logged in users can run the importer.
6.  The CSV attached contains a list of teacher who need to be uploaded as well as the filename for the profile image. Profile images are in the attached Zip file.
if an image is not present for the profile then you should use a default placeholder image.
7.  You can use SQLite for the database backend for simplicity


<h3>
Steps of setting up the project:</h3><br>
Pre-Requisite: <br>
1.  Python 3.8

<h3> Execute below commands: </h3><br>
<li> python -m pip install django</i> <br>
<li> python manage.py makemigrations</li><br>
<li> python manage.py migrate </li><br>
<li> python manage.py createsuperuser --username=admin --email=kajjaldoshi@gmail.com </li><br>
<li> python manage.py collectstatic </li><br>
<li> python manage.py runserver 0.0.0.0:8080 </li><br>

After starting the server, access the django admin site using: <br>http://localhost:8080/admin
<br> Note: <br>
** Use the username and password of superuser created in above step for log in.<br>
** Import CSV option is available under Teacher module.<br>
** For importing pictures , directly upload zip files containing the pictures and csv file containing the name of the picture to be mapped<br>