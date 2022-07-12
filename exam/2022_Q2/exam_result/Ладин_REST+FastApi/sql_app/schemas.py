from pydantic import BaseModel, Field


# -------------------------------------------------------------------------------------------------
class Common(BaseModel):
    """
    main class
    """
    id: int

    class Config:
        orm_mode = True


# -------------------------------------------------------------------------------------------------
class NotesList(Common):
    """
    class for list method
    """
    name: str
    status: int | None
    is_public: bool = Field(default=False)
    is_important: bool = Field(default=False)


# -------------------------------------------------------------------------------------------------
class CreateNotes(BaseModel):
    """
    class for create method
    """
    name: str
    status: int
    is_public: bool = Field(default=False)
    is_important: bool = Field(default=False)


# -------------------------------------------------------------------------------------------------
class PutNotes(BaseModel):
    """
    class for put method
    """
    status: int | None = None
    is_public: bool = Field(default=False)
    is_important: bool = Field(default=False)

    class Config:
        orm_mode = True
