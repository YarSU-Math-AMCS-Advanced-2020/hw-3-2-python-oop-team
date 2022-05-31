from front_controller import FrontController
from request import Request

if __name__ == '__main__':
    hotel_dict = {'from': 'Москва'}
    front_controller = FrontController()
    request = Request('find_train_tickets', hotel_dict)
    res = front_controller.handle(request)
    print(res)
    # plane_dict = {'id': 'pt-5e1f45b8'}
    # request = Request('buy_plane_ticket', plane_dict)
    # front_controller = FrontController()
    # res = front_controller.handle(request)

    # hotel_dict = {'id': 'h-aa84dc1e'}
    # request = Request('buy_hotel', hotel_dict)
    # front_controller = FrontController()
    # res = front_controller.handle(request)

    # train_dict = {'id': 'tt-e5f5f274'}
    # request = Request('buy_train_ticket', train_dict)
    # front_controller = FrontController()
    # res = front_controller.handle(request)

    # dict = {'id': 'tt-e5f5f274', 'client_id': }
    # request = Request('return_client_purchases')
