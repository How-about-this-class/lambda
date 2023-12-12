from pydantic import BaseModel


class ProfessorBase(BaseModel):
    name: str


class ProfessorCreate(ProfessorBase):
    pass


class Professor(ProfessorBase):
    name: str
    
    class Config:
        from_attributes = True


class PortalBase(BaseModel):
    lecture_name: str
    department: str
    academic_number: str
    survey_cnt: str
    total_cnt: str
    semester: str
    option_1: str
    option_2: str
    option_3: str
    option_4: str
    option_5: str


class PortalCreate(PortalBase):
    detail_uk: int


class Portal(PortalBase):
    detail_uk: int
    professors: list[Professor] = []

    class Config:
        from_attributes = True


class ApiResponse(BaseModel):
    status: str
    data: list[Portal] = []
