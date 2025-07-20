# swag-labs-python-selenium

This project is a sample framework for web UI test automation of the [Swag Labs](https://www.saucedemo.com/) application using Python, Selenium, and pytest.

## Features

- **Page Object Model (POM)**: The project structure is based on the Page Object pattern to improve test maintainability and readability.
- **Pytest**: Used as a framework for writing and running tests.
- **WebDriver Manager**: Automatically manages the download and versions of browser drivers.
- **Layered Architecture**: Clear separation into pages (`pages`), steps (`steps`), and tests (`tests`).
- **Test Case Documentation**: Test cases are documented in `TEST-CASES.md`.

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

## Running Tests by Mark
You can run specific subsets of tests using pytest markers.

For example, to run only tests marked as L1 (level 1 smoke tests):

```bash
pytest -m L1
```

To run multiple marks (e.g., L1 or L2):

```bash
pytest -m "L1 or L2"
```

To exclude a mark:

```bash
pytest -m "not slow"
```

## 📄 Test Reports (HTML)

To generate a visual HTML test report using [pytest-html](https://github.com/pytest-dev/pytest-html), run:

```bash
pytest --html=report.html --self-contained-html
```

* `--html=report.html` – specifies the output file name for the report.
* `--self-contained-html` – embeds CSS/JS directly into the file for portability.

### 💡 Open the Report

After test execution, open `report.html` in any browser to view the full report, including:

* Test status (passed/failed/skipped)
* Error messages
* Screenshot on failure (if `driver` fixture is used)
* Final visited URL (automatically included via `pytest_runtest_makereport`)

### 🧪 Example with Verbosity

```bash
pytest -v --html=report.html --self-contained-html
```

### 🗂️ Save Report to a Folder

To save to a `reports/` directory:

```bash
pytest --html=reports/test-report.html --self-contained-html
```

🔍 Opening the HTML Report
After the tests finish, you will get a report.html file in the current directory.
You can open it in your default browser with:

# macOS
open report.html

# Windows
start report.html

# Linux
xdg-open report.html
Or simply double-click the file in your file manager.

## Linting & Code Formatting

This project uses the following tools for code quality:

- [**black**](https://github.com/psf/black) – opinionated code formatter
- [**flake8**](https://flake8.pycqa.org/) – style and syntax checker
- [**isort**](https://github.com/PyCQA/isort) – import sorter

### Running Linters

To check your code style:

```bash
flake8 .
```


To automatically format your code:
```bash
black .
isort .
```

You can combine them into a pre-commit hook or CI step.


