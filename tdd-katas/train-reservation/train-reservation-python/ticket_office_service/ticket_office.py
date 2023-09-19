import urllib.request
import json

class TicketOffice:

    def cancel_reservation(self, train_id, booking_reference):
        url = "http://127.0.0.1:8081"
        urllib.request.urlopen(url + "/reset/" + train_id)


    def reserve(self, train_id, seat_count):
        # TODO: write this code!
        pass

if __name__ == "__main__":
    """Deploy this class as a web service using CherryPy"""
    import cherrypy
    TicketOffice.reserve.exposed = True
    cherrypy.config.update({"server.socket_port" : 8083})
    cherrypy.quickstart(TicketOffice())