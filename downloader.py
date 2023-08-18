from bs4 import BeautifulSoup
import requests

import os
import requests
import shutil

def get_images(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", {"class": "imgboxart"})
    links = []
    for div in results:
        img_tag = div.find('img')
        if img_tag:
            link = img_tag['src']
            link = link.replace("scale_small", "scale_large")
            links.append(link)
    return links


def download_image(output_folder, list_of_images):
    total_images = len(list_of_images)
    for index, link in enumerate(list_of_images):
        try:
            response = requests.get(link, stream=True)
            if response.status_code == 200:
                # Extract the filename from the URL
                reverse_index = total_images - index
                # filename = os.path.join(output_folder, os.path.basename(link))
                filename = os.path.join(output_folder, f"{reverse_index:03}.jpg")
                
                # Save the image
                with open(filename, 'wb') as file:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, file)
                
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {link} (Status code: {response.status_code})")
        except Exception as e:
            print(f"An error occurred while downloading: {link} - {str(e)}")