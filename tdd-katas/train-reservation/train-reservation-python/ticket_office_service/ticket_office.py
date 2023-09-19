import urllib.request
import json
import urllib.request
import json

class TicketOffice:

    def cancel_reservation(self, train_id, booking_reference):
        url = "http://127.0.0.1:8081"
        form_data = {"train_id": train_id, "booking_reference": booking_reference}
        data = urllib.parse.urlencode(form_data)
        req = urllib.request.Request(url + "/cancel", bytes(data, encoding="ISO-8859-1"))
        return json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
    

    def reserve(self, train_id, seat_count):
        # TODO: write this code!
        pass

if __name__ == "__main__":
    """Deploy this class as a web service using CherryPy"""
    import cherrypy
    TicketOffice.reserve.exposed = True
    cherrypy.config.update({"server.socket_port" : 8083})
    cherrypy.quickstart(TicketOffice())