import easygui
from front_controller import FrontController
from request import Request
from client import Client
from uuid import uuid4

front_controller = FrontController()
client_id = '1'

while True != False:
    fin = easygui.buttonbox(msg='', choices=('Отели', 'Авиа', 'Ж/Д', 'Туры', 'Корзина', 'Exit'), image=r'pictures/index.jpg',
                            title="Авиослейвс ПутешествиЯ")

    info = []
    if fin == 'Exit':
        exit()

    # if fin == 'Корзина':
    #
    #     easygui.choicebox(msg="пожалуйста, выбери:", title="", choices=m)


    if fin == 'Отели':
        fin = easygui.enterbox(msg="Пожалуйста, введите куда вы хотите поехать", image=r'pictures/Giga_hotel.jpg',
                               title="Авиослейвс ПутешествиЯ")
        plane_dict = {'city': fin}
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
        amount = easygui.enterbox(msg="Введите количество людей", image=r'pictures/family.jpg',
                                  title="Авиослейвс ПутешествиЯ")
        time = easygui.multenterbox('', title="Авиослейвс ПутешествиЯ", fields=['Дата заезда', 'Дата выезда'])
        request = Request('buy_hotel',
                          {'id': map_id[out], 'client_id': client_id, 'check_in': time[0], 'check_out': time[1],
                           'people_count': int(amount)})
        front_controller.handle(request)
        # request = Request('find_purchases', {'client_id': client_id})
        # front_controller.handle(request)
        # for pur in purchased_hotel:
        #    print(pur.get_title())
        # print(purchased_hotel.get_title())

    if fin == 'Авиа':
        list_info_plane_tickets = ['Откуда', 'Куда', 'Дата отправления', 'Дата прибытия']
        fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_plane_tickets))
        plane_dict = {'from': fin[0], 'to': fin[1], 'departure_date': fin[2], 'arrival_date': fin[3]}
        request = Request('find_plane_tickets', plane_dict)
        filter_list = front_controller.handle(request).data
        map_id = dict()
        for item in filter_list:
            string = 'Время отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                'arrival_time'] + "   Цена:" + str(item['price'])
            map_id[string] = item['id']
            info.append(string)
        out = easygui.choicebox(
            msg='Откуда:' + fin[0] + '\nКуда:' + fin[1] + '\nДата отправления:' + fin[2] + '\nДата прибытия: ' + fin[3],
            title="Авиослейвс ПутешествиЯ", choices=info)
        seat = easygui.enterbox(msg="Введите место(от 1 до 69)", image=r'pictures/hand.jpg',
                                title="Авиослейвс ПутешествиЯ")
        request = Request('buy_hotel',
                          {'id': map_id[out], 'client_id': client_id, 'seat': seat})
        front_controller.handle(request)

    if fin == 'Ж/Д':
        list_info_train_tickets = ['Откуда', 'Куда', 'Дата отправления', 'Дата прибытия']
        fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_train_tickets))
        plane_dict = {'from': fin[0], 'to': fin[1], 'departure_date': fin[2], 'arrival_date': fin[3]}
        request = Request('find_train_tickets', plane_dict)
        filter_list = front_controller.handle(request).data
        map_id = dict()
        for item in filter_list:
            string = 'Вермя отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                'arrival_time'] + "   Цена:" + str(item['price'])
            map_id[string] = item['id']
            info.append(string)
        out = easygui.choicebox(
            msg='Откуда:' + fin[0] + '\nКуда:' + fin[1] + '\nДата отправления:' + fin[2] + '\nДата прибытия: ' + fin[3],
            title="Авиослейвс ПутешествиЯ", choices=info)
        carriage = easygui.enterbox(msg="Введите место(от 1 до 8)", image=r'pictures/carriage.jpg',
                                    title="Авиослейвс ПутешествиЯ")
        seat = easygui.enterbox(msg="Введите место(от 1 до 28)", image=r'pictures/seat.jpg',
                                title="Авиослейвс ПутешествиЯ")
        request = Request('buy_hotel',
                          {'id': map_id[out], 'client_id': client_id, 'seat': seat, 'carriage': carriage})
        front_controller.handle(request)

    if fin == 'Туры':
        tour_id = f't-{str(uuid4()).split("-")[0]}'
        while True:
            choise = easygui.buttonbox(msg='Что вы хотите добавить?',
                                       choices=('Отели', 'Авиа', 'Ж/Д', 'Оформить тур'),
                                       image=r'pictures/tour.png',
                                       title="Авиослейвс ПутешествиЯ")
            if choise == 'Отели':
                hotel = easygui.enterbox(msg="Пожалуйста, введите куда вы хотите поехать",
                                         image=r'pictures/Giga_hotel.jpg',
                                         title="Авиослейвс ПутешествиЯ")
                plane_dict = {'city': hotel}
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
                amount = easygui.enterbox(msg="Введите количество людей", image=r'pictures/family.jpg',
                                          title="Авиослейвс ПутешествиЯ")
                time = easygui.multenterbox('', title="Авиослейвс ПутешествиЯ",
                                            fields=['Дата заезда', 'Дата выезда'])
                request = Request('add_hotel_to_tour',
                                  {'tour_id': tour_id, 'id': map_id[out], 'check_in': time[0],
                                   'check_out': time[1], 'people_count': int(amount)})
                front_controller.handle(request)

            if choise == 'Авиа':
                list_info_plane_tickets = ['Откуда', 'Куда', 'Дата отправления', 'Дата прибытия']
                choise = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_plane_tickets))
                plane_dict = {'from': choise[0], 'to': choise[1], 'departure_date': choise[2],
                              'arrival_date': choise[3]}
                request = Request('find_plane_tickets', plane_dict)
                filter_list = front_controller.handle(request).data
                map_id = dict()
                for item in filter_list:
                    string = 'Время отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                        'arrival_time'] + "   Цена:" + str(item['price'])
                    map_id[string] = item['id']
                    info.append(string)
                out = easygui.choicebox(
                    msg='Откуда:' + choise[0] + '\nКуда:' + choise[1] + '\nДата отправления:' + choise[
                        2] + '\nДата прибытия: ' + choise[3], title="Авиослейвс ПутешествиЯ", choices=info)
                seat = easygui.enterbox(msg="Введите место(от 1 до 69)", image=r'pictures/hand.jpg',
                                        title="Авиослейвс ПутешествиЯ")
                request = Request('add_plane_ticket_to_tour',
                                  {'tour_id': tour_id, 'id': map_id[out], 'seat': seat})
                front_controller.handle(request)

            if fin == 'Ж/Д':
                list_info_train_tickets = ['Откуда', 'Куда', 'Дата отправления', 'Дата прибытия']
                fin = easygui.multenterbox("", title="Авиослейвс ПутешествиЯ", fields=(list_info_train_tickets))
                plane_dict = {'from': fin[0], 'to': fin[1], 'departure_date': fin[2], 'arrival_date': fin[3]}
                request = Request('find_train_tickets', plane_dict)
                filter_list = front_controller.handle(request).data
                map_id = dict()
                for item in filter_list:
                    string = 'Вермя отправления:' + item['departure_time'] + '  Время прибытия:' + item[
                        'arrival_time'] + "   Цена:" + str(item['price'])
                    map_id[string] = item['id']
                    info.append(string)
                out = easygui.choicebox(
                    msg='Откуда:' + fin[0] + '\nКуда:' + fin[1] + '\nДата отправления:' + fin[
                        2] + '\nДата прибытия: ' + fin[3],
                    title="Авиослейвс ПутешествиЯ", choices=info)
                carriage = easygui.enterbox(msg="Введите место(от 1 до 8)", image=r'pictures/carriage.jpg',
                                            title="Авиослейвс ПутешествиЯ")
                seat = easygui.enterbox(msg="Введите место(от 1 до 28)", image=r'pictures/seat.jpg',
                                        title="Авиослейвс ПутешествиЯ")
                request = Request('add_train_ticket_to_tour',
                                  {'tour_id': tour_id, 'id': map_id[out], 'seat': seat,'carriage': carriage})
                front_controller.handle(request)

            if choise == 'Оформить тур':
                request = Request('buy_tour', {'tour_id': tour_id, 'client_id': client_id})
                front_controller.handle(request)
                #request = Request('find_purchases', {'client_id': client_id})
                #print(front_controller.handle(request))
                break


