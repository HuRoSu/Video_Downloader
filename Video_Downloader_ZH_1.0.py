from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
import threading

def Video_Download():
    Show_information.insert('end','分析中，過久需換網址嘗試或不支援\n')
    Show_information.see('end')
    get_url = video_url.get()
    get_path = save_path.get()
    get_video_name = video_name.get()
    get_extension = video_extension.get()
    get_cookie = cookie.get()
    get_username = username.get()
    get_password = password.get()
    ydl_list = youtube_dl.YoutubeDL({'cookiefile': get_cookie,
                                    'embedthumnail': True,
                                    'listformats': True,
                                    'username': get_username,
                                    'password': get_password
                                    }).extract_info(get_url,download=False)
    print(str(ydl_list).split(' '))
    if (((get_url.split('.'))[1] == "youtube"))|(((get_url.split('/'))[2]=="youtu.be")):
        ydl = youtube_dl.YoutubeDL({
                                    'merge-output-format' : 'mp4',
                                    'outtmpl': get_path + '%(title)s.%(ext)s',
                                    'cookiefile': get_cookie,
                                    'embedthumnail': True,
                                    #'listformats': True,
                                    'username': get_username,
                                    'password': get_password
                                    })
    elif (get_video_name == '') & (get_extension == ''):
        ydl = youtube_dl.YoutubeDL({'format': 'bestvideo+bestaudio/best',
                                    'merge-output-format' : 'mp4',
                                    'outtmpl': get_path + '%(title)s.%(ext)s',
                                    'cookiefile': get_cookie,
                                    'embedthumnail': True,
                                    #'listformats': True,
                                    'username': get_username,
                                    'password': get_password
                                    })
    elif (get_video_name != '') & (get_extension != ''):
        ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best',
                                    'outtmpl': get_path + get_video_name + get_extension,
                                    'cookiefile': get_cookie,
                                    'embedthumnail': True,
                                    #'listformats': True,
                                    'username': get_username,
                                    'password': get_password
                                    })
    elif (get_video_name == '') & (get_extension != ''):
        ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best',
                                    'outtmpl': get_path + '%(title)s' + get_extension,
                                    'cookiefile': get_cookie,
                                    'embedthumnail': True,
                                    #'listformats': True,
                                    'username': get_username,
                                    'password': get_password
                                    })
    elif (get_video_name != '') & (writethumbnail == ''):
        ydl = youtube_dl.YoutubeDL({'format': 'bestaudio/best',
                                    'outtmpl': get_path + get_video_name + '.%(ext)s',
                                    'cookiefile': get_cookie,
                                    'embedthumnail': True,
                                    #'listformats': True,
                                    'username': get_username,
                                    'password': get_password
                                    })
    info = youtube_dl.YoutubeDL().extract_info(get_url,download=False)
    Show_information.insert('end','影片標題 =' + info.get('title') + '\n')
    Show_information.insert('end','影片格式 =' + info.get('format') + '\n')
    Show_information.insert('end','下載中...請稍等...\n')
    Show_information.see('end')
    if get_url == '':
        Show_information.insert('end','無網址\n')
        Show_information.see('end')
    else:
        try:
            ydl.download([get_url])
        except Warning:
            print('!!!!!!!!!!!!')
            
    Show_information.insert('end','下載完成！\n')
    Show_information.see('end')

def Thread_():
    t = threading.Thread(target=Video_Download)
    t.setDaemon(True)
    t.start()


def copy(editor, event=None):
    editor.event_generate("<<Copy>>")
def cut(editor, event=None):
    editor.event_generate("<<Cut>>")
def paste(editor, event=None):
    editor.event_generate("<<Paste>>")
def rightKey(event, editor):
    menubar.delete(0,tk.END)
    menubar.add_command(label='複製',command=lambda:copy(editor))
    menubar.add_command(label='剪下',command=lambda:cut(editor))
    menubar.add_command(label='貼上',command=lambda:paste(editor))
    menubar.post(event.x_root,event.y_root)



window = tk.Tk()
window.geometry('500x650')
window.configure(bg='#3c4bb4')
window.title("影片下載器 - 製作 by hurosu")
menubar = tk.Menu(window,tearoff=False)
video_url_text = tk.Label(window,text = "網址 : ",bg='#3c4bb4')
video_url_text.place(x = 20,y = 13)
video_url = tk.Entry(window)
video_url.place(x = 70,y = 15,width=350,height=18)
video_url.bind("<Button-3>", lambda x: rightKey(x, video_url))
save_path_text = tk.Label(window,text="路徑 : ",bg='#3c4bb4')
save_path_text.place(x = 20,y = 50)
save_path = tk.Entry(window)
save_path.bind("<Button-3>", lambda x: rightKey(x, save_path))
save_path.insert(0, "影片/")
save_path.place(x = 70,y = 50,width=350,height=18)
Download_Button = tk.Button(window,text="下載",command = lambda:Thread_())
Download_Button.place(x = 423,y = 17,width=75,height=70)
video_name = tk.Entry(window)
video_name.bind("<Button-3>", lambda x: rightKey(x, video_name))
video_name.place(x = 70,y = 85,width=350,height=18)
video_name_text = tk.Label(window,text="名稱 : ",bg='#3c4bb4')
video_name_text.place(x = 20,y = 85)
video_extension = tk.Entry(window)
video_extension.bind("<Button-3>", lambda x: rightKey(x, video_extension))
video_extension.place(x = 70,y = 120,width=350,height=18)
video_extension_text = tk.Label(window,text="副檔名 : ",bg='#3c4bb4')
video_extension_text.place(x = 20,y = 120)
cookie = tk.Entry(window)
cookie.bind("<Button-3>", lambda x: rightKey(x, cookie))
cookie.place(x = 70,y = 150,width=350,height=18)
cookie_text = tk.Label(window,text="Cookie : ",bg='#3c4bb4')
cookie_text.place(x = 15 ,y = 150)
username = tk.Entry(window)
username.place(x = 70,y = 190,width=150,height=18)
username_text = tk.Label(window,text="帳號 : ",bg='#3c4bb4')
username_text.place(x = 20 ,y = 187.5)
password = tk.Entry(window)
password.place(x = 300,y = 190,width=150,height=18)
password_text = tk.Label(window,text="密碼 : ",bg='#3c4bb4')
password_text.place(x = 250 ,y = 187.5)
Show_information = tk.Text(window)
Show_information.place(x = 70,y = 250,width=350,height=350)
Show_information.insert('end','[!]影片名稱預設為影片標題\n\n')
Show_information.insert('end','[!]若名稱太長\n')
Show_information.insert('end','有可能造成儲存錯誤\n\n')
Show_information.insert('end','[!]副檔名預設為mp4\n')
Show_information.insert('end','也可以改變名稱，例如 : .mp4 , .wmv , .mp3.\n\n')
Show_information.insert('end','[!]如果需要Cookie , Cookie Example : Cookie.txt\n')
Show_information.insert('end','Cookie 格式為 is json.\n\n')
Show_information.insert('end','[!]如果需要登入\n')
Show_information.insert('end','可以使用Cookie或在帳號密碼內輸入帳號密碼\n\n')
Show_information.insert('end','[!]有些影片需要用特殊軟體開啟\n')
Show_information.insert('end','例如 : VLC Media Player ( www.videolan.org )\n\n')
Show_information.insert('end','[!]目前測試可支援網站：Youtube、Twitter、抖音等\n')
Show_information.see('end')
Show_information.bind("<Button-3>", lambda x: rightKey(x, Show_information))

window.mainloop()


#listformats 選擇fotmat
#更新：Youtube影片可選擇畫質
