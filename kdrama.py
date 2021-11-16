from classes.episode_downloader import EpisodeDownloader
from classes.file_attribs import FileAttribs
from classes.file_loader import FileLoader

if __name__ == '__main__':
    source = 'kdrama.json'

    file_loader = FileLoader(source)
    file = file_loader.load_file()

    attribs = FileAttribs(file)
    attribs.check()

    downloader = EpisodeDownloader(attribs.title, attribs.episodes)
    downloader.begin_download()

    