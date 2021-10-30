import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
from scrapy.utils.trackref import format_live_refs
import pathlib
import os
class QuotesSpider(scrapy.Spider):
  name = 'openinsider'
  custom_settings = {
        'FILE_SYSTEM_DB':str(pathlib.Path(__file__).resolve().parents[1])+"/FILE-DB" ,
        
    }
  
  
  
  def parse(self, response):
    index=response.xpath("//table[contains(@class,'tinytable')] //th/h3/text()").getall()
    rows=response.xpath("//table[contains(@class,'tinytable')] //tr")
    lst=[]
    Ticker=None
    for r in rows:
      dt={}
      cols=r.xpath(".//td")
      
      for i,col in enumerate(cols):
        if i ==1:
          dt[index[i]]=str(col.xpath(".//div//a/text()").get())
        
        elif i == 2:
          dt[index[i]]=col.xpath(".//div/text()").get()
        
        elif i ==3:
          dt[index[i]]=col.xpath(".//b//a/text()").get()
          Ticker=col.xpath(".//a/text()").get()
        
        elif i == 4:
          dt[index[i]]=col.xpath(".//a/text()").get()
        
        else:
          dt[index[i]]=col.xpath("text()").get()
        
      lst.append(dt)

    if Ticker:
      
      #dataframe created
      df=pd.DataFrame.from_dict(lst)
      
      #directories
      assets_dir=self.settings.get("FILE_SYSTEM_DB")
      index_dir=assets_dir +"/" +Ticker[0]
      symbol_dir=index_dir + '/' + Ticker
      
      #index directory check and creation
  
      if not os.path.isdir(index_dir):
          os.path.join(index_dir) 
          os.mkdir(index_dir) 
    # ticker dir check and creation
      if not os.path.isdir(symbol_dir):
          os.path.join(symbol_dir) 
          os.mkdir(symbol_dir)
          
      directory=symbol_dir+"/"+Ticker+".csv"
      
      if not os.path.isfile(directory):

          df.to_csv(directory)
      else:
        current_rec_df=df.read_csv(directory)
        df=current_rec_df[current_rec_df[""]]
        df.to_csv(directory, mode='a', header=False)
          
    







  
def create_urls():
 
  sp500=str(pathlib.Path(__file__).resolve().parents[1])+"/FILE-DB/sandp500.csv"
  assets=pd.read_csv(sp500)
  symbols=assets["Symbol"]
  return ["http://openinsider.com/screener?s={}&fd=0&td=0&xp=1&xs=1&vl=&sortcol=0&cnt=1000&page=1".format(s) for s in symbols]








urls=create_urls()
pr = CrawlerProcess()
pr.crawl(QuotesSpider, start_urls=urls)
pr.start()