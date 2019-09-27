import pdfkit
import time
import os
from sample_information_input import Sample
import matplotlib.pyplot as plt
import numpy
import random


def html2pdf(dirs, samples):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header' : [('Accept-Encoding', 'gzip')],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None,
    'quiet': ''
}
    str_list=""
    html_image_list=""
    #update table for report 
    i=0
    for sample in samples:
        #for op1
        ResultDir=os.getcwd()
        print "current Dir is %s" %ResultDir
        html_image_list=html_image_list+"<div class=\"Imgs\"><br><br>Sameple %s <br><hr><img src=\"%s//Figure_1.png\" width=\"650\" height=\"400\" alt=\"\"/></div>" %(i,ResultDir)

        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %(int(sample.s_slot)+1)
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.op1
        str_list=str_list+"<td rowspan=\"3\">&nbsp;%.2f%%</td>" %(sample.dr*100)
        if i==0:
            str_list=str_list+"<td rowspan=\"%s\">&nbsp;%.2f%%</td>" %(len(samples)*6, sample.dr_avg*100)
        str_list=str_list+"</tr>"
        
        #for rp1
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %(int(sample.s_slot)+1)
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.rp1
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr_avg*100)
        str_list=str_list+"</tr>"

        #for op2
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %(int(sample.s_slot)+1)
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.op2
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr_avg*100)
        str_list=str_list+"</tr>"        
        
        #for rp2
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %(int(sample.s_slot)+1)
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.rp2
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr_avg*100)
        str_list=str_list+"</tr>"                

        #for op3
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %(int(sample.s_slot)+1)
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.op3
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr_avg*100)
        str_list=str_list+"</tr>"     

         #for rp3
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %(int(sample.s_slot)+1)
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.rp3
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
#        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr_avg*100)
        str_list=str_list+"</tr>"     
        i=i+1
        
#    for i in range(18):
#        str_list=str_list+"<tr>"
#        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %((i/6)+1)
#        str_list=str_list+"<td>&nbsp;Sample %s</td>" %((i/6)+1) 
#        str_list=str_list+"<td>&nbsp;rubber</td>"
#        str_list=str_list+"<td>&nbsp;Pink</td>"
#        str_list=str_list+"<td>&nbsp;0.5</td>"
#        str_list=str_list+"<td>&nbsp;H2So4</td>"
#        str_list=str_list+"<td>&nbsp;EN374-09</td>"
#        str_list=str_list+"<td>&nbsp;0.532</td>"
#        str_list=str_list+"<td>&nbsp;18%</td>"
#        str_list=str_list+"<td>&nbsp;10%</td>"
#        str_list=str_list+"</tr>"

    html_str=""
    with open("temp.html",'r') as file:
        lines = file.readlines()
        for line in lines:
            html_str=html_str+line
    html_str=html_str.replace('$SampleList$',str_list)
    html_str=html_str.replace('$ImageList$',html_image_list)

    html_str=html_str.replace('$UserName$',"Admin")
    data = time.time()
    timeArray = time.localtime(data)
    time_str=time.strftime('%Y-%m-%d %H:%M:%S',timeArray)
    html_str=html_str.replace('$DateTime$',time_str)
    fileName=time.strftime('%Y-%m-%d-%H-%M-%S.pdf',timeArray)



    #update image for report

    #pdfkit.from_string(html_str, 'out.pdf',options=options) #with --page-size=Legal and --orientation=Landscape
    pdfkit.from_string(html_str, dirs+"\\"+fileName) #with --page-size=Legal and --orientation=Landscape
    #pdfkit.from_file('temp.html','out1.pdf')
    if os.path.isfile(dirs+"\\"+fileName):
        return (True, dirs+"\\"+fileName)
    else:
        return (False, dirs+"\\"+fileName)
        
#def writeExcel(dirs, samples):
#    for sample in samples:
        
        
def GetData():
    data = []
    for i in range(6):
        li =[]
        rate =random.random()
        fu = random.random()
        for j in range(10):
            y1=rate*j*random.uniform(1.0,1.2)+fu
            li.append(y1)
        data.append(li)
    return data
def Move(x, y):
   print "move sensor to Poing(%s,%x)" %(x, y) 
 
        
def CharCreate(data, fileName):
#    fig  = plt.figure()
#    ax = fig.add_subplot(1,1,1)
#    ax.plot([1,2,3,4],[2,3,4,5])
#    plt.title("Matplotlib demo") 
#    plt.xlabel("x axis caption") 
#    plt.ylabel("y axis caption")
#    plt.show()
    fig=plt.figure(figsize=(6, 3))
    color=["blue", "green", "skyblue", "yellow", "pink", "red"]

    i=0

    for li in data:
        #print li
        plt.plot(range(1, len(data[0])+1),li, c=color[i],)
        i=i+1
#        plt.plot([1,2,3,4],[1,3,3,5], c='blue',)
#        plt.plot([1,2,3,4],[1,2,3,3], c='green', )
#        plt.plot([1,2,3,4],[1,2,2, 0], c='skyblue', )
#        plt.plot([1,2,3,4],[1,2,1, 0], c='yellow', )
#        plt.plot([1,2,3,4],[1,1,1, 0], c='pink', )

    plt.legend(('op1', 'rp1', 'op2', 'rp2', 'op3', 'rp3')) 
    #plt.show()
    plt.savefig("%s.png" %fileName)

def WriteExcel(data, fileName):
#Writing Excel
    print "Writing Excel to %s.csv" %fileName
if __name__=="__main__":
    #html2pdf("E:\\WorkSpace\\gloves_test\\Program\\Ui\\Results\\admin", "test.pdf")
    data =GetData()
    CharCreate(data)
