from datetime import date
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask import abort
import sys

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'
db = SQLAlchemy(app)


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()

parser_post = reqparse.RequestParser()
parser_get = reqparse.RequestParser()

parser_post.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)

parser_post.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)

parser_get.add_argument(
    'start_time',
    type=str
)

parser_get.add_argument(
    'end_time',
    type=str
)


class EventDao(object):
    def __init__(self, id, date, event):
        self.id = id
        self.date = date
        self.event = event


resource_fields = {
    'id': fields.Integer,
    'date': fields.DateTime(dt_format='iso8601'),
    'event': fields.String
}

# class HelloWorldResource(Resource):
#     def get(self):
#         return {"message": "Hello from the REST API!"}
#
#     def post(self):
#         args_get = parser_post.parse_args()
#         return args_get['name']
#
#
# class TodayTask(Resource):
#     def get(self):
#         return {"data": "There are no events for today!"}
#
#
# api.add_resource(HelloWorldResource, '/hello')
# api.add_resource(TodayTask, '/event/today')


class Events(Resource):
    def post(self):
        args = parser_post.parse_args(strict=True)
        if args.get('message'):
            return args['message']
        else:
            event = Event(event=args['event'], date=args['date'])
            db.session.add(event)
            db.session.commit()
            args['message'] = "The event has been added!"
            event_date = args['date'].strftime('%Y-%m-%d')
            return {
                "message": args['message'],
                "event": args['event'],
                "date": event_date
            }

    @marshal_with(resource_fields)
    def get(self):
        args = parser_get.parse_args(strict=True)
        if not (args['start_time'] or args['end_time']):
            data = Event.query.all()
        else:
            start_time = date.fromisoformat(args['start_time'])
            end_time = date.fromisoformat(args['end_time'])
            data = Event.query.filter(Event.date.between(start_time, end_time)).all()
        output = [
            EventDao(id=event.id,
                     event=event.event,
                     date=event.date)
            for event in data
        ]
        return output


class Today(Resource):
    @marshal_with(resource_fields)
    def get(self):
        data = Event.query.filter(Event.date == date.today()).all()
        output = [
            EventDao(id=event.id,
                     event=event.event,
                     date=event.date)
            for event in data
        ]
        return output


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if not event:
            abort(404, "The event doesn't exist!")
        return EventDao(id=event.id, event=event.event, date=event.date), 200  # TODO: should return code 200 also

    def delete(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if not event:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return jsonify({"message": "The event has been deleted!"})


api.add_resource(Events, '/event')
api.add_resource(Today, '/event/today')
api.add_resource(EventByID, '/event/<int:event_id>')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run(debug=True)
