import request as rq
from command import AbstractCommand, FindHotelCommand, FindTrainTicketCommand, FindPlaneTicketCommand
from typing import Dict, Type
from search_manager import SearchManager


class FrontController:
    def __init__(self):
        self.map: Dict[str, Type[AbstractCommand]] = {'find_hotels': FindHotelCommand,
                                                      'find_train_tickets': FindTrainTicketCommand,
                                                      'find_plane_tickets': FindPlaneTicketCommand}
        self.search_manager = SearchManager()

    def handle(self, request: rq.Request) -> list | dict | None:
        if self.map.get(request.command):
            return self.map[request.command](request, self).execute()
