class Television:
    "Defaults"
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        self.status = True
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL
        self.SAVED_VOLUME = 0
    
    def control(self, end, pos, step, start):
        if pos == end:
            pos = start
        else:
            pos += step
        return pos
    
    def power(self):
            self.status = True if self.status == False else False
    
    def mute(self):
        if self.status:
            self.muted = True if self.muted == False else False
            if self.muted:
                self.SAVED_VOLUME = self.volume
                self.volume = 0
            else:
                self.volume = self.SAVED_VOLUME
    
    def channel_up(self):
        if self.status:
            self.channel = self.control(self.MAX_CHANNEL, self.channel, 1, self.MIN_CHANNEL)
    
    def channel_down(self):
        if self.status:
            self.channel = self.control(self.MIN_CHANNEL, self.channel, -1, self.MAX_CHANNEL)
    
    def volume_up(self):
        if self.status:
            if self.muted: self.mute()
            self.volume = self.control(self.MAX_VOLUME, self.volume, 1, self.MAX_VOLUME)
    
    def volume_down(self):
        if self.status:
            if self.muted: self.mute()
            self.volume = self.control(self.MIN_VOLUME, self.volume, -1, self.MIN_VOLUME)

    def __str__(self):
        string = f"TV status: Power = {self.status}, Channel = {self.channel}"
        string += f", Volume = {self.volume}"
        return string
