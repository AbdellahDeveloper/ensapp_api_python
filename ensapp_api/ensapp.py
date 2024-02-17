import requests
from .ensapp_classes import AccountInfos,AllInfosCount,Book,Filter,News,ExamConvocation

class ensapp:
    def __init__(self, appoge:str,password:str):
        """
        Ensapp Api By Abdellah Elidrissi
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------

        Initialize the Ensapp With appoge and password

        Args:
        - appoge: Your Appoge Or Email
        - password: Your Ensapp Account Password
        """
        self.appoge=appoge
        self.password=password
    
    

    def GetAccountInfos(self) -> AccountInfos:
        """
        Get Account Infos
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Fetches informations of the account provided from the ensapp api
        """
        response=requests.api.get(f"https://ensapp-api.somee.com/account_infos?username={self.appoge}&password={self.password}")
        if(response.status_code==200):
            reponse_json=response.json()
            obj=AccountInfos.from_dict(reponse_json)
            return obj
        else:
            return None
        
    def GetAllInfosCount(self) -> AccountInfos:
        """
        Get All Infos Count
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Fetches account's statistics informations of the account
        """
        response=requests.api.get(f"https://ensapp-api.somee.com/account_infos/get_all_infos_counts?username={self.appoge}&password={self.password}")
        if(response.status_code==200):
            reponse_json=response.json()
            obj=AllInfosCount.from_dict(reponse_json)
            return obj
        else:
            return None
    
    def ChangeEmail(self,newEmail:str) -> bool:
        """
        Change Linked Email
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Change the email of the account
        """
        response=requests.api.get(f"https://ensapp-api.somee.com/operations/change_email?username={self.appoge}&password={self.password}&newEmail={newEmail}")
        return response.status_code==200
    
    def ChangePhoneNumber(self,newPhoneNumber:str) -> bool:
        """
        Change Linked Phone Number
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Change the phone number of the account
        """
        response=requests.api.post(f"https://ensapp-api.somee.com/operations/change_phone_number?username={self.appoge}&password={self.password}&newPhoneNumber={newPhoneNumber}")
        return response.status_code==200

    def ChangePassword(self,current_password:str,new_password:str) -> bool:
        """
        Change Account's Password
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Change the password of the account
        - current_password : Current Account's Password
        - new_password : New Account's Password
        """
        response=requests.api.post(f"https://ensapp-api.somee.com/operations/change_password?username={self.appoge}&password={self.password}&current_password={current_password}&new_password={new_password}")
        return response.status_code==200
    
    def PostAccountVerificationData(self,firstname:str,lastname:str,arabic_firstname:str,arabic_lastname:str,birthday:str,place_of_birth:str,arabic_place_of_birth:str,bacYear:str,cin:str,massarcode:str) -> bool:
        """
        Post Account Verification Data
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Verify The account by passing all required informations of the user

        - firstname: Your First Name in French
        - lastname: Your Last Name in French
        - arabic_firstname: Your First Name in Arabic
        - arabic_lastname: Your Last Name in Arabic
        - birthday: Your Birthday (format: ##/##/####)
        - place_of_birth: Your Place Of Birth in French
        - arabic_place_of_birth: Your Place Of Birth in Arabic
        - bacYear: Year When You Got Your Bac (e.g., 2023)
        - cin: Your National Identity Card (e.g., AA112233)
        - massarcode: Your Massar Code (e.g., G1111111)
        """
        response=requests.api.post(f"https://ensapp-api.somee.com/operations/personal_data_verification?username={self.appoge}&password={self.password}&firstname={firstname}&lastname={lastname}&arabic_firstname={arabic_firstname}&arabic_lastname={arabic_lastname}&birthday={birthday}&place_of_birth={place_of_birth}&arabic_place_of_birth={arabic_place_of_birth}&bacYear={bacYear}&cin={cin}&massarcode={massarcode}")
        return response.status_code==200
    
    def GetEmploiDuTempsURL(self) -> str:
        """
        Get Emploi Du Temps Direct URL
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Get Emploi_Du_Temps Of The user's classe
        """
        response=requests.api.get(f"https://ensapp-api.somee.com/get_emploi_url?username={self.appoge}&password={self.password}")
        if(response.status_code==200):
            response_json=response.json()      
            return response_json["emploi_link"]
        else:
            return None

    def GetLibraryBooksByPageIndex(self, page_index:int) -> list[Book]:
        """
        Get Library Books By Page Index
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve library books by page index

        Args:
        - page_index: Index of the page to retrieve books from
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/library/get_books_by_page?username={self.appoge}&password={self.password}&page_index={page_index}")
        if response.status_code == 200:
            response_json = response.json()
            books = [Book.from_dict(book_data) for book_data in response_json]
            return books
        else:
            return None

    def GetLibrarySearchingFilters(self) -> list[Filter]:
        """
        Get Library Searching Filters
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve library searching filters
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/library/get_all_filters?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            filters = [Book.from_dict(filter_data) for filter_data in response_json]
            return filters
        else:
            return None

    def SearchForBooksByFilterID_PageIndex(self, filter_id:int, page_index:int) -> list[Book]:
        """
        Search For Books By FilterID and Page Index
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Search for books by filter ID and page index

        Args:
        - filter_id: ID of the filter to apply for the search
        - page_index: Index of the page to retrieve books from
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/library/filter?username={self.appoge}&password={self.password}&filter_id={filter_id}&page={page_index}")
        if response.status_code == 200:
            response_json = response.json()
            books = [Book.from_dict(book_data) for book_data in response_json]
            return books
        else:
            return None

    def GetAllNews(self) -> News:
        """
        Fetch For All News
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Fetch all news related to the user's account
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/news/get_all_news?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            news = News.from_dict(response_json)
            return news
        else:
            return None

    def GetExamConvocationDetails(self) -> ExamConvocation:
        """
        Get Exam Convocation Details
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve exam convocation details
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/services/get_exam_convocation_details?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            exam = ExamConvocation.from_dict(response_json)
            return exam
        else:
            return None

    def GetDiversServicesIDs(self) -> list[Filter]:
        """
        Get Divers Services IDs
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve diverse services IDs
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/services/get_all_divers_services?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            services = [Filter.from_dict(filter_json) for filter_json in response_json]
            return services
        else:
            return None

    def GetAllProgramChangesIDs(self) -> list[Filter]:
        """
        Get All Program Changes IDs
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve all program changes IDs
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/services/get_all_program_changes?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            services = [Filter.from_dict(filter_json) for filter_json in response_json]
            return services
        else:
            return None

    def GetListeningCellsIDs(self) -> list[Filter]:
        """
        Get Listening Cells IDs For Appointments
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve listening cells IDs for appointments
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/services/get_all_listening_cells?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            services = [Filter.from_dict(filter_json) for filter_json in response_json]
            return services
        else:
            return None

    def GetStagesIDs(self) -> list[Filter]:
        """
        Get Stages IDs
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Retrieve stages IDs
        """
        response = requests.api.get(f"https://ensapp-api.somee.com/services/get_all_stages?username={self.appoge}&password={self.password}")
        if response.status_code == 200:
            response_json = response.json()
            services = [Filter.from_dict(filter_json) for filter_json in response_json]
            return services
        else:
            return None

    def SendDiversServiceDemandByID(self, service_id:int) -> bool:
        """
        Send Divers Service Demand By Service_ID
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Send divers service demand by service ID

        Args:
        - service_id: ID of the diverse service to send demand for
        """
        response = requests.api.post(f"https://ensapp-api.somee.com/services/send_service_demand?username={self.appoge}&password={self.password}&serviceid={service_id}")
        return response.status_code == 200

    def StartConventionStageByID(self, stage_id:int) -> bool:
        """
        Start Convention Stage By Stage_ID
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Start convention stage by stage ID

        Args:
        - stage_id: ID of the convention stage to start
        """
        response = requests.api.post(f"https://ensapp-api.somee.com/services/start_convention_stage?username={self.appoge}&password={self.password}&stageid={stage_id}")
        return response.status_code == 200

    def SendListeningAppointmentDemandByID(self, appointment_id:int) -> bool:
        """
        Send Listening Appointment Demand By Listening_Cell_ID
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Send listening appointment demand by listening cell ID

        Args:
        - appointment_id: ID of the listening appointment to send demand for
        """
        response = requests.api.post(f"https://ensapp-api.somee.com/services/demand_listening_appointment?username={self.appoge}&password={self.password}&appointmentid={appointment_id}")
        return response.status_code == 200

    def SendProgramChangeDemand(self, program_id: int) -> bool:
        """
        Send Program Change Demand By ID
        ~~~~~~~~~~~~~~~~~~~~~
        ---------------------------
        Send program change demand by ID

        Args:
        - program_id: ID of the program change to send demand for
        """
        response = requests.api.post(f"https://ensapp-api.somee.com/services/demand_program_change?username={self.appoge}&password={self.password}&programid={program_id}")
        return response.status_code == 200