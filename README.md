# Web Scraping Google Images

## Overview

This repository contains a Python script for web scraping Google Images using Selenium WebDriver and Requests. The script automates the process of fetching and downloading images from Google search results.

## Prerequisites

Before using the script, make sure you have the following installed:

- Python 3
- Selenium WebDriver
- Requests library
- ChromeDriver (or the WebDriver for your preferred browser)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/YGTRAY/webScraping.git
    ```


## Usage 
(check code comments for more understanding)

1. Ensure you have the WebDriver executable (e.g., ChromeDriver) installed and available in your system's PATH.
2. check for the best prompts according to your task then get its Link
3. modify the code according to your specific link 
4. Run the script:

    ```bash
    python googleImageScraping.py
    ```


3. The script will use Selenium to automate the browser, perform the Google search, and download images using Requests.

## Customization

Feel free to customize the script according to your needs. You can modify the search parameters, browser choice, file download location, or implement additional features.


## Acknowledgments
- If you are using Chrome version 115 or newer, please consult [the Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
- This page provides convenient [JSON endpoints](https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json) for specific ChromeDriver version downloading.
- [Selenium WebDriver](https://www.selenium.dev/documentation/en/)
- [Requests library](https://docs.python-requests.org/en/latest/)

Happy Web Scraping!

