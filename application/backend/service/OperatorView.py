from ...models import Event
import jsonpickle

class OperatorView:
    #def getText():
        # get result in format Text
    #def getGraphic():
        # get result in format graphic
    #def getConf():
        # get result in format JSON
    def getLog():
        events = Event.query.all()
        return (jsonpickle.encode(events))

    