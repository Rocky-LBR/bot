from datetime import datetime

from flask import request
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from moders.book_model import BookModel
from resources import api, docs
from services.book_service import BookService

class BookRequestSchema(Schema):
    name =fields.String(required=True)
    author = fields.String(required=True)
    publish_time = fields.DateTime(required=True)


class BookResource(MethodResource,Resource):
    @doc(description='Get a books information')
    def get(self,book_id:int):
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            return {'id':book_id,"author":'Jack',"publish_time":"1992"}
    def put(self,book_id:int):
        try:
            request_json =request.json
            if request_json:
                name = request_json.get('name',None)
                author = request_json.get('author',None)
                publish_time_str = request_json.get('publish_time',None)
                publish_time = datetime.fromisoformat(publish_time_str) if publish_time_str else None

                book_model = BookModel(name=name,author=author,publish_time=publish_time)
                book_model = BookService.updatae_book(book_model)

                return book_model.serilize()
            else:
                return {'error':"Please provide book info "}
        except Exception as e:
            return {'error':e},400



class BooListResource(Resource):
    def get(self):
        book_list = BookService.get_all_books()
        return [book_model.serilize() for book_model in book_list]
    def post(self):

        try:
            request_json =request.json
            if request_json:
                name = request_json.get('name',None)
                author = request_json.get('author',None)
                publish_time = datetime.fromisoformat(request_json.get('publish_time',None))

                book_model = BookModel(name=name,author=author,publish_time=publish_time)
                BookService.create_book(book_model)

                return book_model.serilize()
            else:
                return {'error':"Please provide book info "}
        except Exception as e:
            return {'error':e},400


api.add_resource(BookResource,'/books/<int:book_id>')
api.add_resource(BooListResource,'/books')
docs.register(BookResource)

@app.route('/swagger.yaml',methods=['GET'])
def gen_swagger_yaml():
    yaml_spec = docs.spec.to_yaml()
    return Response(yaml_spec,mimetypes='text/yaml')
