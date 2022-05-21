from dataclasses import dataclass


@dataclass
class Request:
    command: str
    args: dict


# class Request:
#     def __init__(self, request_str: str):
#         self.request_str = request_str
#         self.request_list = request_str.split('/')
#
#     # 'find_hotel?client_id=1&country=Russia&city=Moscow&1000<price<5000'
#
#     def get_command(self):
#         return self.request_list[0]
#
#     def get_client_id(self):
#         return self.request_list[1][10:]
#
#     def get_params_dict(self):
#         params_list = self.request_list[2].split('&')
#         params_dict = {}
#         for param in params_list:
#             if 'price' in param:
#                 params_dict[param.split('=')[0]] = (
#                     int(param.split('=')[1].split(',')[0]), int(param.split('=')[1].split(',')[1]))
#             else:
#                 params_dict[param.split('=')[0]] = param.split('=')[1]
#         return params_dict
#
#
# # req = Request('find_hotel/client_id=1435hj/country=Russia&city=Moscow&price=0,5000')
# # print(req.get_command())
