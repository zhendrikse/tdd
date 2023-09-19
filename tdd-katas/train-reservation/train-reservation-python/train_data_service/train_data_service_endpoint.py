"""
This module exposes a TrainDataService on http using Cherrypy
"""
import json
import cherrypy

def start(trains_data):
    from train_data_service import TrainDataService
    TrainDataService.data_for_train.exposed = True
    TrainDataService.reserve.exposed = True
    TrainDataService.reset.exposed = True
    cherrypy.config.update({"server.socket_port" : 8081})
    cherrypy.quickstart(TrainDataService(trains_data))

def main(args):
    if args:
        trains_data_file = args[0]
    else:
        trains_data_file = "trains.json"
    with open(trains_data_file) as f:
        trains_data = f.read()
    start(trains_data)
        

if __name__ == '__main__':
        import sys
        help_text = """ 
    Use this program to start a train data service:

        python train_data_service.py

    It will start a service on:

        http://localhost:8081/data_for_train

    You can pass on the command line the name of the json file to use as a data source. 
    It defaults to looking for "trains.json" in the current working directory.

        python {0} trains.json
        """.format(sys.argv[0])
        if "-help" in sys.argv or "--help" in sys.argv or "-h" in sys.argv:
            print(help_text)
        else:
            main(sys.argv[1:])