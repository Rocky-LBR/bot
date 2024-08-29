from datetime import datetime
from flask import request
from flask_restful import Resource
from resources import api



class RegisterServerResource(Resource):
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
                # SendMessageService.insert_send_message(id=id,send_msg=send_msg,ip=ip,phone=phone)
                return {"code":200,"msg":"success"}
            else:
                return {'error': "Please provide correct info "}
        except Exception as e:
            return {'error': e}, 400

api.add_resource(RegisterServerResource,'/RegisterServerResource')