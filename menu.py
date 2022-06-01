import easygui
from front_controller import FrontController
from request import Request

front_controller = FrontController()
client_id = '1'

fin = easygui.buttonbox(msg='', choices=('Отели', 'Авиа', 'Ж/Д', 'Туры'), image=r'pictures/index.jpg',
                        title="Авиослейвс ПутешествиЯ")
while True:
    info = []
    if fin == 'Отели':
        fin = easygui.enterbox(msg="Пожалуйста, введите куда вы хотите поехать", image=r'pictures/Giga_hotel.jpg',
                               title="Авиослейвс ПутешествиЯ")
        plane_dict = {'city': fin}
        request = Request('find_hotels', plane_dict)
        filtered_list = front_controller.handle(request).data
        map_id = dict()
        for item in filtered_list:
            string = 'Название ' + item['title'] + '   Страна ' + item['location']['country'] + '   Город ' + \
                     item['location']['city']
            map_id[string] = item['id']
            info.append(string)
        out = easygui.multchoicebox(msg="пожалуйста, умоляю, выбери билеты:", title="Авиослейвс ПутешествиЯ",
                                    choices=info)
        request = Request('buy_hotel', {'id': map_id[out[0]], 'client_id': client_id})
        amount = easygui.enterbox(msg="Введите количество людей", image=r'pictures/family.jpg',
                                  title="Авиослейвс ПутешествиЯ")

    if fin == 'Авиа':
        list_info_plane_tickets = ['Откуда', 'Куда', 'Дата отбытия', 'Дата прибытия']
        fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_plane_tickets))
        plane_dict = {'from': fin[0], 'to': fin[1], 'departure_date': fin[2], 'arrival_date': fin[3]}
        request = Request('find_plane_tickets', plane_dict)
        filter_list = front_controller.handle(request).data
        map_id = dict()
        print(filter_list)
        for item in filter_list:
            string = 'Вермя отбытия:' + item['departure_time'] + '  Время прибытия:' + item['arrival_time'] +"   Цена:"+ str(item['price'])
            map_id[string] = item['id']
            info.append(string)
        out = easygui.multchoicebox(
            msg='Откуда:' + fin[0] + '\nКуда:' + fin[1] + '\nДата отбытия:' + fin[2] + '\nДата прибытия: ' + fin[3],
            title="Авиослейвс ПутешествиЯ", choices=info)

    if fin == 'Ж/Д':
        list_info_train_tickets = ['Откуда', 'Куда', 'Дата отбытия', 'Дата прибытия']
        fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_train_tickets))
        plane_dict = {'from': fin[0], 'to': fin[1], 'departure_date': fin[2], 'arrival_date': fin[3]}
        request = Request('find_train_tickets', plane_dict)
        filter_list = front_controller.handle(request).data
        map_id = dict()
        print(filter_list)
        for item in filter_list:
            string = 'Вермя отбытия:' + item['departure_time'] + '  Время прибытия:' + item['arrival_time'] +"   Цена:"+ str(item['price'])
            map_id[string] = item['id']
            info.append(string)
        out = easygui.multchoicebox(
            msg='Откуда:' + fin[0] + '\nКуда:' + fin[1] + '\nДата отбытия:' + fin[2] + '\nДата прибытия: ' + fin[3],
            title="Авиослейвс ПутешествиЯ", choices=info)

    exit()