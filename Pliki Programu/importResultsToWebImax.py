import os
import datetime
import xlrd

from PyQt4 import QtCore

class ImportResultsToCSV(QtCore.QThread):

    def __init__(self, responsible, path_xls_file, excel_sheet_name, parent=None):
        super(ImportResultsToCSV, self).__init__(parent)
        self.responsible = responsible
        self.excel_sheet_name = excel_sheet_name
        self.work_book = xlrd.open_workbook(path_xls_file)
        self.work_sheet = self.work_book.sheet_by_name(excel_sheet_name)
        self.user_path()

    def run(self):
        self.read_excel_file(self.excel_sheet_name)

    def user_path(self):
        self.userdir = os.path.expanduser('~') + '\\Desktop\\TeRI_Results\\' + str(datetime.date.today()) \
                       + '\\CSV_WebImax'

        if not os.path.exists(self.userdir):
            os.makedirs(self.userdir)

    def read_excel_file(self, excel_sheet_name):
        # Definuje nazwy paczek z konkretnych TC
        if excel_sheet_name == '2G':
            self.package_list = {'KC201': '', 'KC202': '', 'KC203': '', 'KC204': '', 'KC205': '', 'KC206': '',
                                 'KC207': '', 'KC208': '', 'KC221': '', 'KC222': '', 'KC223': '', 'KC231': '',
                                 'KC233': '', 'KC241': '', 'KC_End': ''}
        elif excel_sheet_name == '3G':
            self.package_list = {'KC401': '', 'KC402': '', 'KC403': '', 'KC404': '', 'KC405': '', 'KC406': '',
                                 'KC408': '', 'KC420': '', 'KC421': '', 'KC422': '', 'KC423': '', 'KC424': '',
                                 'KC425': '', 'KC426': '', 'KC427': '', 'KC428': '', 'KC429': '', 'KC430': '',
                                 'KC431': '', 'KC432': '', 'KC433': '', 'KC434': '', 'KC436': '', 'KC437': '',
                                 'KC_End': ''}
        # Wpisywanie zakresów dla poszczególnych paczek KC
        for item in range(self.work_sheet.nrows):
            # Odczytuje i zapisuje do słownika nazwę paczki dla 2G i 3G
            if self.work_sheet.cell_value(item, 9) in self.package_list.keys():
                self.package_list[self.work_sheet.cell_value(item, 9)] = item
                continue
            elif self.work_sheet.cell_value(item, 0) == 'Passed':
                self.package_list['KC_End'] = item

        for count in range(3, 20):
            if self.work_sheet.cell_value(self.package_list['KC_End'] - count, 0) != '':
                self.package_list['KC_End'] -= count + 1
                break

        self.list_to_write_to_csv = list()
        # Tworzymy listę wszystkich TC z excel`a
        for item_ws in range(self.work_sheet.nrows):
            if self.work_sheet.cell_value(item_ws, 0) == 'Passed':
                break
            # Jeżeli pole w excelu z nazwą TC nie jest puste wykonaj instrukcje
            if self.work_sheet.cell_value(item_ws, 0) != '':
                item_list = list()
                item_list.append(
                    [item_ws, self.work_sheet.cell_value(item_ws, 0), self.work_sheet.cell_value(item_ws, 8),
                     self.responsible, self.work_sheet.cell_value(item_ws, 9), '', '',
                     self.work_sheet.cell_value(item_ws, 16)])
                # Jeżeli kolejne pola z TC są puste wykonaj instrukcję (pouste pola oznaczają komórki złączone)
                if self.work_sheet.cell_value(item_ws + 1, 0) == '':
                    # Sprawdzamy kolejne pola w celu stworzenia listy z tym samym TC ale różnymi parametrami
                    for z_item in range(1, 100):

                        if self.work_sheet.cell_value(item_ws + z_item, 0) == '':
                            item_list.append(
                                [item_ws + z_item, self.work_sheet.cell_value(item_ws + z_item, 0),
                                 self.work_sheet.cell_value(item_ws + z_item, 8),
                                 self.responsible, self.work_sheet.cell_value(item_ws + z_item, 9), '', '',
                                 self.work_sheet.cell_value(item_ws + z_item, 16)]
                            )
                        else:
                            if len(item_list) == 1:
                                self.check_and_format_single_tc(excel_tc=item_list[0])

                            elif len(item_list) > 1:
                                self.check_tc_list(tc_list=item_list)
                            break
                else:  # if self.work_sheet.cell_value(item_ws + z_item, 0) == '':
                    # Jeżeli długość item_list jest 1 przekazujemy listę do funkcji w celu formatowania i zapisujemy
                    # do list_to_write_to_cvs
                    if len(item_list) == 1:
                        self.check_and_format_single_tc(excel_tc=item_list[0])

                    elif len(item_list) > 1:
                        self.check_tc_list(tc_list=item_list)
        self.check_time()
        self.write_to_csv()

    def check_tc_list(self, tc_list):
        package = list(self.package_list.keys())
        package.sort()
        list_to_rm = list()

        for item in tc_list:
            if item[4] in package:
                list_to_rm.append(item)

        if len(list_to_rm) > 0:
            for item in list_to_rm:
                tc_list.remove(item)

        if len(tc_list) == 1:
            self.check_and_format_single_tc(excel_tc=tc_list[0])
        elif len(tc_list) > 1:
            self.check_and_format_tc_list(tc_list=tc_list)

    def check_and_format_tc_list(self, tc_list):

        for item in tc_list:
            if item[2] == 'P':
                item[2] = 'passed'
            elif item[2] == 'F':
                item[2] = 'failed'
                self.write_to_file(paramiter='Fail', tc=item)
            elif item[2] == 'N/A':
                self.write_to_file(paramiter='N/A', tc=item)
            elif item[2] == '':
                self.write_to_file(paramiter='Null', tc=item)

        pass_list = [x for x in tc_list if x[2] == 'passed']
        fail_list = [x for x in tc_list if x[2] == 'failed']
        na_list = [x for x in tc_list if x[2] == 'N/A']

        if len(pass_list) == len(tc_list):
            self.check_and_format_single_tc(tc_list[0])
        elif len(fail_list) == len(tc_list):
            self.check_and_format_single_tc(tc_list[0])
        elif len(na_list) == len(tc_list):
            pass
        elif (len(pass_list) + len(fail_list)) == len(tc_list):
            self.check_and_format_single_tc(fail_list[0])
        elif (len(pass_list) + len(na_list)) == len(tc_list):
            self.check_and_format_single_tc(pass_list[0])
        elif (len(fail_list) + len(na_list)) == len(tc_list):
            self.check_and_format_single_tc(fail_list[0])
        elif (len(pass_list) + len(fail_list) + len(na_list)) == len(tc_list):
            self.check_and_format_single_tc(fail_list[0])

    def check_and_format_single_tc(self, excel_tc):
        package = list(self.package_list.keys())
        package.sort()

        if excel_tc[0] >= self.package_list[package[0]] and excel_tc[0] <= self.package_list['KC_End']:
            for index, element in enumerate(excel_tc):
                if type(element) is str:
                    excel_tc[index] = '_'.join(element.split())

            for index, element in enumerate(package):
                try:
                    if (excel_tc[0] > self.package_list[element]) and \
                            (excel_tc[0]< self.package_list[package[index + 1]]):
                        excel_tc[1] = excel_tc[1] + '_' + element
                        break
                except IndexError:
                    if excel_tc[0] > self.package_list[package[-1]] and element == package[-1]:
                        pass

        if excel_tc[2] == 'P':
            excel_tc[2] = 'passed'
            self.list_to_write_to_csv.append(excel_tc)
        elif excel_tc[2] == 'F':
            excel_tc[2] = 'failed'
            self.list_to_write_to_csv.append(excel_tc)
            self.write_to_file(paramiter='Fail', tc=excel_tc)
        elif excel_tc[2] == 'N/A':
            self.write_to_file(paramiter='N/A', tc=excel_tc)
        elif excel_tc[2] == '':
            self.write_to_file(paramiter='Null', tc=excel_tc)
            pass  # write to investigation log

    def write_to_file(self, paramiter, tc):
        """
        Funkcja mająca za zadanie na podstawie parametru wpisać do odpowiedniego pliku logów zawartości zmiennej tc
        :param paramiter:
        :param tc:
        :return:
        """
        if paramiter == 'N/A':
            log_file = open(self.userdir + '\\NA_results_' + self.excel_sheet_name + '.txt', 'a', encoding='utf-8')
            log_file.write('{0}, {1}, {2}, {3}, {4}, {5}, {6} {7}'.format(tc[1], tc[2], tc[3], tc[4], tc[5],
                                                                           tc[6], tc[7], '\n'))
            log_file.close()

        elif paramiter == 'Null':
            log_file = open(self.userdir + '\\TC_without_result_' + self.excel_sheet_name + '.txt', 'a', encoding='utf-8')
            log_file.write('{0}, {1}, {2}, {3}, {4}, {5}, {6} {7}'.format(tc[1], tc[2], tc[3], tc[4], tc[5],
                                                                           tc[6], tc[7], '\n'))
            log_file.close()

        elif paramiter == 'Fail':
            if type(tc[4]) is float:
                tc[4] = self.change_time_represation(tc[4])
            log_file = open(self.userdir + '\\TC_with_FAIL_result_' + self.excel_sheet_name + '.txt', 'a', encoding='utf-8')
            log_file.write('{0}, {1}, {2}, {3}, {4}, {5}, {6} {7}'.format(tc[1], tc[2], tc[3], tc[4], tc[5],
                                                                           tc[6], tc[7], '\n'))
            log_file.close()

    def write_to_csv(self):
        """
        Tworzenie i wpisywanie do pliku CSV wszystkich list z self.list_to_write_to_csv.
        :return:
        """
        out = open(self.userdir + '\\CSV_Import_To_WebImax_' + self.excel_sheet_name + '.csv', 'w')
        for row in self.list_to_write_to_csv:
            row.remove(row[0])
            for column in row:
                out.write('{0};'.format(column))
            out.write('\n')
        out.close()

    def check_time(self):
        """
        This function check all records in list_to_write_to_csv.
        Excel przechowuje komórki w formacie time oraz data jako liczby typu float.
        W celu poprawnego wyświetlania czasu w pliku csv wymagane jest odpowiednie przekształcenie. Wykonuje to funkcja xlrd.xldate_as_tuple
        Zwracana jest tulpa (0, 0, 0, 0, 0, 0). Ostatnie 3 są odpowiedzialne za czas H, M, S.

        :return:
        """
        for item in self.list_to_write_to_csv:
            if type(item[4]) is float:
                a = xlrd.xldate_as_tuple(item[4], self.work_book.datemode)
                item[4] = str(a[3])+str(':')
                if a[4] < 9 and a[4] >= 0:
                    item[4] += ('0' + str(a[4]) + ':')
                else:
                    item[4] += (str(a[4]) + ':')

                if a[5] < 9 and a[5] >= 0:
                    item[4] += ('0' + str(a[5]))
                else:
                    item[4] += (str(a[5]))

    def change_time_represation(self, time):
        a = xlrd.xldate_as_tuple(time, self.work_book.datemode)
        time = str(a[3])+str(':')
        if a[4] < 9 and a[4] >= 0:
            time += ('0' + str(a[4]) + ':')
        else:
            time += (str(a[4]) + ':')

        if a[5] < 9 and a[5] >= 0:
            time += ('0' + str(a[5]))
        else:
            time += (str(a[5]))

        return time