# JJKChat

## Objectives
1. Understand the design, implementation and use of an application backed by a database
system.
2. Understand the use of the E-R model for database application design.
3. Gain experience by implementing applications using layers of increasing complexity and
fairly complex data structures.
4. Gain further experience with Web programming concepts including REST and HTTP.

## Overview
You will design, implement and test a simple database application for photo messaging in a social context, like Instagram but based on chat groups. The application has a UI that runs these operations, backed by a database engine:
1. Register a user with the application
2. Login to the application
3. Create a chat group with a given name
4. Add a user to your contacts list based on name, last name, and either 1) phone or 2) email
address.
5. Add a contact to a chat group
6. Remove a user from a chat group
7. Remove a user from the contacts list
8. Remove a chat group (only the owner)
9. Post a photo and message to a chat group. The message can include hashtags.
10. See the photos, the original message that came with the photo, and any replies
11. Like a photo posted on a chat group
12. Dislike a photo posted on a chat group
13. Reply to the original photo message posted on a chat group

## Optionally, you application can support the following for extra credit:
1. Post a video to a group
2. Run from a cloud (Heroku, Amazon, google)
3. Run on a mobile phone
In addition, you will develop a web-based dashboard that will provide statistics such as:
1. Trending topics via #hashtags
2. Total number of posts per day
3. Total number of replies per day
4. Total number of likes per day
5. Total number of dislikes per day
6. Most Active users per day
7. Number of posts per day by some user
8. Number of replies to a given photo
9. Number of likes to a given photo
10. Number of likes to a given photo
You will be given a more specific list of statistics later on.

The data in the application is managed by a relational database system, and exposed to the
client applications through a REST API. You will build the database application and REST API, which form the backend of the system. Your database engine must be relational, and you must implement the code in either Java, Python, or JavaScript. The backend will provide server-side support for the operations mentioned before. Your solution MUST follow the Model-View-Controller Design Pattern. In this scheme, your solution will be organized as follows:
1) View – applications, JavaScript pages, and HTML pages will handle all interaction
with the users and will show results from operations performed on the database. This
is the client code for the application. The client MUST NOT interact directly with the
database. They must talk through the REST API. I recommend using ReactJS for the
UI.
2) Controller – Java, Python, or JavaScript objects will act as controllers. Each object
will get a request, create a business service object to handle the request, collect the
results from the methods in this business service object and forward the results to the
client using JavaScript Object Notation (JSON). This MUST be implemented with
web services using either Java Jersey, Python Flask, or NodeJS.
3) Model – a set of business service objects that implement all tasks and access to the
database system. You cannot use ORM APIs for this layer. You implement this
with Data Access Objects (DAOs) written in Java, Python, or JavaScript. The DAO
send straight SQL to the underlying database system.

You are required to use the facilities of the ECE Computer Labs at UPRM, or your personal
laptops. As IDE, I recommend you use InteliJ, PyCharm, WebStorm, or Eclipse IDE for Java
EE developers to build your solution.