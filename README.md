
# Ensapp Api for Python 💻

![App Screenshot](https://github.com/AbdellahDeveloper/ensapp_api/raw/main/images/ENSAPP%20API%20Banner.png)

![Static Badge](https://img.shields.io/badge/Awesome%20API-8A2BE2?logo=windows&logoColor=white)

Implementation Of Ensapp Rest API in Python :
>[![Ensapp](https://img.shields.io/badge/Ensapp%20Rest%20API-32a852?style=for-the-badge&logo=webpack&logoColor=white)](https://github.com/AbdellahDeveloper/ensapp_api)



## Installation ⚙️

To install it, use :

```bash
  pip install ensapp
```


## Usage ✍

### Import Ensapp Package

```python
from ensapp_api import ensapp
```
### Create Instance Of ensapp
replace appoge and password with yours
```python
ensapp_instance = ensapp('appoge','password')
```

### Available Functions

#### Account Management
```python
ensapp_instance.GetAccountInfos() # Get All Account Infos such as firstname,lastname...
ensapp_instance.GetAllInfosCount() # Get Your Account's Infos Counts
ensapp_instance.PostAccountVerificationData("firstname","lastname",...) # Post Account Verification Data
ensapp_instance.ChangeEmail("e.g. newEmail@email.com") # Change Linked Email 
ensapp_instance.ChangePassword("e.g. newpassword") # Change Password
ensapp_instance.ChangePhoneNumber("e.g. 0600000000") # Change Linked Phone Number
```
#### Books Library
```python
ensapp_instance.GetLibraryBooksByPageIndex("page_index") # Retreive All Books By Page Index e.g. 1,2,...
ensapp_instance.GetLibrarySearchingFilters() # Retreive All Existing Searching Filters e.g. Informatique-3
ensapp_instance.SearchForBooksByFilterID_PageIndex("filter_id","page_index") # Retreive All Books By Filter ID from GetLibrarySearchingFilters() and Page Index
```
#### News
```python
ensapp_instance.GetAllNews() # Get All Ensapp News
```
#### Exam & Emploi
```python
ensapp_instance.GetEmploiDuTempsURL() # Get Your Emploi_Du_Temps Download URL
ensapp_instance.GetExamConvocationDetails() # Get Your Exam Convocation Download URL
```
#### Ensapp Services
```python
ensapp_instance.GetAllProgramChangesIDs() # Get All Program Changes IDs
ensapp_instance.SendProgramChangeDemand("program_id") # Replace program_id by your choosen one from GetAllProgramChangesIDs()

ensapp_instance.GetDiversServicesIDs() # Get All Services IDs
ensapp_instance.SendDiversServiceDemandByID("service_id") # Replace service_id by your choosen one from GetDiversServicesIDs()

ensapp_instance.GetListeningCellsIDs() # Get All Listening Cells IDs
ensapp_instance.SendListeningAppointmentDemandByID("appointment_id") # Replace appointment_id by your choosen one from GetListeningCellsIDs()

ensapp_instance.GetStagesIDs() # Get All Stages IDs
ensapp_instance.StartConventionStageByID("stage_id") # Replace stage_id by your choosen one from GetStagesIDs()
```



## 🛠 Built With
![Static Badge](https://img.shields.io/badge/Python%203.12-6b32fa?logo=python&logoColor=white)




# Hi, I'm Abdellah Elidrissi! 👋

Passionate developer and student with a diverse skill set that spans across various domains. From Web Development utilizing technologies like Asp.net Core MVC, Node.js, HTML, CSS, JavaScript, and React, to Android Development with expertise in Java and Flutter, I've ventured into Desktop Development using WinForms in C# and even dived into the world of Games Development, specializing in Unreal Engine. Additionally, I have a knack for 3D Design, leveraging tools like Blender to bring creative ideas to life.

I embarked on this journey in the world of programming at the age of 13, and my trajectory has been a fascinating evolution, starting from desktop applications to conquering the realms of Android, Games, and finally Web Development. Currently, I'm studying at ENSA MARRAKECH.

With a genuine love for programming, I find joy in turning concepts into functional and aesthetically pleasing applications. I'm excited to see what challenges and innovations lie ahead in this ever-evolving field.
