# Software Engineering - Proaid
## About
**Proaid** is a doctor appointment booking and scheduling assistant web-application used for medical purposes. The platform intends to offer a variety of features to both doctors and patients such as medical record sharing, appointment booking, schedule preview and agenda organizing in general. 
         
<p align="center">
  <img src="https://github.com/OxymoroVP/Proaid/blob/main/GUI/logo.png" width="350" height="350" />
</p>

This repository is a complete project made by students at the Aristotle University of Thessaloniki taking the *Spring 2021 Software Engineering Course (8th Semester)*. Objective of *assignment1* is to:
* set the Functional & Non-Functional requirements 
* develop the User Stories (behavior scenarios) in Gherkin language 
* interact with UI/UX Design and implement static modeling into UML class diagram notation

Objective of *assignment2* is to:
* adjust corresponding design patterns to project 
* struct a RESTful web-service using SwaggerHub
* build Node-RED flows 

## Users & external systems
#### Users ####
* Doctor [desktop user only]
* Registered Patient [mobile user only]
#### External systems ####
* Notification system
* Registered patients database 
* Unregistered patients database
* External APIs [Calendar, Print, Email, Text message]

## Functional & Non-Functional Requirements
User and System requirements of the application can be found in text format files. Refer to [FunctionalReq.txt](https://github.com/OxymoroVP/Proaid/blob/main/FunctionalReq.txt) / 
[NonFunctionalReq.txt](https://github.com/OxymoroVP/Proaid/blob/main/NonFunctionalReq.txt) for an extended preview.

## User Stories 
User stories aim to facilitate sensemaking of the platform's functionality and they are implemented into 12 features, developed in <br/>*Gherkin language*.


## GUI & UML class diagram notation
#### UI/UX ####
The early-stage Graphical User Interface of Proaid is designed using the Figma editor. Some of the vector templates illustrating platform's design are provided in folder *GUI*.
Follow Figma project link [here](https://www.figma.com/file/kZ3lZFH6XMoVevtMztTlK2/Desktop-feel-(LOGIN)?node-id=0%3A1) for more.
#### UML - Static modeling ####
Structural (or Static) view emphasizes the static structure of the system using objects, attributes, operations and relationships. It includes class diagrams and composite structure diagrams and it is developed in StarUML environment. Refer to files [classes.mdj](https://github.com/OxymoroVP/Proaid/blob/main/UML/classes.mdj) / [use_case.mdj](https://github.com/OxymoroVP/Proaid/blob/main/UML/use_case.mdj) for the *class and use case* diagram correspondingly.  


## Swagger API & Node-RED
You can find the project API in SwaggerHub [here](https://app.swaggerhub.com/apis/Omada-Ergasias-7/Proaid/1.14.2#/) and the API documentation [here](https://app.swaggerhub.com/apis-docs/Omada-Ergasias-7/Proaid/1.14.2#/). The directory *python-flask-server* contains project files in order to develop the service with Python-Flask Framework. For the .json format of the Proaid API jump to *proaid-api-swagger.json*

Node-RED flows demonstrating the online services of the application are stored in *flows.json*.
 

## Contact

Nikos Karagkiozidis<br/>
Stavros Malakoudis<br/>
Vasilis Polynopoulos<br/>
Giorgos Tsakiridis<br/>
Group 7 SE2021 | ECE Faculty of Engineering, AUTh<br/> 


