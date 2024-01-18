import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# this is a function to fetch images in "google image" 
def fetch_images(query, max_links_to_fetch, webdriver_path):
    options = Options()
    options.binary_location = webdriver_path
    #service = Service(webdriver_path)
    driver=webdriver.Chrome(options=options)

    


   # search_box = driver.find_element_by_xpath("//textarea[@class='gLFyf']")
   # search_box.send_keys(query)
   # search_box.send_keys(Keys.ENTER)


#-----------------------------------------------------------------------------------------
   # dont forget to change the url here for your specified task
   #  the purpose of fill in it with link and not automated with a query to search for is that i had a complicated task, i could't find the best prompts
   #  so as a quik solution i try a bunch of prompts untill
   #  i find the accurate result then i copy past the link here to guarantis good retrived images (my task)

   
    driver.get('https://www.google.com/search?q=coriandre+culinaire&tbm=isch&ved=2ahUKEwj9iJzb8f2CAxWYjycCHanCBQcQ2-cCegQIABAA&oq=coriandre+culinaire&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BAgAEB46BggAEAgQHlDFD1j4H2D4ImgAcAB4AIABbogB3QqSAQQxLjEymAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=9QVyZb26BZifnsEPqYWXOA&bih=703&biw=1536')
   



    image_urls = set()
    image_count = 0
    results_start = 0

    while image_count < max_links_to_fetch:
        thumbnail_results = driver.find_elements(By.CSS_SELECTOR,"img.rg_i.Q4LuWd")
        number_results = len(thumbnail_results)

        for img in thumbnail_results[results_start:number_results]:
            try:
                img.click()
                time.sleep(2)
                actual_images = driver.find_elements(By.CSS_SELECTOR,'img.sFlh5c.pT0Scc.iPVvYb')
                for actual_image in actual_images:
                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))
                        image_count += 1
            except Exception as e:
                print(e)
        results_start = len(thumbnail_results)
        if len(image_urls) >= max_links_to_fetch:
            break

    driver.quit()
    return image_urls
# this is a function to download fetched images from "google image" 
def download_images(folder_path, file_prefix, urls):
    for i, url in enumerate(urls):
        try:
            response = requests.get(url)
            with open(os.path.join(folder_path, f"{file_prefix}_{i+1}.jpg"), "wb") as file:
                file.write(response.content)
        except Exception as e:
            print(f"Error downloading image {i+1}: {e}")
# i was working with a query variable to make fetching easy but its not always good to find accurate prompts, this is what i was talking about above in fetching method 
query = 'corianderCulinaire'  # Replace 'your search query' with the term you want to search for
max_links = 90  # Number of image links you want to fetch
folder = 'image_folder_coriander'  # Folder to save the images
# Path to your Chrome webdriver make sure to install the accurate webdriver depending on your navigator version
webdriver_path = 'C:\\Users\\hp\\Desktop\\seleniumScrape\\chrome-win64\\chrome.exe'  

# Fetch image URLs
image_links = fetch_images(query, max_links, webdriver_path)

# Download images
download_images(folder, query, image_links)
