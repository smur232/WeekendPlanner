from django.db import models
from bs4 import BeautifulSoup
import requests
# Create your models here.


class Event(models.Model):
    # These also help determine how the form looks like on the admin page
    url = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=300, default='')
    # TODO: not yet a in a date time format so need a parser (is there a library?)
    event_time = models.CharField(max_length=300, default='')
    address = models.CharField(max_length=300, default='')
    description = models.CharField(max_length=500, default='')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    image_url = models.ImageField(upload_to='images/',
                                  height_field=None,
                                  width_field=None
                                  )

    def __str__(self):
        return self.title

    def parse_through_listing_timeout(self, m_url):
        self.url = m_url
        r = requests.get(m_url)
        soup = BeautifulSoup(r.text, "lxml")
        self.title = soup.find('title').text
        self.description = soup.find("div", {'class': "review__body"}).text
        self.image_url = soup.find("meta", {'property': "og:image"}).get("content")
        self.address = soup.find("meta", {'property': "og:street-address"}).get("content")
        self.latitude = soup.find("meta", {'property': "og:latitude"}).get("content")
        self.longitude = soup.find("meta", {'property': "og:longitude"}).get("content")

        for info in soup.find("table", {'class', 'listing_details'}).find_all('tr'):
            header = info.th
            if '住所' in header and not self.address:
                self.address = info.td.find('br').previousSibling.strip()
            if '営業時間' in header:
                self.event_time = info.td.text
