# Data Analysis Tool
An open-source Python script for data analysis and exploration using pandas, presented as a web application using Flask.

## Overview
This tool provides a convenient way to perform exploratory analysis on tabular data. Leveraging the power of pandas, it offers insights such as descriptive statistics, data information, and a preview of the dataset through the first few rows. The application is hosted using Flask, allowing users to interact with it through a web browser.

## Features
- Descriptive Statistics: Quickly obtain basic statistics for numerical columns.
- Data Information: Get an overview of the dataset, including column names, non-null counts, and data types. If there are missing values, it will display detailed information; otherwise, it will indicate that there are no missing values.
- Preview Data: View the first few rows of the dataset to understand its structure.

## Getting Started
### Prerequisites
- Python installed
- Required libraries: pandas, Flask

### Installation
`pip install pandas Flask`

### Usage
1. Clone the repository:

`git clone https://github.com/niladrigithub/data-analysis-tool.git`

2. Navigate to the project directory:

`cd data-analysis-tool`

3. Run the Flask application:

`python app.py`

4. Open your web browser and visit `http://127.0.0.1:5000/`

5. Enter the full path to your CSV file in the provided form and click "Explore Data."

## Hosting on the Web
This application can be deployed to a web server to make it accessible to a broader audience. Choose a hosting platform and follow their deployment guidelines.

## Contributing
Contributions are welcome! If you have ideas for improvements or encounter issues, please submit a pull request or open an issue.

## License
This project is licensed under the MIT License - see the [License](https://github.com/niladrigithub/data-analysis-tool/blob/main/LICENSE) file for details.
