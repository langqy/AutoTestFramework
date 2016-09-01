# -*- coding: utf-8 -*-

import re

from tools.read_xls import ReadXls

from src.utils.randomGen import random_string,random_number_str


class CaseData:
    def __init__(self, sheet_name, file_name='p2c2.xlsx'):
        self.data = ReadXls(file_name, sheet_name=sheet_name).get_data()
        self.type = self.data.pop(0)

    def get_type(self, key=None):
        return self.type[key] if key else self.type

    def if_float(self, value):
        try:
            return float(value)
        except:
            return value

    def if_string(self, value):
        return value

    def if_list(self, value):
        to_list = value.split('&')
        return to_list

    def if_int(self, value):
        try:
            return int(value)
        except:
            try:
                return float(value)
            except:
                return value

    def parse_data(self):
        method_patten = re.compile(r'#.+#')
        for index, case in enumerate(self.data):
            for key, cell in case.iteritems():
                if method_patten.search(cell):
                    case[key] = method_patten.sub(self.cell_method(method_patten.findall(cell)[0]), cell)
                if self.type[key].lower() == 'string':
                    case[key] = self.if_string(case[key])
                elif self.type[key].lower() == 'float':
                    case[key] = self.if_float(case[key])
                elif self.type[key].lower() == 'int':
                    case[key] = self.if_int(case[key])
                elif self.type[key].lower() == 'list':
                    case[key] = self.if_list(case[key])
        return self.data

    def cell_method(self, value):
        if 'R.N' in value:
            return random_number_str(int(value.replace('#', '').replace('R.N.', '')))
        elif 'R.S' in value:
            return random_string(int(value.replace('#', '').replace('R.S.', '')))

    def get_data(self):
        return self.parse_data()


if __name__ == '__main__':
    cd = CaseData(sheet_name='add_spot_commodity')
    print cd.get_type('pay_out_algr')
    print cd.get_type()
    print cd.get_data()