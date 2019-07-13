import requests
import datetime
import re, sys, json, os
from bs4 import BeautifulSoup

from datetime import datetime
from threading import Timer

#========================================================
# logs
import logging
from logging.handlers import RotatingFileHandler

def main():
    if not os.path.exists('logs'):
        os.mkdir('logs')
    if not os.path.exists('web/api/programme_tv'):
        os.makedirs('web/api/programme_tv')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
    #file
    file_handler = RotatingFileHandler('logs/programme_tv.log', 'a', 1000000, 1)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    #console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
    #========================================================
    
    requests.encoding = 'utf-8'
    
    main_site = 'https://www.programme.tv'
    types = [
        'tnt',
        'generaliste', 'canal-tps',
        'cinema', 'sport',
        'information', 'belgique-suisse',
        'jeunesse', 'musique',
        'documentaire', 'serie'
    ]
    
    def get_links(url):
        urls = []
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.select("#daynav > li > a")[:3]
        for link in links:
            urls.append(main_site + link.attrs['href'])
        return urls
    
    def get_program(urls):
        out = []
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            boxes = soup.select('ul .box')
            page = {}
            for box in boxes:
                top = box.select('.bheader')[0]
                data = box.select('.bcontent')[0]
    
                # long infos request
                try:
                    full_link = main_site + data.select('h2 a')[0].attrs['href']
                    req = requests.get(full_link)
                    full_data = BeautifulSoup(req.text, 'html.parser')
                except Exception as e:
                    full_link = None
                    logger.error(str(e) + '\n url: %s\nbox : %s' % (url, re.sub('( +)|(\n+)', ' ', box.text)))
    
                # short infos
                infos = {
                    'logo': top.select('a img')[0].attrs['src'],
                    'heure': top.select('.hour')[0].text,
                    'titre': data.select('h2')[0].text.strip(),
                    'resume': data.select('.resume')[0].text.strip(),
                    'lien': full_link,
                }
                if len(data.select('.subtitle')):
                    infos['subtitle'] = data.select('.subtitle')[0].text.strip()
    
                try:
                    # long infos
                    infos['long-title'] = re.sub('( +)|(\n+)', ' ', full_data.select('.title h1')[0].text.strip())
                    infos['type'] = full_data.select('.title .type')[0].text
                    infos['infos'] = [item.text for item in full_data.select('.desc .infos')]
                    infos['long-resume'] = full_data.select('.resume p')[0].text
                except Exception as e:
                    logger.error(str(e) + '\n url: %s' % full_link)
    
                chaine = top.select('a img')[0].attrs['alt'][10:]
                page[chaine] = infos
            out.append(page)
        return out

    for type_prog in types:
        logger.info(type_prog + ' starting')
    
        url = main_site + '/%s/' % type_prog
        urls = get_links(url)
        data = get_program(urls)

        with open('web/api/programme_tv/' + type_prog + '.json', 'w+') as fp:
            json.dump(data, fp)
            logger.info(type_prog + ' done')
    
    logger.info('All done')
    

def auto_scraper():
    now = datetime.today()
    y = now.replace(day=now.day + 1, hour=1, minute=0, second=0, microsecond=0)
    delta_t = y - now
    
    secs = delta_t.seconds + 1

    t = Timer(secs, main)
    main()
    t.start()
