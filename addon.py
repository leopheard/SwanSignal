from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.simplecast.com/Z1tu2Hds"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://image.simplecastcdn.com/images/0cb5ca85-da11-4b94-9f5e-381719ff4f48/776e1e7d-8130-4373-a1ed-b62fac052cf5/3000x3000/swansignalpodcastcoverat2x.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://image.simplecastcdn.com/images/0cb5ca85-da11-4b94-9f5e-381719ff4f48/776e1e7d-8130-4373-a1ed-b62fac052cf5/3000x3000/swansignalpodcastcoverat2x.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
