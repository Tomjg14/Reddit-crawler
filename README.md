# Reddit-crawler

This blog will describe how to collect comments from Reddit and how to work with those comments to perform sentiment analysis. The comments were collected as part of a master thesis and were not made publicly available.

This blog contains the following sections:
* [The Data](#the-data)
* [Crawling](#crawling)
* [Preprocessing](#preprocessing)
* [Sentiment Analysis](#sentiment-analysis)

First, I will provide some more information on what data was collected, from where and why. Then I will go into more detail on how the data was crawled. Next, I will explain the exact preprocessing steps that were performed to prepare the data. Finally, I will provide some information on how to perform the sentiment analysis on the data.

## The Data

Before I start explaining what data was collected, I would like to explain for what purpose the data was collected. The data was collected as part of a master thesis that was focussed on the relationship between the fluctuation of several cryptocurrencies and the daily sentiment on social media related to those cryptocurrencies. 

To be able to perform such a study, different sorts of data from different sources should be collected. For example, daily cryptocurrency prices and daily social media comments. This blog will only go into more detail on how the daily social media comments were collected. 

As mentioned above, the social media of interest of this blog is the well known forum site named Reddit. Reddit is 'a source for what's new and popular on the web'. It is a site were the users provide the content and decide via voting what is good or bad.<sup>[1](#reddit-footnote)</sup>

The nice thing about Reddit is that there exist some sort of order in the content available. Every different topic can be subcategorized into so-called 'subreddits'. These are different parts of the website dedicated to one general topic. Like for example the different cryptocurrencies like Bitcoin or Ethereum. 

There exist different subreddits dedicated to those cryptocurrencies and some even have daily discussions. These daily discussions are opened on each new day and contain discussions on topics related to that day. These discussions might be on price speculations or the technology behind the cryptocurrency. There might even be discussions on material found on other social media, like e.g. tweets or posts made on Facebook. 

The well structured and publicly available content is also one of the main reasons why Reddit was chosen as source for the data instead of Facebook or Twitter. Next to the fact that the Reddit API was easier to use. Because the study was interested in data from months ago, it was quickly decided that Twitter and Facebook were not suitable. With Facebook the reason was that messages are often only shared between friends or group members of often private groups and there was no quarantee that this was on a daily basis. With Twitter the reason was that their API only allowed to collect tweets from a few weeks ago. This left us with Reddit as the main source of data. 

<a name="reddit-footnote">1</a>: https://www.reddit.com/wiki/faq
## Crawling

## Preprocessing

## Sentiment Analysis
