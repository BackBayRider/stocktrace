#download securities list,statistics data,history price data

if __name__ == '__main__':	
	from download import download
	from stocktrace.util import settings
	download(False,True,True,stockList=settings.STOCK_LIST);

			
