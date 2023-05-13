import remote
from tkinter import *
import Videos


class GUI(remote.Television):
    def __init__(self, window):
        self.info_lists = Videos.video_application("Video_links")
        print(f"\n\n\n{self.info_lists}\n\n\n")
        self.window = window
        remote.Television.__init__(self)
        print(f"{self.channel}\n\n\n\n")
        self.MAX_VOLUME = 100
        self.MAX_CHANNEL = 100
        
        "TV"
        self.tv = Tk()
        self.chan = Label(self.tv, text = f"Channel: {self.channel}")
        self.chan.pack()
        self.noise = Label(self.tv, text = f"Volume: {self.volume}")
        self.noise.pack()
        self.info = Label(self.tv, text = f"Power: {'on' if self.status else 'off'}\nSound: {'off' if self.muted else 'on'}")
        self.info.pack()
        self.channel_pos = Label(self.tv, text = f"""   Title:
                                             {self.info_lists[self.channel][0]}""")
        self.channel_pos.pack()
        self.tv.title("TV")
        self.tv.geometry("500x500")
    
        "Center buttons"
        distance = 10
        distance /= 2
        self.top_frame = Frame(self.window)
        self.mute_button = Button(self.top_frame, text = "Mute",
                command = lambda:(self.mute(),self.stat_info()))
        self.power_button = Button(self.top_frame, text = "Power",
                command = lambda:(self.power(),self.stat_info()))
        self.mute_button.pack(padx = distance, side = "left", pady=0)
        self.power_button.pack(padx = distance, side = "right", pady=0)
        self.top_frame.pack(pady = 20)
        
        diameter = 10
        radius = diameter/2
        
        self.channel_up_button = Button(self.window, text = '↑',
                                        command = lambda:(self.channel_up(),
                                                          self.current_chan()))
        self.volume_frame = Frame(self.window)
        self.volume_down_button = Button(self.volume_frame, text = '-',
                                         command = lambda: (self.volume_down(), 
                                                           self.current_sound(),
                                                           self.stat_info()))
        self.volume_up_button = Button(self.volume_frame, text = '+',
                                       command = lambda: (self.volume_up(),
                                                          self.current_sound(),
                                                          self.stat_info()))
        self.channel_down_button = Button(self.window, text = '↓',
                                          command = lambda: (self.channel_down(),
                                                             self.current_chan()))
        "packing the central buttons"
        self.channel_up_button.pack(pady = radius)
        self.volume_down_button.pack(side = "left", padx = radius*2)
        self.volume_up_button.pack(side = "right", padx = radius*2)
        self.volume_frame.pack(pady = radius)
        self.channel_down_button.pack(pady = radius)
        print(self.channel)
        self.video = Button(self.window,
                            text = "Play",
                            command = lambda:(Videos.open_video(self.info_lists[self.channel][1])) if self.channel < len(self.info_lists) else None)
        self.video.pack(pady = 20)
        
        "saved channel buttons"
        channel_space = 5
        button_height = 1
        button_width = 12
        self.channels_frame = Frame(self.window)
        self.a_button = Button(self.channels_frame, width = button_width,
                               height = button_height, text = "Channel A",
                               command = lambda:(self.change1(), self.current_chan()))
        self.b_button = Button(self.channels_frame, width = button_width,
                               height = button_height, text = "Channel B",
                               command = lambda:(self.change2(), self.current_chan()))
        self.c_button = Button(self.channels_frame, width = button_width,
                               height = button_height, text = "Channel C",
                               command = lambda:(self.change3(), self.current_chan()))
        self.d_button = Button(self.channels_frame, width = button_width,
                               height = button_height, text = "Channel D",
                               command = lambda:(self.change4(), self.current_chan()))
        
        
        self.a_button.pack()
        self.b_button.pack(pady = channel_space)
        self.c_button.pack(pady = channel_space)
        self.d_button.pack(pady = channel_space)
        self.channels_frame.pack(pady=10)
        
        self.tv.mainloop()
        
    def current_chan(self):
        print("channel change")
        self.chan.config(text = f"Channel: {self.channel}")
        self.channel_pos.config(text = f"""     Title: 
            {self.info_lists[self.channel][0] if self.channel < len(self.info_lists) else 'None'}""")
        
    def current_sound(self):
        print("sound change")
        self.noise.config(text = f"Volume: {self.volume}")
    
    def stat_info(self):
        self.info.config(text = f"Power: {'on' if self.status else 'off'}\nSound: {'off' if self.muted else 'on'}")
        try: 
            self.image_code(f"images/{self.info_lists[self.channel][2]}.jpg")
        except:
            self.image_code("images/Img Not Found.jpg")
   

   
    def change1(self):
        if self.status: self.channel = 1
    def change2(self): 
        if self.status: self.channel = 2
    def change3(self): 
        if self.status: self.channel = 3
    def change4(self): 
        if self.status: self.channel = 4
        