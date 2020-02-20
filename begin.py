from scrapy import cmdline

if __name__ == "__main__":
    args = "scrapy crawl weatherforecast_Spider".split()
    cmdline.execute(args)