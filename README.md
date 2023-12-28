# beautifulSpaghetti

## Overview

**beautifulSpaghetti** is a Python application designed for web scraping, providing a fun and interactive way to extract data from websites. The application incorporates ASCII art, user authorization, and a simulated loading experience to enhance user engagement.

## Features

- **ASCII Art Title**: The program starts with an eye-catching ASCII art title, adding a touch of creativity.
  
- **Authorization**: Users are prompted to confirm their authorization before proceeding with the web scraping process.

- **Fake Loading**: A simulated loading animation creates a visually appealing experience while the program prepares for scraping.

- **User Input (Website Link)**: Users input the link of the website they wish to scrape, ensuring flexibility and ease of use.

- **Folder Creation**: The application creates a structured folder system within the "Documents" directory to neatly organize scraped HTML files, images, and tables.

- **Web Scraping Logic**: Utilizing BeautifulSoup, the program enables users to choose whether to save HTML files, images, and tables from the specified website.

- **Restart Mechanism**: In case users decide not to save any data, the program gracefully restarts the scraping process.

- **Graceful Error Handling**: The program handles exceptions carefully and informs users in case of errors during the scraping process.

## Downloading the Project from Git

To download and use the **beautifulSpaghetti** project from Git, follow these steps:

### Step 1: Clone the Repository

Open your terminal and run the following command to clone the repository to your local machine:

```bash
git clone https://github.com/dangelodavide/beautifulSpaghetti.git
```

### Step 2: Navigate to the Project Directory

Move into the project directory using the following command:

```bash
cd beautifulSpaghetti
```

### Step 3: Run the Program

Now, you can run the program using:

```bash
python beautifulSpaghetti.py
```

Follow the on-screen instructions to input the website link and proceed with the web scraping process.

Enjoy using **beautifulSpaghetti**! If you encounter any issues or have suggestions, feel free to open issues or contribute to the project.

## Usage

1. Run the program.
2. Input the link of the website you wish to scrape when prompted.
3. Confirm your authorization to use the program.
4. Follow on-screen instructions to choose the type of data you want to save (HTML files, images, and/or tables).
5. The scraped data will be organized in the "beautifulSpaghetti" folder within your "Documents" directory.

## Disclaimer

**Warning:** Web scraping may violate the terms of service of some websites. Ensure that you have the legal right to scrape data from the target website. Use this application responsibly and only with proper authorization.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
