import requests
import chardet
from bs4 import BeautifulSoup
import tkinter as tk

def scrape_website():
    # Get the URL entered by the user
    url = url_entry.get()

    # Send a request to the webpage and get its HTML content
    response = requests.get(url)
    encoding = chardet.detect(response.content)['encoding']
    response.encoding = encoding
    html_content = response.text

    # Parse the HTML content using BeautifulSoup and lxml parser
    soup = BeautifulSoup(html_content, 'lxml')

    # Extract the title of the article
    article_title = soup.head.title.text if soup.head.title else ''

    # Extract the main image of the article
    article_image = soup.find('meta', property='og:image')['content'] if soup.find('meta', property='og:image') else ''

    # Extract any YouTube/Vimeo movies embedded in the article
    embedded_videos = soup.find_all('iframe', {'src': ['https://www.youtube.com/embed/', 'https://player.vimeo.com/video/']})

    # Extract self-embedded videos in the article
    self_embedded_videos = soup.find_all('video', {'controls': True, 'src': True})
    if not self_embedded_videos:
        self_embedded_videos = soup.find_all('video_wrapper', {'controls': True, 'src': True})

    if not self_embedded_videos:
        self_embedded_videos = soup.find_all('iframe[data-src*=https://youtube.com/embed]')

    # Extract the meta description of the article
    meta_description = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else ''

    # Extract the meta tags of the article
    meta_tags = [meta['content'] for meta in soup.find_all('meta', attrs={'property': 'article:tag'})]

    # Extract the cleaned text of the article
    article_text = '\n\n'.join([p.get_text() for p in soup.find_all('p') if len(p.get_text()) > 0])

    # Display the extracted information in the text box
    results_text.configure(state='normal')
    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, f"Article Title: {article_title}\n")
    results_text.insert(tk.END, f"Article Image: {article_image}\n")
    results_text.insert(tk.END, f"Embedded Videos: {embedded_videos}\n")
    results_text.insert(tk.END, f"Self-Embedded Videos: {self_embedded_videos}\n")
    results_text.insert(tk.END, f"Meta Description: {meta_description}\n")
    results_text.insert(tk.END, f"Meta Tags: {meta_tags}\n")
    results_text.insert(tk.END, f"Article Text:\n{article_text}")
    results_text.configure(state='disabled')

# Create the GUI window
root = tk.Tk()
root.title("Web Scraper")

# Create the URL entry field
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Create the Scrape button
scrape_button = tk.Button(root, text="Scrape", command=scrape_website)
scrape_button.pack()

# Create the results text box
results_text = tk.Text(root, state='disabled', wrap='word', height=30, width=80)
results_text.pack()

# Start the GUI main loop
root.mainloop()
