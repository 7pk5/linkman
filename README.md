
---

# Link Management App

## Overview

The Link Management App is a Streamlit-based web application designed to help users manage and organize links along with their descriptions. It allows users to add new links, fetch descriptions from the web, view existing links, and download the updated link data as an Excel spreadsheet.

## Features

- **Add Links:** Users can enter a new link and automatically fetch its webpage title and description.
- **Check Duplicates:** The app checks if a link from the same domain already exists in the database to avoid duplication.
- **View Current Links:** Displays a table of all currently stored links and their descriptions.
- **Download Data:** Provides a download button to export the current link data as an Excel spreadsheet.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your/repository.git
   cd repository-folder
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   ```bash
   streamlit run app.py
   ```


## Usage

- **Login:** The app does not currently require login credentials. Simply access the application to start managing links.
- **Add a New Link:** Enter a URL into the input field and click submit. The app will fetch and display the title and description of the webpage.
- **View Existing Links:** The app displays a table showing all currently stored links and their descriptions.
- **Download Data:** Click the "Download Excel" button to download the current link data as an Excel spreadsheet (`links.xlsx`).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the [GitHub repository](https://github.com/your/repository).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

