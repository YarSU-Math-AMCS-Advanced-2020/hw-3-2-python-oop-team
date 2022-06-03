import easygui
from front_controller import FrontController
from request import Request
from client import Client
from uuid import uuid4

front_controller = FrontController()
client_id = '1'

while True != False:
    fin = easygui.buttonbox(msg='', choices=('Отели', 'Авиа', 'Ж/Д', 'Туры', 'Корзина', 'Exit'),
                            image=r'pictures/index.jpg',
                            title="Авиослейвс ПутешествиЯ")

    info = []
    if fin == 'Exit':
        exit()
    if fin == 'Корзина':
        request = Request('find_purchases', {'client_id': client_id})
        list_purchases = front_controller.handle(request).data
        for item in list_purchases:
            print(item.info())
        print(list_purchases)

    if fin == 'Отели':
        request = Request('get_cities_with_hotel', {})
        list_cities_with_hotel = front_controller.handle(request).data
        city = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                 choices=list_cities_with_hotel)
        if city != None:
            plane_dict = {'city': city}
            request = Request('find_hotels', plane_dict)
            filtered_list = front_controller.handle(request).data
            map_id = dict()
            for item in filtered_list:
                string = 'Name ' + item['title'] + '   Countre ' + item['location']['country'] + '   Cite ' + \
                         item['location']['city']
                map_id[string] = item['id']
                info.append(string)
            out = easygui.choicebox(msg="пожалуйста, умоляю, выбери билеты:", title="Авиослейвс ПутешествиЯ",
                                    choices=info)
            if out != None:
                amount = easygui.enterbox(msg="Введите количество людей", image=r'pictures/family.jpg',
                                          title="Авиослейвс ПутешествиЯ")
                if amount != None:
                    time = easygui.multenterbox('', title="Авиослейвс ПутешествиЯ",
                                                fields=['Дата заезда', 'Дата выезда'])
                    if time != None:
                        request = Request('buy_hotel',
                                          {'id': map_id[out], 'client_id': client_id, 'check_in': time[0],
                                           'check_out': time[1],
                                           'people_count': int(amount)})
                        front_controller.handle(request)
        # request = Request('find_purchases', {'client_id': client_id})
        # front_controller.handle(request)
        # for pur in purchased_hotel:
        #    print(pur.get_title())
        # print(purchased_hotel.get_title())

    if fin == 'Авиа':
        request = Request('get_plane_departure_cities', {})
        list_departure_cities = front_controller.handle(request).data
        departure_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                             choices=list_departure_cities)
        if departure_cities != None:
            request = Request('get_plane_arrival_by_departure_cities', {'from': departure_cities})
            list_arrival_cities = front_controller.handle(request).data
            if len(list_arrival_cities) != 1:
                arrival_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                                   choices=list_arrival_cities)
            else:
                pup = easygui.buttonbox(msg=f'Для выбора доступен только один город: {list_arrival_cities[0]}',
                                        choices=('Я хочу полететь в этот город', 'Я не хочу лететь в этот город'),
                                        image="Изображение WeChat 2.jpg", title='Авиослейвс ПутешествиЯ')
                if pup == 'Я хочу полететь в этот город':
                    arrival_cities = list_arrival_cities[0]
                else:
                    arrival_cities = None
            if arrival_cities != None:
                list_info_plane_tickets = ['Дата отправления', 'Дата прибытия']
                fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_plane_tickets))
                if fin != None:
                    plane_dict = {'from': departure_cities, 'to': arrival_cities, 'departure_date': fin[0],
                                  'arrival_date': fin[1]}
                    request = Request('find_plane_tickets', plane_dict)
                    filter_list = front_controller.handle(request).data
                    map_id = dict()
                    for item in filter_list:
                        string = 'Время отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                            'arrival_time'] + "   Цена:" + str(item['price'])
                        map_id[string] = item['id']
                        info.append(string)
                    out = easygui.choicebox(
                        msg='Откуда:' + departure_cities + '\nКуда:' + arrival_cities + '\nДата отправления:' + fin[
                            0] + '\nДата прибытия: ' + fin[1],
                        title="Авиослейвс ПутешествиЯ", choices=info)
                    if out != None:
                        seat = easygui.enterbox(msg="Введите место(от 1 до 69)", image=r'pictures/hand.jpg',
                                                title="Авиослейвс ПутешествиЯ")
                        if seat != None:
                            request = Request('buy_plane_ticket',
                                              {'id': map_id[out], 'client_id': client_id, 'seat': seat})
                            front_controller.handle(request)

    if fin == 'Ж/Д':
        request = Request('get_train_departure_cities', {})
        list_departure_cities = front_controller.handle(request).data
        departure_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                             choices=list_departure_cities)
        if departure_cities != None:
            request = Request('get_train_arrival_by_departure_cities', {'from': departure_cities})
            list_arrival_cities = front_controller.handle(request).data
            if len(list_arrival_cities) != 1:
                arrival_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                                   choices=list_arrival_cities)
            else:
                pup = easygui.buttonbox(msg=f'Для выбора доступен только один город: {list_arrival_cities[0]}',
                                        choices=('Я хочу поехать в этот город', 'Я не хочу ехать в этот город'),
                                        image="Изображение WeChat 2.jpg", title='Авиослейвс ПутешествиЯ')
                if pup == 'Я хочу поехать в этот город':
                    arrival_cities = list_arrival_cities[0]
                else:
                    arrival_cities = None
            if arrival_cities != None:
                list_info_train_tickets = ['Дата отправления', 'Дата прибытия']
                fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_train_tickets))
                plane_dict = {'from': departure_cities, 'to': arrival_cities, 'departure_date': fin[0],
                              'arrival_date': fin[1]}
                if fin != None:
                    request = Request('find_train_tickets', plane_dict)
                    filter_list = front_controller.handle(request).data
                    map_id = dict()
                    for item in filter_list:
                        string = 'Вермя отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                            'arrival_time'] + "   Цена:" + str(item['price'])
                        map_id[string] = item['id']
                        info.append(string)
                    out = easygui.choicebox(
                        msg='Откуда:' + departure_cities + '\nКуда:' + arrival_cities + '\nДата отправления:' + fin[
                            0] + '\nДата прибытия: ' + fin[1],
                        title="Авиослейвс ПутешествиЯ", choices=info)
                    if out != None:
                        carriage = easygui.enterbox(msg="Введите место(от 1 до 8)", image=r'pictures/carriage.jpg',
                                                    title="Авиослейвс ПутешествиЯ")
                        if carriage != None:
                            seat = easygui.enterbox(msg="Введите место(от 1 до 28)", image=r'pictures/seat.jpg',
                                                    title="Авиослейвс ПутешествиЯ")
                            if seat != None:
                                request = Request('buy_train_ticket',
                                                  {'id': map_id[out], 'client_id': client_id, 'seat': seat, 'carriage': carriage})
                                front_controller.handle(request)

    if fin == 'Туры':
        tour_id = f't-{str(uuid4()).split("-")[0]}'
        while True:
            info.clear()
            choice = easygui.buttonbox(msg='Что вы хотите добавить?',
                                       choices=('Отели', 'Авиа', 'Ж/Д', 'Оформить тур'),
                                       image=r'pictures/tour.png',
                                       title="Авиослейвс ПутешествиЯ")
            if choice == 'Отели':
                request = Request('get_cities_with_hotel', {})
                list_cities_with_hotel = front_controller.handle(request).data
                city = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                         choices=list_cities_with_hotel)
                if city != None:
                    plane_dict = {'city': city}
                    request = Request('find_hotels', plane_dict)
                    filtered_list = front_controller.handle(request).data
                    map_id = dict()
                    for item in filtered_list:
                        string = 'Name ' + item['title'] + '   Countre ' + item['location']['country'] + '   Cite ' + \
                                 item['location']['city']
                        map_id[string] = item['id']
                        info.append(string)
                    out = easygui.choicebox(msg="пожалуйста, умоляю, выбери билеты:", title="Авиослейвс ПутешествиЯ",
                                            choices=info)
                    if out != None:
                        amount = easygui.enterbox(msg="Введите количество людей", image=r'pictures/family.jpg',
                                                  title="Авиослейвс ПутешествиЯ")
                        if amount != None:
                            time = easygui.multenterbox('', title="Авиослейвс ПутешествиЯ",
                                                        fields=['Дата заезда', 'Дата выезда'])
                            if time != None:
                                request = Request('add_hotel_to_tour',
                                                  {'tour_id': tour_id, 'id': map_id[out], 'check_in': time[0],
                                                   'check_out': time[1], 'people_count': int(amount)})
                                front_controller.handle(request)

            if choice == 'Авиа':
                request = Request('get_plane_departure_cities', {})
                list_departure_cities = front_controller.handle(request).data
                departure_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                                     choices=list_departure_cities)
                if departure_cities != None:
                    request = Request('get_plane_arrival_by_departure_cities', {'from': departure_cities})
                    list_arrival_cities = front_controller.handle(request).data
                    if len(list_arrival_cities) != 1:
                        arrival_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                                           choices=list_arrival_cities)
                    else:
                        pup = easygui.buttonbox(msg=f'Для выбора доступен только один город: {list_arrival_cities[0]}',
                                                choices=(
                                                'Я хочу полететь в этот город', 'Я не хочу лететь в этот город'),
                                                image="Изображение WeChat 2.jpg", title='Авиослейвс ПутешествиЯ')
                        if pup == 'Я хочу полететь в этот город':
                            arrival_cities = list_arrival_cities[0]
                        else:
                            arrival_cities = None
                    if arrival_cities != None:
                        list_info_plane_tickets = ['Дата отправления', 'Дата прибытия']
                        fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_plane_tickets))
                        if fin != None:
                            plane_dict = {'from': departure_cities, 'to': arrival_cities, 'departure_date': fin[0],
                                          'arrival_date': fin[1]}
                            request = Request('find_plane_tickets', plane_dict)
                            filter_list = front_controller.handle(request).data
                            map_id = dict()
                            for item in filter_list:
                                string = 'Время отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                                    'arrival_time'] + "   Цена:" + str(item['price'])
                                map_id[string] = item['id']
                                info.append(string)
                            out = easygui.choicebox(
                                msg='Откуда:' + departure_cities + '\nКуда:' + arrival_cities + '\nДата отправления:' +
                                    fin[
                                        0] + '\nДата прибытия: ' + fin[1],
                                title="Авиослейвс ПутешествиЯ", choices=info)
                            if out != None:
                                seat = easygui.enterbox(msg="Введите место(от 1 до 69)", image=r'pictures/hand.jpg',
                                                        title="Авиослейвс ПутешествиЯ")
                                if seat != None:
                                    request = Request('add_plane_ticket_to_tour',
                                                      {'tour_id': tour_id, 'id': map_id[out], 'seat': seat})
                                    front_controller.handle(request)

            if fin == 'Ж/Д':
                request = Request('get_train_departure_cities', {})
                list_departure_cities = front_controller.handle(request).data
                departure_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                                     choices=list_departure_cities)
                if departure_cities != None:
                    request = Request('get_train_arrival_by_departure_cities', {'from': departure_cities})
                    list_arrival_cities = front_controller.handle(request).data
                    if len(list_arrival_cities) != 1:
                        arrival_cities = easygui.choicebox(msg='Выберите город:', title="Авиослейвс ПутешествиЯ",
                                                           choices=list_arrival_cities)
                    else:
                        pup = easygui.buttonbox(msg=f'Для выбора доступен только один город: {list_arrival_cities[0]}',
                                                choices=('Я хочу поехать в этот город', 'Я не хочу ехать в этот город'),
                                                image="Изображение WeChat 2.jpg", title='Авиослейвс ПутешествиЯ')
                        if pup == 'Я хочу поехать в этот город':
                            arrival_cities = list_arrival_cities[0]
                        else:
                            arrival_cities = None
                    if arrival_cities != None:
                        list_info_train_tickets = ['Дата отправления', 'Дата прибытия']
                        fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_train_tickets))
                        plane_dict = {'from': departure_cities, 'to': arrival_cities, 'departure_date': fin[0],
                                      'arrival_date': fin[1]}
                        if fin != None:
                            request = Request('find_train_tickets', plane_dict)
                            filter_list = front_controller.handle(request).data
                            map_id = dict()
                            for item in filter_list:
                                string = 'Вермя отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                                    'arrival_time'] + "   Цена:" + str(item['price'])
                                map_id[string] = item['id']
                                info.append(string)
                            out = easygui.choicebox(
                                msg='Откуда:' + departure_cities + '\nКуда:' + arrival_cities + '\nДата отправления:' +
                                    fin[
                                        0] + '\nДата прибытия: ' + fin[1],
                                title="Авиослейвс ПутешествиЯ", choices=info)
                            if out != None:
                                carriage = easygui.enterbox(msg="Введите место(от 1 до 8)",
                                                            image=r'pictures/carriage.jpg',
                                                            title="Авиослейвс ПутешествиЯ")
                                if carriage != None:
                                    seat = easygui.enterbox(msg="Введите место(от 1 до 28)", image=r'pictures/seat.jpg',
                                                            title="Авиослейвс ПутешествиЯ")
                                    if seat != None:
                                        request = Request('add_train_ticket_to_tour',
                                                          {'tour_id': tour_id, 'id': map_id[out], 'seat': seat, 'carriage': carriage})
                                        front_controller.handle(request)

            if choice == 'Оформить тур':
                request = Request('buy_tour', {'tour_id': tour_id, 'client_id': client_id})
                front_controller.handle(request)
                # request = Request('find_purchases', {'client_id': client_id})
                # print(front_controller.handle(request))
                break
