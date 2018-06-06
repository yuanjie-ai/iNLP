# -*- coding: utf-8 -*-
import urllib
import urllib.request as urllib2

from bs4 import BeautifulSoup

from .handian import Handian


class Stoke(object):
    def __init__(self):
        self.handian = Handian()

    def get_stoke(self, word):
        print("Explode {}".format(word))
        self.handian_url = self.handian.get_url(word=word)
        word_utf = word
        word = hex((ord(word)))[2:]
        word = urllib.parse.quote(word)
        return self.get_stoke_from_handian(word_utf)

    def get_stoke_from_handian(self, word):
        url = self.handian_url
        print("url", url)
        if url == "http://www.zdic.net/sousuo/":
            return None

        html = self.post_baidu(url)
        # print(html)
        if html is None:
            return None
        return self.anlysis_stoke_from_html(html)

    def anlysis_stoke_from_html(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        zh_stoke = soup.find(id="z_i_t2_bis")
        zh_stoke = zh_stoke.contents
        zh_stoke_list = []
        for st in zh_stoke[0]:
            zh_stoke_list.append(st)
        return zh_stoke_list

    def post_baidu(self, url):
        try:
            timeout = 10
            # request = urllib2.Request(url)
            request = urllib2.Request(url)
            request.add_header('User-agent',
                               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
            request.add_header('connection', 'keep-alive')
            request.add_header('referer', url)
            response = urllib2.urlopen(request, timeout=timeout)
            html = response.read()
            response.close()
            return html
        except Exception as e:
            print('URL Request Error:', e)
            return None


if __name__ == "__main__":
    print("extract character stoke from http://www.zdic.net/")

    stoke = Stoke()
    print("中", stoke.get_stoke("袁"))
