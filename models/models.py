from sqlalchemy import BigInteger,String,ForeignKey,Integer
from sqlalchemy.orm import (relationship,Mapped,
                            mapped_column,DeclarativeBase)
from sqlalchemy.ext.asyncio import (AsyncSession,AsyncAttrs,
                                    async_sessionmaker,create_async_engine)


engine = create_async_engine('sqlite+aiosqlite:///test.db')
async_session_maker = async_sessionmaker(engine)
 
class Base(DeclarativeBase,AsyncAttrs):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    telegram_id:Mapped[int] = mapped_column(BigInteger)
    name:Mapped[str] = mapped_column(String(50))
    adress:Mapped[str] = mapped_column(String(50))
    phone:Mapped[int] = mapped_column(BigInteger)
    orders:Mapped[str] = mapped_column(String)
    def __repr__(self):
        return f'User(id={self.id}, name={self.name}'
    





