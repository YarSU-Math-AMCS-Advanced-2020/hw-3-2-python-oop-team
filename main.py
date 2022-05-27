from front_controller import FrontController
from request import Request


if __name__ == '__main__':
    ticket_dict = {'to': 'Москва'}
    #hotel_dict = {'city': 'Kyiv', 'price': (123, 4123)}
    #request = Request('find_plane_tickets', ticket_dict)

    hotel_dict = {'id': 'h-aa84dc1e'}
    request = Request('buy_hotel', hotel_dict)
    front_controller = FrontController()
    res = front_controller.handle(request)
