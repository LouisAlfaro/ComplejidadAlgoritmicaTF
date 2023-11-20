# Trabajo Final para el curso de Complejidad Algorítmica UPC

Para este proyecto usamos grafos no dirigidos y usamos las oponderaciones para representar las relaciones entre animes y asi tener la posibilidad de recomendar animes.

## Installation

To install the application, you need to have Python 3.6 or higher installed on your machine. You also need to have Poetry installed. If you don't have Poetry, you can install it by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

Once you have Python and Poetry installed, you can install the application by cloning the repository and installing the dependencies:

```bash
git clone https://github.com/Diego22rct/TrabajoFinal-Complejidad-Algoritmica-Backend.git
cd TrabajoFinal-Complejidad-Algoritmica-Backend
poetry install
```

## Usage

To run the application, use the following command:

```bash
poetry run uvicorn app.main:app --reload
```

This will start the application on `http://localhost:8000`.

## Testing

To run the tests, use the following command:

```bash
poetry run pytest
```

## Contributing

If you want to contribute to the project, please create a fork of the repository, make your changes, and create a pull request.

## License

This project is licensed under the terms of the MIT license.