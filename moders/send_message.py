from datetime import datetime

from sqlalchemy import String, Integer, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from resources import db


class SendMessage(db.Model):
    __tablename="sendmessage"
    id:Mapped[int] = mapped_column(Integer,primary_key=True)
    ip:Mapped[str] = mapped_column(String(255),nullable=False)
    send_msg:Mapped[str] = mapped_column(String(255),nullable=False)
    phone: Mapped[str] = mapped_column(String(255), nullable=False)
    nickname: Mapped[str] = mapped_column(String(255), nullable=False)
    msg_code: Mapped[str] = mapped_column(String(255), nullable=False)
    time:Mapped[datetime]=mapped_column(TIMESTAMP,nullable=False)

    def serilize(self):
        return {
            'id':self.id,
            'ip':self.ip,
            'send_msg':self.send_msg,
            'phone':self.phone,
            'nickname':self.nickname,
            'msg_code':self.msg_code,
            'time':self.time
        }