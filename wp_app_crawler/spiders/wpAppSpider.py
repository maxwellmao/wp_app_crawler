from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from wp_app_crawler.items import WpAppItem
import json

class WPAppSpider(CrawlSpider):
    name='wp_app'
    allowed_domains=['www.windowsphone.com']
    start_urls=[
            'http://www.windowsphone.com/en-us/store/featured-apps',
            'http://www.windowsphone.com/en-us/store/featured-games'
    ]


    def parse(self, response):
        '''
            parsing the total categories of app store
        '''
        print '[Parse]', response.url
        for category in response.xpath('//div[@id="main"]/ul[@class="categoryNav navText"]/li/a/@href'):
            cateURL=category.extract()
            yield Request(cateURL, callback=self.parseCategory)
#            print cateURL

    def parseCategory(self, response):
        print '[Parse Category Menus]', response.url
        for menu in response.xpath('//div[@class="appSet"]/ul[@class="hMenu filters"]/li/a/@href'):
            menuURL=menu.extract()
#            print menuURL
            yield Request(menuURL, callback=self.parseCategoryMenuApp)

    def parseCategoryMenuApp(self, response):
        print '[parseCategoryMenuApp]', response.url
        for app in response.xpath('//table[@class="appList"]/tbody/tr/td[@class="small"]/a[@class="appImage small"]/@href'):
            appURL=app.extract()
#            print appURL
            yield Request(appURL, self.parseApp)

        for next in response.xpath('//a[@id="nextLink"]/@href'):
            nextURL=next.extract()
#            print '[Next Link]', nextURL
            yield Request('http://www.windowsphone.com'+nextURL, self.parseCategoryMenuApp)

    def parseApp(self, response):
        print '[Parse App]', response.url
        info={}
        item=WpAppItem()
        info['url']=item['url']=response.url
        name=response.xpath('//div[@id="application" and @class="game"]/h1/text()[1]')
        if name:
            info['name']=item['name']=name[0].extract()
        else:
            info['name']=item['name']=''
        
        price=response.xpath('//div[@id="offer"]/span/text()[1]')
        if price:
            info['price']=item['price']=price[0].extract()
        else:
            info['price']=item['price']=''

        review=response.xpath('//div[@id="rating"]/meta[@itemprop="ratingCount"]/@content')
        if review:
            info['review_num']=item['review_num']=review.extract()[0]
        else:
            info['review_num']=item['review_num']=''

        rate=response.xpath('//div[@id="rating"]/meta[@itemprop="ratingValue"]/@content')
        if rate:
            info['rating']=item['rating']=rate.extract()[0]
        else:
            info['rating']=item['rating']=''

        like=response.xpath('//div[@class="pluginCountButton pluginCountNum"]/span[@class="pluginCountTextDisconnected"]/text()[1]')
        if like:
            info['fb_like']=item['fb_like']=like[0].extract()
        else:
            info['fb_like']=item['fb_like']=''

#        info['social_network']=item['social_network']=response.xpath('//div[@id="socialNetworks"]').extract()

        tweet=response.xpath('//div[@id="twitter"]/iframe/html/body/div[@id="widget"]/div[@id="c"]/a[@id="count"]')
#        print '[iframe]', response.xpath('//iframe').extract()
#        print '[tweet]', tweet
        if tweet:
            info['tweet_num']=item['tweet_num']=tweet.extract()
        else:
            info['tweet_num']=item['tweet_num']=''

        publish=response.xpath('//div[@id="publisher"]/a[@itemprop="publisher"]/text()[1]')
        if publish:
            info['publisher']=item['publisher']=publish[0].extract()
        else:
            info['publisher']=item['publisher']=''

        size=response.xpath('//div[@id="packageSize"]/span/text()[1]')
        if size:
            info['size']=item['size']=size[0].extract()
        else:
            info['size']=item['size']=''

        date=response.xpath('//div[@id="releaseDate"]')
        if date:
            info['release_date']=item['release_date']=date[0].extract()
        else:
            info['release_date']=item['release_date']=''

        version=response.xpath('//div[@id="version"]')
        if version:
            info['version']=item['version']=version[0].extract()
        else:
            info['version']=item['version']=''

        require=[]
        for r in response.xpath('//div[@id="softwareRequirements"]/ul/li/text()[1]'):
            require.append(r.extract())
        info['works_with']=item['works_with']='\t'.join(require)

        require=[]
        for r in response.xpath('//div[@id="hardwareRequirements"]/ul/li/text()[1]'):
            require.append(r.extract())
        info['app_require']=item['app_require']='\t'.join(require)

        lang=[]
        for l in response.xpath('//div[@id="languageList"]/div[@class="wrapper"]/div[@class="textContainer"]/span/text()[1]'):
            lang.append(l.extract())
        info['lang']=item['lang']='\t'.join(lang)

        desc=response.xpath('//div[@class="description"]/pre/text()[1]')
        if desc:
            info['description']=item['description']=desc[0].extract()
        else:
            info['description']=item['description']=''

        dl=response.xpath('//div[@id="downloadLink"]/div/a/@href')
        if dl:
            info['download_link']=item['download_link']=dl.extract()[0]
        else:
            info['download_link']=item['download_link']=''

        print '[App Details]', json.dumps(info)

        for app in response.xpath('//div[@id="moreFromPublisher"]/ul/li/a/@href'):
            yield Request(app.extract(), self.parseApp)


