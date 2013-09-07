
from distutils.core import setup

setup(name='SpeedyDeletionTool',
      version='1.0',
      description='Transfer of articles from wikipedia to speedydeletion.wikia.com ',
      author='James Michael DuPont',
      author_email='jamesmikedupont+sd@gmail.com',
      url='http://speedydeletion.wikia.com',
      packages=[".",
                "batchdownload",
                "category",
                "families",
                "listsofwikis",
                "pywikibot",
                "userinterfaces"
            ],
      install_requires=['feedparser','BeautifulSoup'],

     )
