from datetime import datetime

from flask import request
from flask_restful import Resource

from resources import api
from services.send_message_service import SendMessageService


class CloudServerResource(Resource):
    def post(self):
        try:
            request_json = request.json
            if request_json:
                id = request_json.get('id', None)
                send_msg = request_json.get('send_msg', None)
                ip = request_json.get('ip', None)
                phone = request_json.get(',phone', None)
                time = datetime.fromisoformat(request_json.get('time', None))
                #数据库操作把数据按照ip、data、time、msgcode写入数据库
                SendMessageService.insert_send_message(id=id,send_msg=send_msg,ip=ip,phone=phone)
                return {"code":200,"msg":"success"}
            else:
                return {'error': "Please provide correct info "}
        except Exception as e:
            return {'error': e}, 400

class CloudServerPictureResource(Resource):
    def post(self):
        try:
            request_json = request.json
            file_path ="path"
            file = request.files['file']
            file.save(file_path)
            id = request_json.get('id', None)
            ip = request_json.get('ip', None)
            phone = request_json.get(',phone', None)
            time = datetime.fromisoformat(request_json.get('time', None))
            SendMessageService.insert_send_message(id=id,send_msg=file_path,ip=ip,phone=phone)
            return {'code': 200, "msg": "success"}
        except Exception as e:
            return {'code': 400, "msg": "failed"}

api.add_resource(CloudServerResource,'/CloudServerResource')
api.add_resource(CloudServerPictureResource,'/CloudServerPictureResource')
