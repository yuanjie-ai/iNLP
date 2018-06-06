# -*- coding: utf-8 -*-

import urllib
import urllib.request as urllib2

from bs4 import BeautifulSoup


class Stoke(object):
    hanzi5_url = "http://www.hanzi5.com/bishun/%s.html"

    def get_stoke(self, word):
        print("Explode {}".format(word))
        word = hex((ord(word)))[2:]
        word = urllib.parse.quote(word)
        return self.get_stoke_from_hanzi5(word)

    def get_stoke_from_hanzi5(self, word):
        url = self.hanzi5_url % word
        html = self.post_baidu(url)
        if html is None:
            return None
        return self.anlysis_stoke_from_html(html)

    def anlysis_stoke_from_html(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        li = soup.find("div", {"class", "site-article-content hanzi5-article-hanzi-info"})
        for tabb in li.findAll('table'):
            for trr in tabb.findAll('tr')[3:4]:
                for tdd in trr.findAll('td')[1:2]:
                    zh_stoke = tdd.contents
        zh_stoke_list = []
        for st in zh_stoke[0]:
            zh_stoke_list.append(st)
        return zh_stoke_list

    def post_baidu(self, url):
        try:
            timeout = 5
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
    print("extract character stoke from http://www.hanzi5.com/bishun/")

    stoke = Stoke()
    print(stoke.get_stoke("袁"))
