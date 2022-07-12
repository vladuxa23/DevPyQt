from sqlalchemy import Boolean, Column, Integer, String


from .database import Base

# -------------------------------------------------------------------------------------------------
class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(Integer, default=1)
    is_public = Column(Boolean, default=True)
    is_important = Column(Boolean, default=True)

