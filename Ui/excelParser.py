"""
Module implementing Dialog.

"""
import xlrd,xlwt,xlutils
from win32com import client
import os

class ExcelHelper:
    def __init__(self):
        pass
    #写数据
    def write_excel(self,filename, data):
        book = xlwt.Workbook()            #创建excel对象
        sheet = book.add_sheet('sheet1')  #添加一个表
        c = 0  #保存当前列
        for d in data: #取出data中的每一个元组存到表格的每一行
            for index in range(len(d)):   #将每一个元组中的每一个单元存到每一列
                sheet.write(c,index,d[index])
            c += 1
        book.save(filename) #保存excel

    def xls2pdf(self, filename):
        self._export_folder=""
        '''
        xls 和 xlsx 文件转换
        '''
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = client.Dispatch("Excel.Application")
        xlApp.Visible = False    
        xlApp.DisplayAlerts = 0   
        books = xlApp.Workbooks.Open(r"abc.xls",False)
        books.ExportAsFixedFormat(0, exportfile)
        books.Close(False)
        print('保存 PDF 文件：', exportfile)
        xlApp.Quit()
if __name__ == "__main__":
    eh = ExcelHelper()
    eh.write_excel(r"abc.xls", [["a", "b", "c"], ["aa", "bb", "cc"]])

    eh.xls2pdf(r"abc.xls")
