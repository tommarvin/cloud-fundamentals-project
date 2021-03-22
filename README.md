# cloud-fundamentals-project

# Requirements

- Kanban Board: Trello or an equivalent Kanban Board
- Database: GCP SQL Server or other Cloud Hosted managed Database.
- Programming language: Python
- Unit Testing with Python (Pytest)
- Integration Testing with Python (Selenium)
- Front-end: Flask (HTML)
- Version Control: Git
- CI Server: Jenkins
- Cloud server: GCP Compute Engine

# My Approach

My CRUD application will allow the user to create workers and their detail's to a table which they can then view and edit as they please. I want to create the same idea as mentioned for workers, for jobs as well. I want the workers to have capabilities that can be compared to requirements of that of the jobs so the user will be able to match workers up to jobs based on what the job requires and whether the worker is capable to do the job. I will build the relationship between workers and jobs by a model called teams. Each job will have a team number, a workers connection and a job connection so that the two main tables (workers and jobs) can be connected by this third table using foreign keys.

Workers:
- A name
- Age
- A listen of things that they are capable of doing
- Contact Details

Jobs:
- Address
- A list of requirements for the job that match up with the capabilities of workers
- Start Date
- A team
- Customer Contact details

Teams:
- Have a workers id
- Have a jobs id
- A number 


# Project Tracking:
User Stories:

To help me get an idea of what I really wanted to include in my application, I used User Stories so that I had a set of clear pass or fail criteria that I could refer back to when writing the code.

![image](https://user-images.githubusercontent.com/80106830/111926916-a86f4200-8aa6-11eb-9e6c-55651897a1ae.png)


Trello Board:

To give me further clarity of what I should be doing at a given time or rather what to include in my project, I created a trello board where I could move each task along as I either began or completed it.


![image](https://user-images.githubusercontent.com/80106830/111927254-094b4a00-8aa8-11eb-9473-5ed353b17fc0.png)



# My Database Structure
![image](https://user-images.githubusercontent.com/80106830/111928127-ae672200-8aaa-11eb-973c-dac452e5b25d.png)


# Risk Assessment

# Testing

I have tested my application using pytest. I only achieved 73% coverage, leaving a large proportion of application/routes.py uncovered. This was due to the amount of routes involved within my application. There was also a lack of time dedicated to this section of the project, the time required for the testing nearer the deadline was under estimated.

![image](https://user-images.githubusercontent.com/80106830/111929471-4d414d80-8aae-11eb-99cf-9a6b585cdcfd.png)


# CI Server Jenkins









# Front End Design
I have a very simple but clear front end design for my application. My aim was to make it as simple for the user a possible with data clearly displayed and actions performed to the data easy as well. The addition of the navbar makes the application significantly easier going to and from different functions of the application. to give the navbar the hover effect i used a lot of the styling from the following page: https://www.w3schools.com/howto/howto_js_topnav.asp 

Create Worker

![image](https://user-images.githubusercontent.com/80106830/111923142-99cc5f00-8a95-11eb-8445-de80df4416ad.png)



Create Job

![image](https://user-images.githubusercontent.com/80106830/111923160-c08a9580-8a95-11eb-9775-86654a1de5c7.png)



# Read Workers
![image](https://user-images.githubusercontent.com/80106830/111923648-1102f280-8a98-11eb-88dd-d817b4825be6.png)

![image](https://user-images.githubusercontent.com/80106830/111923668-24ae5900-8a98-11eb-843c-c4fc0feaeecc.png)



Read Jobs 

![image](https://user-images.githubusercontent.com/80106830/111923713-5f17f600-8a98-11eb-9b43-650265bef0c5.png)

![image](https://user-images.githubusercontent.com/80106830/111923729-6fc86c00-8a98-11eb-9644-1608806b590c.png)

![image](https://user-images.githubusercontent.com/80106830/111923749-8a024a00-8a98-11eb-8dc6-5d39af4bac2d.png)



Edit Workers

![image](https://user-images.githubusercontent.com/80106830/111923772-af8f5380-8a98-11eb-81fd-a405eefa8df5.png)



Edit Jobs

![image](https://user-images.githubusercontent.com/80106830/111923796-cb92f500-8a98-11eb-9c98-85c87a35c7b8.png)



Create/Read/Edit Teams of workers within Jobs

![image](https://user-images.githubusercontent.com/80106830/111923809-e36a7900-8a98-11eb-9e09-1714f45bff0f.png)

![image](https://user-images.githubusercontent.com/80106830/111924248-6c82af80-8a9b-11eb-8462-35653c5c8fe4.png)

![image](https://user-images.githubusercontent.com/80106830/111923924-9f2ba880-8a99-11eb-8068-3588c8390975.png)


# Requirements.txt
![image](https://user-images.githubusercontent.com/80106830/111922721-3b9e7c80-8a93-11eb-9c49-09774ff570da.png)


 
