# Bitcoin Tweet Classification

This project aims to classify tweets related to Bitcoin into different categories such as "spam", "bot", or "human". It also analyzes the sentiment and emotions expressed in these tweets. The project is structured to facilitate data processing, analysis, and visualization.

## Project Structure

```
bitcoin-tweet-classification/
├── data/
│   ├── raw/                  # Contains raw data files
│   └── processed/            # Contains cleaned and processed data files
├── notebooks/                 # Jupyter Notebooks for analysis
│   └── data_cleaning_and_analysis.ipynb
├── src/                      # Source code for the project
│   ├── __init__.py           # Indicates that src is a package
│   ├── data_cleaning.py      # Functions for cleaning data
│   ├── api_requests.py       # Functions for handling API requests
│   └── visualization.py       # Functions for visualizing data
├── tests/                    # Unit tests for the project
│   └── test_data_cleaning.py  # Tests for data cleaning functions
├── requirements.txt          # Project dependencies
├── .gitignore                # Files and directories to ignore in Git
└── README.md                 # Project documentation
```

## Installation

To set up the project, clone the repository and install the required packages:

```bash
git clone <repository-url>
cd bitcoin-tweet-classification
pip install -r requirements.txt
```

## Usage

1. **Data Preparation**: Place your raw data files in the `data/raw` directory. The data cleaning and processing will be handled in the `src/data_cleaning.py` script.

2. **Data Cleaning and Analysis**: Use the Jupyter Notebook located in `notebooks/data_cleaning_and_analysis.ipynb` for exploratory data analysis and to visualize the data cleaning process.

3. **API Requests**: The `src/api_requests.py` script contains functions to interact with the necessary APIs for fetching additional data or processing the tweets.

4. **Visualization**: Use the functions in `src/visualization.py` to create visual representations of the data and results.

5. **Testing**: Run the unit tests located in `tests/test_data_cleaning.py` to ensure that the data cleaning functions work as expected.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.