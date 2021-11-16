
class FileAttribs:
    def __init__(self, json):
        self.json = json
        self.title = json['title']
        self.episodes = json['episodes']
    
    def check(self):
        if(len(self.title) == 0):
            raise Exception(f'Invalid title: {title}')
        if(len(self.episodes) == 0):
            raise Exception(f'There are no episodes entered. Please double check.')
    