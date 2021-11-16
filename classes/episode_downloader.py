import m3u8_To_MP4

class EpisodeDownloader:
    def __init__(self, title, episodes):
        self.title = title
        self.episodes = episodes
    
    def begin_download(self):
        for e in self.episodes:
            fn = e['fn']
            url = e['url']
            filename = f'{self.title}_{fn}.mp4'
            try:
                m3u8_To_MP4.async_download(url, mp4_file_name=filename)
                print(f'Successfully downloaded {filename}')
            except Exception:
                raise f'There was a problem downloading {filename}'
