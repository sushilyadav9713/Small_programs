import requests
from bs4 import BeautifulSoup
import os

# User-Agent header to simulate a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"
}


# Function to search for a book and return the page URL
def search_zlibrary(book_title):
    search_url = (
        "https://z-lib.is/s"  # Example URL for search (replace with actual if changed)
    )
    params = {"q": book_title}

    response = requests.get(search_url, headers=HEADERS, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        # Parse the search results and return the first book URL
        book_link = soup.find(
            "a", class_="book-item-link"
        )  # Update this based on actual structure
        if book_link:
            return book_link["href"]
    return None


# Function to download a book by visiting the download page
def download_book(book_url, download_folder="downloads"):
    # Ensure download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    response = requests.get(book_url, headers=HEADERS)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        # Find download link (You need to inspect ZLibrary's actual download link structure)
        download_link = soup.find(
            "a", class_="download-button"
        )  # Update based on actual structure
        if download_link:
            file_url = download_link["href"]
            file_name = file_url.split("/")[-1]
            download_file(file_url, os.path.join(download_folder, file_name))
        else:
            print("No download link found.")
    else:
        print(f"Failed to load the book page: {book_url}")


# Function to download file from URL
def download_file(file_url, file_name):
    response = requests.get(file_url, stream=True, headers=HEADERS)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_url}")


# Main bot logic
def zlibrary_bot(book_title, download_folder="downloads"):
    print(f"Searching for '{book_title}' on ZLibrary...")
    book_page_url = search_zlibrary(book_title)

    if book_page_url:
        print(f"Book found: {book_page_url}")
        print(f"Downloading book...")
        download_book(book_page_url, download_folder)
    else:
        print(f"No book found for '{book_title}'.")


if __name__ == "__main__":
    book_title = "Python Programming"  # Example search query
    zlibrary_bot(book_title, download_folder="books")
