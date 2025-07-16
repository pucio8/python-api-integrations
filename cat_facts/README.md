# Cat Facts CLI

A fun command-line application in Python that fetches and displays a random fact about cats from a public API.

---

## Key Features

-   Connects to the `catfact.ninja` public API to get real-time data.
-   Handles potential network errors gracefully.
-   Presents a single, random cat fact in a clean, readable format in the console.

---

## Tech Stack

### Console Application
-   **Language:** Python
-   **Libraries:** `requests`

### Consumed API
-   **API:** Cat Fact Ninja API
-   **Authentication:** None (Public API)

---

## Setup and Run

1.  **Clone the repository:**
    ```bash
    git clone [REPOSITORY_URL]
    cd cat_facts
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file containing `requests`)*

3.  **Run the application:**
    ```bash
    python main.py
    ```
    *(Assuming the script is named `main.py`)*

---

## Example Usage

After running the script, you will see a similar output in your console:

Connecting to the API...

🐾 Today fact about cats :
-> A cat's field of vision is about 200 degrees.
Thank you for the fact!
