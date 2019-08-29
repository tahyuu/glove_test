# coding='utf-8'
"""
Module implementing Dialog.

"""
import xlrd,xlwt,xlutils
from win32com import client
import os
import time
import win32api

class ExcelHelper:
    def __init__(self):
        pass
    def write_excel(self,filename, data):
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        c = 0
        for d in data:
            for index in range(len(d)):
                sheet.write(c,index,d[index])
            c += 1
        book.save(filename)

    def xls2pdf(self, filename):
        self._export_folder=""
        name = os.path.basename(filename).split('.')[0] + '.pdf'
        exportfile = os.path.join(self._export_folder, name)
        xlApp = client.Dispatch("Excel.Application")
        xlApp.Visible = False    
        xlApp.DisplayAlerts = 0   
        time.sleep(2)
        books = xlApp.Workbooks.Open("E:\\WorkSpace\\gloves_test\\Program\\Ui\\abc.xls",False)
        time.sleep(2)
        exportfile="E:\\WorkSpace\\gloves_test\\Program\\Ui\\%s" %exportfile
        print exportfile
        books.ExportAsFixedFormat(0,exportfile)
        time.sleep(2)
        books.Close(False)
        print('PDF is', exportfile)
        xlApp.Quit()
    def exceltopdf(self,doc):
        excel = client.DispatchEx("Excel.Application")
        excel.Visible = 0

        wb = excel.Workbooks.Open(r'E:\\WorkSpace\\gloves_test\\Program\\Ui\\abc.xls')
        ws = wb.Worksheets[0]

        try:
            wb.SaveAs(r'E:\\WorkSpace\\gloves_test\\Program\\Ui\\abc.pdf', FileFormat=57)
        except Exception, e:
            print "Failed to convert"
            print str(e)
        finally:
            wb.Close()
            excel.Quit()
if __name__ == "__main__":
    eh = ExcelHelper()
    eh.write_excel(r"abc.xls", [["a", "b", "c"], ["aa", "bb", "cc"]])

    #eh.xls2pdf(r"abc.xls")
    eh.exceltopdf(r"abc.xls")
