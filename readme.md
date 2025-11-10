 # Application Stomail

A simple email sending application built using Python 2.7+ and SQLite. This project is designed to facilitate the sending of emails from your local machine.

## Requirements

- Python 2.7 or higher (Python versions 3.0, 3.1, 3.2, 3.3, and 3.4 are not supported)
- SQLite3 database

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Configuration

The configuration file `config.py` contains the necessary settings for the application. It includes the connection URI to the SQLite database and the hashes of the installed packages.

## Usage

To create a new session, you can use the following function:

```python
from config import make_session

with make_session() as session:
    # Your code here
    pass
```

This will return a SQLAlchemy session that can be used to interact with the database.

## Development

For development purposes, you can modify the `config.py` file or create a new `develop` section in it to include additional packages and their respective hashes for testing.

## Acknowledgments

This project utilizes the following libraries:

- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and Object Relational Mapping (ORM) system.

Enjoy using Application Stomail! If you encounter any issues or have suggestions, please open an issue. Contributions are always welcome.