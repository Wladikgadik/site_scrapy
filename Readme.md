# Book scraper

Book scraper is a introductory assignment based on scrapy tutorial template.


### Quick Start

Book scraper requires [Scrapy](https://scrapy.org/) library to run.

For Windows:

    > cd \site_scrapy\tutorial
    > scrapy crawl quotes

For Linux:

    $ cd \site_scrapy\tutorial
    $ scrapy crawl quotes

But thus the names of books can be seen only in the stdout mixed with log.
You can save output in file. These formats are supported out of the box:
   * JSON
   * JSON lines
   * CSV
   * XML

Use -o flag:

    scrapy crawl quotes -o filename.json

This command will save the output to filename.json in the project folder