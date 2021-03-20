from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
import threading

def Video_Download():
    Show_information.insert('end','Ready Download.\n')
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
    Show_information.insert('end','Title =' + info.get('title') + '\n')
    Show_information.insert('end','Title =' + info.get('format') + '\n')
    Show_information.insert('end','Downloading...Waiting...\n')
    Show_information.see('end')
    if get_url == '':
        Show_information.insert('end','No URL.\n')
        Show_information.see('end')
    else:
        try:
            ydl.download([get_url])
        except Warning:
            print('!!!!!!!!!!!!')
            
    Show_information.insert('end','Done!\n')
    Show_information.see('end')

def Thread_():
    t = threading.Thread(target=Video_Download)
    t.setDaemon(True)
    t.start()

window = tk.Tk()
window.geometry('500x650')
window.configure(bg='#3c4bb4')
window.title("Video Downloader - created by hurosu")
video_url_text = tk.Label(window,text = "URL : ",bg='#3c4bb4')
video_url_text.place(x = 32,y = 13)
video_url = tk.Entry(window)
video_url.place(x = 70,y = 15,width=350,height=18)
save_path_text = tk.Label(window,text="PATH : ",bg='#3c4bb4')
save_path_text.place(x = 25,y = 50)
save_path = tk.Entry(window)
save_path.insert(0, "Videos/")
save_path.place(x = 70,y = 50,width=350,height=18)
Download_Button = tk.Button(window,text="Download!!!",command = lambda:Thread_())
Download_Button.place(x = 423,y = 17,width=75,height=70)
video_name = tk.Entry(window)
video_name.place(x = 70,y = 85,width=350,height=18)
video_name_text = tk.Label(window,text="Name : ",bg='#3c4bb4')
video_name_text.place(x = 20,y = 85)
video_extension = tk.Entry(window)
video_extension.place(x = 70,y = 120,width=350,height=18)
video_extension_text = tk.Label(window,text="Extension : ",bg='#3c4bb4')
video_extension_text.place(y = 120)
cookie = tk.Entry(window)
cookie.place(x = 70,y = 150,width=350,height=18)
cookie_text = tk.Label(window,text="Cookie : ",bg='#3c4bb4')
cookie_text.place(x = 15 ,y = 150)
username = tk.Entry(window)
username.place(x = 70,y = 190,width=150,height=18)
username_text = tk.Label(window,text="username : ",bg='#3c4bb4')
username_text.place(x = 0 ,y = 187.5)
password = tk.Entry(window)
password.place(x = 300,y = 190,width=150,height=18)
password_text = tk.Label(window,text="password : ",bg='#3c4bb4')
password_text.place(x = 230 ,y = 187.5)
Show_information = tk.Text(window)
Show_information.place(x = 70,y = 250,width=350,height=350)
Show_information.insert('end','[!]Video Name Default is Video Title.\n\n')
Show_information.insert('end','[!]If Video Title too Long\n')
Show_information.insert('end','The saved video may cause errors.\n\n')
Show_information.insert('end','[!]Extension Default is Video Extension\n')
Show_information.insert('end','Extension Example : .mp4 , .wmv , .mp3.\n\n')
Show_information.insert('end','[!]If have Cookie , Cookie Example : Cookie.txt\n')
Show_information.insert('end','Cookie format is json.\n\n')
Show_information.insert('end','[!]If Video need Login\n')
Show_information.insert('end','You Can use Cookie or type username and password.\n\n')
Show_information.insert('end','[!]Some Video Need Use Special playback software\n')
Show_information.insert('end','Example : VLC Media Player ( www.videolan.org )\n')
Show_information.see('end')

window.mainloop()


#listformats 選擇fotmat
#更新：Youtube影片可選擇畫質
