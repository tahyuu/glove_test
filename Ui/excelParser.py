"""
Module implementing Dialog.

"""
import xlrd,xlwt,xlutils
from win32com import client
import os

class ExcelHelper:
    def __init__(self):
        pass
    #д����
    def write_excel(self,filename, data):
        book = xlwt.Workbook()            #����excel����
        sheet = book.add_sheet('sheet1')  #���һ����
        c = 0  #���浱ǰ��
        for d in data: #ȡ��data�е�ÿһ��Ԫ��浽����ÿһ��
            for index in range(len(d)):   #��ÿһ��Ԫ���е�ÿһ����Ԫ�浽ÿһ��
                sheet.write(c,index,d[index])
            c += 1
        book.save(filename) #����excel

    def xls2pdf(self, filename):
        self._export_folder=""
        '''
        xls �� xlsx �ļ�ת��
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = client.Dispatch("Excel.Application")
        xlApp.Visible = False    
        xlApp.DisplayAlerts = 0   
        books = xlApp.Workbooks.Open(r"abc.xls",False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        print('���� PDF �ļ���', exportfile)
        xlApp.Quit()
if __name__ == "__main__":
    eh = ExcelHelper()
    eh.write_excel(r"abc.xls", [["a", "b", "c"], ["aa", "bb", "cc"]])

    eh.xls2pdf(r"abc.xls")
