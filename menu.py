import easygui
from front_controller import FrontController
from request import Request

front_controller = FrontController()
client_id = '1'

fin = easygui.buttonbox(msg='', choices=('Отели', 'Авиа', 'Ж/Д','Туры'), image='index.jpg', title="Авиослейвс ПутешествиЯ")
while True:
    info = []
    if fin == 'Отели':
        fin = easygui.enterbox(msg="Пожалуйста, введите куда вы хотите поехать", image="Giga_hotel.jpg", title="Ок")
        plane_dict = {'city': fin}
        request = Request('find_hotels', plane_dict)
        filter_list = front_controller.handle(request)
        map_id = dict()
        for item in range(len(filter_list)):
            string ='Название ' + filter_list[item]['title'] + '   Страна ' + filter_list[item]['location']['country'] + '   Город ' + filter_list[item]['location']['city']
            map_id[string] = filter_list[item]['id']
            info.append(string)
        out = easygui.multchoicebox(msg="пожалуйста, умоляю, выбери билеты:", title="", choices=info)
        request = Request('buy_hotel', {'id': map_id[out[0]], 'client_id': client_id})
        resp = front_controller.handle(request)
        print(resp)
        exit()
