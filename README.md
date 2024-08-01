# Telegram Bot Project

## Overview

This project is a Telegram bot built using the following technologies:
- **Python**: The programming language used.
- **GitHub**: For version control and repository management.
- **Linux**: The operating system where the bot is developed and tested.
- **PostgreSQL**: A relational database used for storing any persistent data.
- **Redis**: An in-memory data structure store, used for caching or other temporary data needs.
- **Celery**: A distributed task queue used for background task processing.
- **Aiogram**: A modern and fully asynchronous framework for interacting with the Telegram Bot API.
- **Django**: A high-level Python web framework used for web-related components.

## Installation

### Prerequisites

- Python 3.12 or later
- PostgreSQL
- Redis
- Celery

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install Pipenv**

   If you don't have `pipenv` installed, you can install it using pip:

   ```bash
   pip install pipenv
   ```

3. **Install Dependencies**

   With `pipenv`, you can install the dependencies listed in `Pipfile`:

   ```bash
   pipenv install
   ```

   To install the development dependencies (if any):

   ```bash
   pipenv install --dev
   ```

4. **Create a `.env` File**

   In the root directory of the project, create a `.env` file and add your Telegram Bot API token:

   ```dotenv
   BOT_TOKEN=your_telegram_bot_token_here
   ```

5. **Configure Database and Redis**

   Ensure that PostgreSQL and Redis are properly configured and running. Update the database and Redis settings in your Django settings file (`settings.py`).

6. **Run Migrations (If using Django)**

   If your project uses Django, run the following command to apply migrations:

   ```bash
   pipenv run python manage.py migrate
   ```

7. **Start the Bot**

   Use `pipenv` to run the bot:

   ```bash
   pipenv run python bot.py
   ```

## Features

### Task 1: Basic Commands

- **/start**: Responds with "Добро пожаловать в наш бот!" ("Welcome to our bot!")
- **/help**: Provides a list of available commands: `/start`, `/help`, `/echo`, `/photo`

### Task 2: Echo Command

- **/echo**: Echoes back the user's message. If no message is provided, prompts the user to enter a message and provides an option to cancel the input.

### Task 3: Inline Buttons and Callback Handling

- **Inline Buttons**: Displays two inline buttons "Выбор 1" ("Choice 1") and "Выбор 2" ("Choice 2").
- **Callback Handling**: Responds with "Вы выбрали Выбор 1" ("You chose Choice 1") or "Вы выбрали Выбор 2" ("You chose Choice 2") based on the button clicked.

## Code Structure

- `bot.py`: Main bot script that initializes the bot, sets up handlers, and starts polling.
- `handlers/commands.py`: Contains command and callback handlers for the bot.

## Usage

1. Start the bot with the command `pipenv run python bot.py`.
2. Interact with the bot on Telegram using the provided commands and inline buttons.

## Troubleshooting

- **Import Errors**: Ensure all dependencies are correctly installed and compatible with your Python version.
- **Environment Issues**: Check that environment variables and database connections are correctly configured.
- **Bot Not Responding**: Verify that the bot token is correct and that the bot has the necessary permissions.

## Contributing

Feel free to submit issues or pull requests if you find bugs or have suggestions for improvements. 

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Feel free to make further adjustments based on your specific setup or preferences!
