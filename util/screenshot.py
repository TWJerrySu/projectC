import os
import os.path

class screenshot:
    def __init__(self):
        pass

    def get_stock_number_list(self):
        tmp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
        path = os.path.join(tmp_path, "data", "stock.scv")
        data = open(path)
        data_list = data.read().split(',')
        print(data_list)
        return data_list

    def take_screen_from_list(self, stock_num):
        stk = stock_num + '.png'
        file_path = os.path.join(self.save_path, stk)
        self.driver.get_screenshot_as_file(file_path)

# a = screenshot()
# a.get_stock_number_list()
# for cc in d :
#     a.take_screen_from_list(cc)
