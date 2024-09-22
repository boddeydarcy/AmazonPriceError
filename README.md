# Amazon Price Error Finder
This will run on Amazon AWS, quite bittersweet really, and will run on an EC2 instance along with a lambda function and SNS email notifications when it finds something.

As I am currently in the market for some new golf clubs this will scrape Amazon's pages with the keyword of golf and then will have a list of brand names that will be used to cross check wether to scrape the info eg. Callaway, Taylormade, Titleist.

Using an AWS Lambda function I can make this scraper run every hour or however long and then will notify my email if it finds anything related to golf and with the keywords that has a discount of greater than 95%. This will typically mean that there is a price error. Price errors aren't necessarily going to work as depending on the seller they will catch on and realise their mistake, but with amazon alot of the time these errors slip through their system.
