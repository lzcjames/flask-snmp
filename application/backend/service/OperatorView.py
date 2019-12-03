from ...models import Event
from ...models import Record
import jsonpickle

class OperatorView:
    #def getText():
        # get result in format Text
    #def getGraphic():
        # get result in format graphic
    #def getConf():
        # get result in format JSON
    def getLogEvent():
        events = Event.query.all()
        return (jsonpickle.encode(events))
    
    def getLogRecord():
        records = Record.query.all()
        return (jsonpickle.encode(records))


    