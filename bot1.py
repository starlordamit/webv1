import os
import telepot
import time
import subprocess
token='1853159306:AAEyEvCh1CRXCwZzvw_G3lwumfLY5_IDQto'
phy='database//phy'
chem='database//chem'
math='database//math'
phydpp='database//phydpp'
chemdpp='database//chemdpp'
mathdpp='database//mathdpp'
botvar=''
car='''<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<body class="w3-black">
</div>
<div class="w3-padding-large" id="main">
<header class="w3-container w3-padding-32 w3-center w3-black" id="home">
</header>'''
template='''<!DOCTYPE html>
<title>Pryass 2021</title>
<h1 class="w3-jumbo"><span class="w3-hide-small">Pryaas Batch 2021</h1>
<p>Time To Rule the World.</p>

'''
endtemplate='</body></html>'
datastructure=['','','','']
def cmd_c(cmd):
    a=subprocess.getoutput(cmd)
    #cc=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    n=2000
    message=[a[i:i+n] for i in range(0, len(a), n)]
    return message


def read_data(sub):
    di='database//'+sub
    with open(di,'r') as f:
        ##|lecture1|[lecture1]\n[lecture2]
        data=f.read()
        data=data.split('|')
        try:
            data.remove('')
        except:
            a=True
        #print(data)
        #['lecture1','[lecture1]\n[lecture2]\n','lecture 2']
        chapters=[]
        chaptersdata=[]
        for i in range(len(data)//2):
            chapters.append(data[i*2])
            chaptersdata.append(data[(i*2)+1])
        chpterdatalist=[]
        try:
            chaptersdata.remove('')
        except:
            a=True
        #print(chaptersdata)
        #print(chapters)
        chaptersdata1=chaptersdata[0].split('\n')
        #print(chaptersdata1)
        try:
            chaptersdata1.remove('')
        except:
            tt=True
        #print(chaptersdata1)
        chapterdatalist=[]
        for j in chaptersdata1:
            #print(j)
            #print(eval(j))
            chapterdatalist.append(eval(j))
            #[[lec1],[lec2]]
        print('#done')
        return (chapters,chapterdatalist)
    
def newchapter(name,data):
    #phy|chaptername
    #data=data.split('|')
    with open('database//'+name,'a') as f:
        wdata="|"+data+"|"
        f.write(wdata)
def write_data(name,data,link):
    #phy|lectureno|link
    #data=lecturedata.split('|')
    with open('database//'+name,'a') as f:
        wdata=str([data,link])+'\n'
        f.write(wdata)
        #|lecture1|[lecture1]\n[lecture2]

def html_maker():
    mainhtml=template+'<hr><H1>Lectures</h1><hr>'
    data_lectures=[read_data('phy'),read_data('chem'),read_data('math'),read_data('phydpp'),read_data('chemdpp'),read_data('mathdpp')]
    name=['PHYSICS LECTURES','CHEMISTRY LECTURES','MATH LECTURES','PHYSICS DPPs','CHEMISTRY DPPs','MATH DPPs']
    bb=0
    #data_dpp= []
    for sub in data_lectures:
        #i=([chapters],[chaptersdata])

        ch=sub[0]
        chd=sub[1]
        #print(ch)
        #print(len(ch))
        mainhtml+='<h2><hr>'+name[bb]+'</h2>'
        bb+=1
        for i in range(len(ch)):
            #print(i)
            #print(mainhtml)
            #print(ch)
            #for cha in ch:
                #print(cha)
                mainhtml+='<h3>'+ch[i]+'</h3>'
                mainhtml+='<ul>'
                #print(chd)
                for lec in chd:
                    syntx1='<button class="w3-button w3-light-grey w3-padding-large w3-section"><a href='
                    syntax2='</a>'
                    syn3='</button>'
                    #print(lec)
                    #gg=syntx1+lec[1]+'>'+lec[0]+syntax2+syn3
                    gg=f'<br><a href={lec[1]}>{lec[0]}</a>'
                    print(gg)
                    mainhtml+=gg
                    
                mainhtml+='</ul>'
                #print(mainhtml)
    mainhtml+=endtemplate
    with open('index.html','w') as f:
         f.write(mainhtml)

            
        
    
def handle(msg):
    chat_id = msg['chat']['id']
    try:
        text =  msg['text']
    except:
        text = ''
    sender = msg['from']['id']
    msgid=['message_id']
    tx=text
    try:
        text=text.split('|')
    except:
        a=True
    if text[0] == 'new':
        newchapter(text[1],text[2])
        bot.sendMessage(chat_id,text[2]+'Added.. ')
        html_maker()
    elif text[0]=='add':
        #phy|lectureno|link
        write_data(text[1],text[2],text[3])
        bot.sendMessage(chat_id,text[2]+'Added.. ')
        html_maker()
    else:
        for i in cmd_c(tx):
            bot.sendMessage(chat_id,i)
html_maker()
#bot = telepot.Bot(token)
#bot.message_loop(handle)
#while 1:
#    time.sleep(10)
