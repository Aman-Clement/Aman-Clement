import datetime
import json
from bs4 import BeautifulSoup
from selenium import webdriver

today = datetime.date.today()
day = today.day

today = datetime.datetime.now()
month = today.strftime("%B")




driver = webdriver.Edge()

URL = f"https://www.britannica.com/on-this-day/{month}-{day}"
driver.get(URL)
soup = BeautifulSoup(driver.page_source, 'html.parser')
Featured_Event = soup.find('div',attrs={'class':'otd-featured-event col-100 col-sm-50'})

Heading_Text = Featured_Event.find('div',attrs={'class':'title font-18 font-weight-bold mb-10'}).text
Body_Text = Featured_Event.find('div',attrs={'class':'description font-serif'}).text

 
if Body_Text and Heading_Text:
    # Load the response into a json object
    OTD = json.dumps(Body_Text)
    quoteTitle = json.dumps(Heading_Text)
    
    # In case of receiving multiple quotes,
    # we will pick the first one
    mainQuote = OTD
    OTDtitle = quoteTitle
else:
    print("Error")
 
 
# Reading the readme file
with open("README.md", mode="r", encoding="utf8") as f:
    readmeText = f.read()
 

# Title OTD
openingTagTitle = "<h3 OTD"
closingTagTitle = "</h3 OTD"

startIndexTitle = readmeText.index(openingTagTitle)
endIndexTitle = readmeText.index(closingTagTitle)

quoteTitleMarkdown = "<h2 head>" + OTDtitle + "." + "</h2 head>"
 
quoteMarkdown = "<h3 quote align='center'>" + mainQuote + "." + "</h3 quote>"
 
content = readmeText[startIndexTitle +
                     len(openingTagTitle): endIndexTitle]
newBody = (
    readmeText[:startIndexTitle]
    + openingTagTitle 
    + quoteTitleMarkdown
    + quoteMarkdown
    + closingTagTitle
    + readmeText[endIndexTitle + len(closingTagTitle) + 1:]
)


newContent =   newBody
 
# Writing new Quote into readme file
readme_file = open("README.md",
                   mode="w", encoding="utf8")
readme_file.write(newContent)
