from sqlalchemy import Select, asc

from moders.send_message import SendMessage
from resources import db

class SendMessageService:
    def get_message(self,send_msg:str,ip:str,phone:str):
        query = Select(SendMessage).where(SendMessage.ip ==ip and SendMessage.send_msg==send_msg and SendMessage.phone==phone)
        return db.session.scalars(query).all()

    def insert_send_message(self,id,send_msg,ip,phone):
        #判断是否重复插入（send_msg和ip、phone是否一致，一致则不进行插入）
        exist_message = self.get_message(send_msg,ip,phone)
        if not exist_message:
            #完成数据插入操作
            return {"msg":"success","code":True}
        else:
            return {"msg":'fail,the message has been recorded already',"code":False}


