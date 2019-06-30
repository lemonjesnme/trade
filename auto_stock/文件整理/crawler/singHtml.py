# -*- coding: utf-8 -*-

from downloader import download


class Crawler(object):
    
    def start(self, urls):
 
        
      for index in range(len(urls)):
          html = download(urls[index])
          print(html)
          


if __name__ == "__main__":
    crawler = Crawler()
    # 同时抓取看过和未看过的链接，两者区别在于status查询参数上
    '''
    root_urls = ['?'.join([base_url, 'start=0&limit=20&sort=new_score&status=P']),
                 '?'.join([base_url, 'start=0&limit=20&sort=new_score&status=F'])]
    '''
    root_urls =['https://xueqiu.com/hq']
    html = crawler.start(root_urls)
    
          