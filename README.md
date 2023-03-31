# Article Extractor(GUI)
This is a Python script that creates a simple GUI window to allow users to enter a URL of a website and scrape certain information from it, such as the article title, the main image, embedded videos, meta description, meta tags, and article text. The extracted information is displayed in a text box within the GUI.

### Installation
To use this script, you need to have Python 3 installed, as well as the following libraries:

requests
chardet
BeautifulSoup

You can install these libraries using pip by running the following command in your terminal:

```python3
pip3 install requests chardet beautifulsoup4
```

### Usage
To run the script, simply execute the following command in your terminal:

```python3
python3 web_scraper_gui.py
```

This will open the GUI window. To scrape a website, enter the URL in the URL entry field and click the "Scrape" button. The script will send a request to the webpage and parse its HTML content using BeautifulSoup. The extracted information will be displayed in the text box below.

Note that the script only works with websites that have a well-defined structure and follow common practices. Some websites may have different HTML structures or may block scraping attempts, in which case the script may not work properly.


### Credits
This script was created by Abdalrahman. If you have any questions or suggestions, please feel free to contact me at abdalrahman.gamal.m@gmail.com
