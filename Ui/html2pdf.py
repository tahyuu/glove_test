import pdfkit
import time
import os
from sample_information_input import Sample
import matplotlib.pyplot as plt
import numpy


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
    #update table for report 
    i=0
    for sample in samples:
        #for op1
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %sample.s_slot
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.op1
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr1*100)
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
        str_list=str_list+"</tr>"
        
        #for rp1
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %sample.s_slot
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.rp1
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr1*100)
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
        str_list=str_list+"</tr>"

        #for op2
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %sample.s_slot
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.op2
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr2*100)
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
        str_list=str_list+"</tr>"        
        
        #for rp2
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %sample.s_slot
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.rp2
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr2*100)
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
        str_list=str_list+"</tr>"                

        #for op3
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %sample.s_slot
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.op3
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr3*100)
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
        str_list=str_list+"</tr>"     

         #for rp3
        str_list=str_list+"<tr>"
        str_list=str_list+"<th scope=\"row\">&nbsp;%s</th>" %sample.s_slot
        #str_list=str_list+"<td>&nbsp;Sample %s</td>" %sample.s_slot 
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_name
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_mtype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_color
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_thickness
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_ctype
        str_list=str_list+"<td>&nbsp;%s</td>" %sample.s_standard
        str_list=str_list+"<td>&nbsp;%.3f</td>" %sample.rp3
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr3*100)
        str_list=str_list+"<td>&nbsp;%.2f%%</td>" %(sample.dr*100)
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
        
def CharCreate():
#    fig  = plt.figure()
#    ax = fig.add_subplot(1,1,1)
#    ax.plot([1,2,3,4],[2,3,4,5])
#    plt.title("Matplotlib demo") 
#    plt.xlabel("x axis caption") 
#    plt.ylabel("y axis caption")
#    plt.show()

    fig=plt.figure(figsize=(6, 3))
    plt.plot([1,2,3,4],[2,3,4,5], c='red',)
    plt.plot([1,2,3,4],[1,3,3,5], c='blue',)
    plt.plot([1,2,3,4],[1,2,3,3], c='green', )
    plt.plot([1,2,3,4],[1,2,2, 0], c='skyblue', )
    plt.plot([1,2,3,4],[1,2,1, 0], c='yellow', )
    plt.plot([1,2,3,4],[1,1,1, 0], c='pink', )

    plt.legend(('op1', 'rp1', 'op2', 'rp2', 'op3', 'rp3')) 
    plt.show()


    #pdfkit.from_url('http://google.com', 'out.pdf', options=options)
if __name__=="__main__":
    #html2pdf("E:\\WorkSpace\\gloves_test\\Program\\Ui\\Results\\admin", "test.pdf")
    CharCreate()
