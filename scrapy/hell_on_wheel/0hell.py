import scrapy
import codecs
import time

result_file = codecs.open('result.txt', mode='w',  encoding="utf-8")
link_file  = open('link.txt', encoding='utf-8', mode='r')


class QuotesSpider(scrapy.Spider):
    name = "rfa"

    def start_requests(self):
        urls = [
            'https://www.rfa.org/khmer/news/history/khmer-history-in-pre-history-12152009041732.html' ,
            'https://www.rfa.org/khmer/news/history/agriculture-system-in-pre-era-12162009050201.html' ,
            'https://www.rfa.org/khmer/news/history/history-on-organizing-commune-in-pre-era-12162009050945.html' ,
            'https://www.rfa.org/khmer/news/history/History-Part-1-Geography-01212014231202.html' ,
            'https://www.rfa.org/khmer/news/history/Cambodian-Pre-History-and-the-1st-Indian-Influence-01292014000728.html' ,
            'https://www.rfa.org/khmer/news/history/The-Phnom-Empire-02052014001005.html' ,
            'https://www.rfa.org/khmer/news/history/second-indian-influence-02112014235937.html' ,
            'https://www.rfa.org/khmer/news/history/Civilization-of-the-Phnom-Empire-02192014001358.html' ,
            'https://www.rfa.org/khmer/news/history/The-Khmer-Kings-in-Chenla-Period-02262014024902.html' ,
            'https://www.rfa.org/khmer/news/history/cambodia-broke-into-two-in-pre-angkor-03122014011849.html' ,
            'https://www.rfa.org/khmer/news/history/Khmer-civilization-during-Chenla-period-03192014034643.html' ,
            'https://www.rfa.org/khmer/news/history/The-first-King-of-Angkor-and-Devaraja-03262014011051.html' ,
            'https://www.rfa.org/khmer/news/history/king-during-angkor-era-04022014010400.html' ,
            'https://www.rfa.org/khmer/news/history/the-kings-of-angkor-continued-04092014005953.html' ,
            'https://www.rfa.org/khmer/news/history/activities-of-kings-during-angkor-04232014030656.html' ,
            'https://www.rfa.org/khmer/news/history/the-kings-of-angkor-continued-05142014024643.html' ,
            'https://www.rfa.org/khmer/news/history/King-Suriyavarman-II-05212014010233.html' ,
            'https://www.rfa.org/khmer/news/history/after-king-Suriyavarman-II-05282014044401.html' ,
            'https://www.rfa.org/khmer/news/history/The-Great-King-Jayavarman-VII-The-Builder-of-Bayon-Temple-06042014004658.html' ,
            'https://www.rfa.org/khmer/news/history/the-king-of-angkor-continued-06112014034739.html' ,
            'https://www.rfa.org/khmer/news/history/the-king-of-angkor-continued-06252014003352.html' ,
            'https://www.rfa.org/khmer/news/history/The-Cucumber-King-Fact-or-Fiction-07022014005309.html' ,
            'https://www.rfa.org/khmer/news/history/student-demonstration-07062014054539.html' ,
            'https://www.rfa.org/khmer/news/history/cambodia-under-thailand-07152014032141.html' ,
            'https://www.rfa.org/khmer/news/history/cambodia-under-thailand-07222014012554.html' ,
            'https://www.rfa.org/khmer/news/history/king-phnhea-yat-07292014053512.html' ,
            'https://www.rfa.org/khmer/news/history/The-abandon-of-Angkor-and-the-establishment-of-the-new-capital-in-Phnom-Penh-08052014013306.html' ,
            'https://www.rfa.org/khmer/news/history/angkor-civilization-09022014011516.html' ,
            'https://www.rfa.org/khmer/news/history/cambodia-after-angkor-and-the-games-of-throne-09092014030025.html' ,
            'https://www.rfa.org/khmer/news/history/thai-intervention-to-cambodian-conflict-09162014013206.html' ,
            'https://www.rfa.org/khmer/news/history/preah-bat-srey-soknbath-09302014032646.html' ,
            'https://www.rfa.org/khmer/news/history/sdech-kan-10072014061501.html' ,
            'https://www.rfa.org/khmer/news/history/preah-chan-rachea-10142014055456.html' ,
            'https://www.rfa.org/khmer/news/history/the-construction-of-new-capitbal-long-vek-10212014035331.html' ,
            'https://www.rfa.org/khmer/news/history/King-Boraminthoreachea-10282014041145.html' ,
            'https://www.rfa.org/khmer/news/history/the-arrival-of-europeans-to-cambodia-11102014234929.html' ,
            'https://www.rfa.org/khmer/news/history/Relationship-with-Europeans-11252014052432.html' ,
            'https://www.rfa.org/khmer/news/history/the-king-of-long-vek-12022014040255.html' ,
            'https://www.rfa.org/khmer/news/history/the-collapse-of-lung-vek-12092014034234.html' ,
            'https://www.rfa.org/khmer/news/history/king-rama-choeung-prey-12162014020301.html' ,
            'https://www.rfa.org/khmer/news/history/king-ponhea-ton-12232014025101.html' ,
            'https://www.rfa.org/khmer/news/history/The-Kings-Ponhea-On-and-Chaovea-Ponhea-Nhom-01062015005520.html' ,
            'https://www.rfa.org/khmer/news/history/King-Srey-Soriyo-Por-01132015015202.html' ,
            'https://www.rfa.org/khmer/news/history/king-chey-chetha-ii-01202015003517.html' ,
            'https://www.rfa.org/khmer/news/history/King-Preah-Reach-Samphea-and-the-Tragedy-with-the-Royal-Palace-02032015004731.html' ,
            'https://www.rfa.org/khmer/news/history/Preak-Ponhea-Nou-and-Preah-Ang-Nun-02242015035414.html' ,
            'https://www.rfa.org/khmer/news/history/Angchan-Ibrahim-the-first-Muslim-King-of-Cambodia-03032015023951.html' ,
            'https://www.rfa.org/khmer/news/history/king-ang-so-and-srey-chey-chedh-03172015033210.html' ,
            'https://www.rfa.org/khmer/news/history/king-preah-keo-va-ang-chi-03242015024533.html' ,
            'https://www.rfa.org/khmer/news/history/Kings-Chechesda-Ang-Su-and-Preah-Ang-Yang-03312015033207.html' ,
            'https://www.rfa.org/khmer/news/history/Kings-Angsou-and-Ang-Im-05122015041417.html' ,
            'https://www.rfa.org/khmer/news/history/Kings-Thomareachea-Ramathipadey-and-Angsou-06022015055048.html' ,
            'https://www.rfa.org/khmer/news/history/Preah-Srey-Thomareachea-Thipadey-06232015064654.html' ,
            'https://www.rfa.org/khmer/news/history/Preah-Keohva-Ang-Im-2nd-Reign-06302015030334.html' ,
            'https://www.rfa.org/khmer/news/history/King-Sedha-Thireach-and-Keo-Va-Ang-Im-07212015043435.html' ,
            'https://www.rfa.org/khmer/news/history/King-Sedhathireach-2nd-reign-07282015043528.html' ,
            'https://www.rfa.org/khmer/news/history/king-thomreachea-thomareacheaangim-and-ang-tong-08112015062650.html' ,
            'https://www.rfa.org/khmer/news/history/King-Preah-Srey-Chey-Ched-Ang-Snguon-08182015033309.html' ,
            'https://www.rfa.org/khmer/news/history/Samdech-Preah-Ramathipadey-Preah-Ang-Tong-2nd-reign-08252015003417.html' ,
            'https://www.rfa.org/khmer/news/history/King-Odhaya-Reachea-Ang-Ton-09012015051255.html' ,
            'https://www.rfa.org/khmer/news/history/King-Ang-Nun-Preah-Ream-09082015061102.html' ,
            'https://www.rfa.org/khmer/news/history/Preah-Ang-Eng-09152015072445.html' ,
            'https://www.rfa.org/khmer/news/history/khmerkrom-call-govt-to-vn-for-khmerkrom-learning-01282018092003.html' ,
            'https://www.rfa.org/khmer/news/history/khao-i-dang_camp-04032018073133.html' ,
            'https://www.rfa.org/khmer/news/history/Khmer-krom-celebrate-losing-aniversary-05302018042349.html' ,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        head =  response.css("h1::text").extract()[0]
        texts = response.css("#storytext p::text")
        i = 10
        result_file.write( '***********' + '\n' + str(i)+ '\t' + head + '\n' + '\n' )
        for text in texts :
            i = i + 1
            result_file.write( str(i)+ '\t' + text.extract() + '\n')