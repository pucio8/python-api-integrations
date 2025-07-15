# Simple Weather CLI

A console application in Python for fetching and displaying the current temperature for a specified city using the OpenWeatherMap API.

---

## Key Features

-   Securely handles API keys using a `.env` file.
-   Fetches real-time weather data from the OpenWeatherMap API.
-   Displays the current temperature in Celsius, rounded to the nearest degree.
-   Simple, single-function script, easy to understand and modify.

---

## Tech Stack

### Console Application
-   **Language:** Python
-   **Libraries:** `requests`, `python-dotenv`

### Consumed API
-   **API:** OpenWeatherMap 2.5 API

---

## Setup and Run

1.  **Clone the repository:**
    ```bash
    git clone [REPOSITORY_URL]
    cd [PROJECT_DIRECTORY_NAME]
    ```
2.  **Create an Environment File:**
This application requires an environment file to store your private API key.
Create a new file named `.env` in the root directory of the project and add the following line, replacing `your_api_key_here` with your actual key from OpenWeatherMap:

    ```
    WEATHER_KEY=your_api_key_here
    ```
<details>
<summary>Step-by-step instructions on how to get an API key.</summary>

- Go to the [OpenWeatherMap](https://openweathermap.org/) website and create a free account.
- Navigate to the "API keys" tab in your user dashboard.
- You will find a default API key already generated for you. Copy this key.
</details>

Important: The `.env` file contains private keys. Never commit it to GitHub. Make sure your .gitignore file includes an entry for `.env`.

    ```bash
    # .gitignore
    .env
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file containing `requests` and `python-dotenv`)*

4.  **Run the application:**
    ```bash
    python main.py
    ```

---

## Example Usage

After running the script, you will see the following output in your console:

```bash
Temperature in Krapkowice is 18°C
```

*(The city and temperature will vary based on the code and current weather conditions.)*

