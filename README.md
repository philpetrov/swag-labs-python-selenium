# swag-labs-python-selenium

This project is a sample framework for web UI test automation of the [Swag Labs](https://www.saucedemo.com/) application using Python, Selenium, and pytest.

## Features

- **Page Object Model (POM)**: The project structure is based on the Page Object pattern to improve test maintainability and readability.
- **Pytest**: Used as a framework for writing and running tests.
- **WebDriver Manager**: Automatically manages the download and versions of browser drivers.
- **Layered Architecture**: Clear separation into pages (`pages`), steps (`steps`), and tests (`tests`).

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/philpetrov/swag-labs-python-selenium
    cd swag-labs-python-selenium
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

To run all tests, execute the following command in the project's root directory:
```bash
pytest
```
