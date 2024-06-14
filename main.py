import sys
import requests
import re
from bs4 import BeautifulSoup

def main():
    # Get the URL from the command line argument
    url = sys.argv[1]
    # Make a GET request to the URL
    response = requests.get(url,verify=False)
    # Print the status code
    status_code = response.status_code
    if status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        # Find the title tag
        title = soup.title.string
        # Print the title
        print(f"Title: {title}")
        # Find all tags a with href attribute
        links = soup.find_all("a", href=True)
        # Print the links
        for link in links:
            rel_value = link.get('rel')
            if rel_value and 'author' in rel_value:
                print(f"Author: {link.text}")
        # Extracting text from all paragraph tags in content_tag
        paragraph_strings = [p.get_text() for p in soup.find_all("p")]
        # Print the paragraph strings
        print("Paragraphs:")
        for paragraph in paragraph_strings:
            print(paragraph)
        # Extracting the date from the content
        date_pattern = r"(January|February|March|April|May|June|July|August|September|October|November|December)\s([1-9]|[12][0-9]|3[01]),\s([0-9]{4})"
        # Search for the date pattern in the response text
        match = re.search(date_pattern, response.text)
        if match:
            # Print the date of the article
            print(f"Date of article: {match[0]}")
    # If the status code is not 200
    else:
        # Print an error message
        print(f"Failed to fetch the URL: {url}")


if __name__ == '__main__':
    main()