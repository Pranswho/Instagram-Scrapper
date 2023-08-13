from src.InstagramScrapper import InstagramScrapper
import os
if __name__ == '__main__':

    print("Starting Social Media Scrapper...")
    keyword = str(input("Enter keyword to search for: "))
    insta_limit = int(input("Enter how many posts to scrape from Instagram: "))


    scrapper = InstagramScrapper()
    scrapper.Scrape_Instagram(tag=keyword,limit=insta_limit,browser='chrome') 
