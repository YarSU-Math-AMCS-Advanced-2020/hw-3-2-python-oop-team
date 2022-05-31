import easygui
from front_controller import FrontController
from request import Request

front_controller = FrontController()

fin = easygui.buttonbox(msg='', choices=('Отели', 'Авиа', 'Ж/Д','Туры'), image='index.jpg', title="Авиослейвс ПутешествиЯ")
while True:
    info = []
    if fin == 'Отели':
        fin = easygui.enterbox(msg="Пожалуйста, введите куда вы хотите поехать", image="Giga_hotel.jpg", title="Ок")
        plane_dict = {'city': fin}
        request = Request('find_hotels', plane_dict)
        filter_list = front_controller.handle(request)
        for item in range(len(filter_list)):
            string ='Название ' + filter_list[item]['title'] + '   Страна ' + filter_list[item]['location']['country'] + '   Город ' + filter_list[item]['location']['city']
            string = string.ljust(200) + filter_list[item]['id'].rjust(30)
            info.append(string)
        out = easygui.multchoicebox(msg="пожалуйста, умоляю, выбери билеты:", title="", choices=info)
        print(out[0].split()[-1])
        plane_dict = {'id': out[0].split()[-1]}
        request = Request('buy_hotel', plane_dict)
