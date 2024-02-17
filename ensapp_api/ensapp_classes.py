from typing import Any
from dataclasses import dataclass

# For Account Infos
@dataclass
class AdditionalInfos:
    validEmail: str
    phoneNumber: str

    @staticmethod
    def from_dict(obj: Any) -> 'AdditionalInfos':
        _validEmail = str(obj["Informations complémentaires"][0]["info_value"])
        _phoneNumber = str(obj["Informations complémentaires"][1]["info_value"])
        return AdditionalInfos(_validEmail, _phoneNumber)

@dataclass
class PersonalInfos:
    lastName: str
    firstName: str
    identificationNumber: str
    dateOfBirth: str
    placeOfBirth: str
    nationality: str

    @staticmethod
    def from_dict(obj: Any) -> 'PersonalInfos':
        _lastName = str(obj["Informations personnelles"][0]["info_value"])
        _firstName = str(obj["Informations personnelles"][1]["info_value"])
        _identificationNumber = str(obj["Informations personnelles"][2]["info_value"])
        _dateOfBirth = str(obj["Informations personnelles"][3]["info_value"])
        _placeOfBirth = str(obj["Informations personnelles"][4]["info_value"])
        _nationality = str(obj["Informations personnelles"][5]["info_value"])
        return PersonalInfos(_lastName, _firstName, _identificationNumber, _dateOfBirth, _placeOfBirth, _nationality)
@dataclass
class UniversityInfos:
    appogeNumber: str
    cne_Massar: str
    education_level: str
    education_field: str

    @staticmethod
    def from_dict(obj: Any) -> 'UniversityInfos':
        _appogeNumber = str(obj["Informations universitaires"][0]["info_value"])
        _cne_Massar = str(obj["Informations universitaires"][1]["info_value"])
        _education_level = str(obj["Informations universitaires"][2]["info_value"])
        _education_field = str(obj["Informations universitaires"][3]["info_value"])
        return UniversityInfos(_appogeNumber, _cne_Massar, _education_level, _education_field)
    
@dataclass
class AccountInfos:
    personal_infos: PersonalInfos
    university_infos: UniversityInfos
    additional_infos: AdditionalInfos

    @staticmethod
    def from_dict(obj: Any) -> 'AccountInfos':
        _personal_infos = PersonalInfos.from_dict(obj)
        _university_infos = UniversityInfos.from_dict(obj)
        _additional_infos = AdditionalInfos.from_dict(obj)
        return AccountInfos(_personal_infos, _university_infos, _additional_infos)
    
#------------------------------------------------------------------------------------
    
# For AccountInfoCount
    
@dataclass
class AllInfosCount:
    last_emploi_date: str
    allnews_in_two_week: int
    not_read_messages_count: int
    document_demand_waiting_status: int
    appointment_demand_waiting_status: int
    available_convocations: int

    @staticmethod
    def from_dict(obj: Any) -> 'AllInfosCount':
        _last_emploi_date = str(obj.get("last_emploi_date"))
        _allnews_in_two_week = int(obj.get("allnews_in_two_week"))
        _not_read_messages_count = int(obj.get("not_read_messages_count"))
        _document_demand_waiting_status = int(obj.get("document_demand_waiting_status"))
        _appointment_demand_waiting_status = int(obj.get("appointment_demand_waiting_status"))
        _available_convocations = int(obj.get("available_convocations"))
        return AllInfosCount(_last_emploi_date, _allnews_in_two_week, _not_read_messages_count, _document_demand_waiting_status, _appointment_demand_waiting_status, _available_convocations)
    
#------------------------------------------------------------------------------------
    
# For Books Library


@dataclass
class Book:
    id: int
    title: str
    writerName: str
    editor: str
    category: str
    is_available: bool
    book_image: str

    @staticmethod
    def from_dict(obj: Any) -> 'Book':
        _id = obj.get("id")
        _title = obj.get("title")
        _writerName = obj.get("infos")[0].get("info_value")
        _editor = obj.get("infos")[1].get("info_value")
        _category = obj.get("infos")[2].get("info_value")
        _is_available = obj.get("is_available")
        _book_image = obj.get("book_image")
        return Book(_id, _title, _writerName, _editor, _category, _is_available, _book_image)
    
#------------------------------------------------------------------------------------
    
# For Books Filters

@dataclass
class Filter:
    filter_name: str
    filter_id: int

    @staticmethod
    def from_dict(obj: Any) -> 'Filter':
        _filter_name = str(obj.get("filter_name"))
        _filter_id = int(obj.get("filter_id"))
        return Filter(_filter_name, _filter_id)
    
#------------------------------------------------------------------------------------
    
# For News

@dataclass
class Infos:
    publication_date: str
    concerned_education_levels: str
    concerned_education_fields: str

    @staticmethod
    def from_dict(obj: Any) -> 'Infos':
        _publication_date = str(obj["infos"][0]["info_value"])
        _concerned_education_levels = str(obj["infos"][1]["info_value"])
        _concerned_education_fields = str(obj["infos"][2]["info_value"])
        return Infos(_publication_date, _concerned_education_levels, _concerned_education_fields)
    
class AllNews:
    index: int
    title: str
    infos: Infos
    more_info_short_message: str
    more_info_complete_message: str
    more_info_link: str

    @staticmethod
    def from_dict(obj: Any) -> 'AllNews':
        _index = int(obj.get("index"))
        _title = str(obj.get("title"))
        _infos = Infos.from_dict(obj.get("infos"))
        _more_info_short_message = str(obj.get("more_info_short_message"))
        _more_info_complete_message = str(obj.get("more_info_complete_message"))
        _more_info_link = str(obj.get("more_info_link"))
        return AllNews(_index, _title, _infos, _more_info_short_message, _more_info_complete_message, _more_info_link)

@dataclass
class News:
    news_count: int
    all_news: list[AllNews]

    @staticmethod
    def from_dict(obj: Any) -> 'News':
        _news_count = int(obj.get("news_count"))
        _all_news = [AllNews.from_dict(y) for y in obj.get("all_news")]
        return News(_news_count, _all_news)


#------------------------------------------------------------------------------------
    
# For Exam Convocation

@dataclass
class ExamConvocation:
    control_type: str
    convocation_url: str

    @staticmethod
    def from_dict(obj: Any) -> 'ExamConvocation':
        _control_type = str(obj.get("control_type"))
        _convocation_url = str(obj.get("convocation_url"))
        return ExamConvocation(_control_type, _convocation_url)