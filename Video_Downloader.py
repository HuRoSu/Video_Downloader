from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
import threading

def Video_Download():
    
    ydl = youtube_dl.YoutubeDL({'outtmpl': 'file/%(title)s.mp4'})
    ydl.download(['https://twitter.com/i/status/820467689164447745'])

def Thread_():
    t = threading.Thread(target=Video_Download)
    t.setDaemon(True)
    t.start()

window = tk.Tk()
window.geometry('500x500')
window.configure(bg='#3c4bb4')
window.title("Video Downloader - created by hurosu")
video_url_text = tk.Label(window,text = "URL : ",bg='#3c4bb4')
video_url_text.grid(row=1,column=0,padx=30,pady=15)
video_url = tk.Entry(window)
video_url.place(x = 70,y = 15,width=350,height=18)
save_path_text = tk.Label(window,text="PATH : ",bg='#3c4bb4')
save_path_text.grid(row=2,column=0,padx=25,pady=15)
save_path = tk.Entry(window)
save_path.place(x = 70,y = 67.5,width=350,height=18)
Download_Button = tk.Button(window,text="Download!!!",command = lambda:Thread_())
Download_Button.place(x = 423,y = 17,width=75,height=70)
Show_information = tk.Text(window)
Show_information.place(x = 70,y = 120,width=350,height=350)
window.mainloop()
