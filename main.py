from front_controller import FrontController
from request import Request


if __name__ == '__main__':
    ticket_dict ={'to': 'Москва'}
    hotel_dict = {'city': 'Kyiv', 'price': (123, 4123)}
    request = Request('find_hotels', hotel_dict)
    front_controller = FrontController()
    res = front_controller.handle(request)
    print(res)
