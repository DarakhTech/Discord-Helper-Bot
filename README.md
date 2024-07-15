# Discord Bot with Google Sheets Integration

This Discord bot allows users to set reminders, add events, manage work pauses, and update Google Sheets with job application information. The bot leverages `gspread` and `oauth2client` for Google Sheets integration and uses `discord.py` for interacting with Discord.

## Features

- **/remind**: Set a reminder at a specified time with a custom message.
- **/add_event**: Schedule an event at a specified date and time.
- **/wp**: Start and stop work-pause reminders.
- **/update**: Immediately append job application information to a Google Sheet.

## Requirements

- Python 3.6+
- A Discord bot token
- Google Sheets API credentials
- Required Python packages (listed in `requirements.txt`)

## Setup

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment and activate it**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up Google Sheets API credentials**:
    - Follow the instructions to create a Google Cloud project and enable the Google Sheets API.
    - Create credentials for a service account and download the JSON key file.
    - Place the JSON key file in the `src/constants` directory and name it `token.json`.

5. **Create a `.env` file** in the root directory of the project and add your credentials:

    ```env
    BOT_TOKEN=your-discord-bot-token
    GOOGLE_SHEETS_CREDENTIALS_PATH=src/constants/token.json
    SHEET_NAME=Your Google Sheet Name
    WORKSHEET_NAME=Sheet1
    ```

6. **Run the bot**:

    ```sh
    python app.py
    ```

## Usage

- **/remind HH:MM Message**: Set a reminder for a specified time with a custom message.
- **/add_event YYYY-MM-DD HH:MM Event**: Schedule an event at a specified date and time.
- **/wp start {time in minutes}**: Start work-pause reminders.
- **/wp end**: End work-pause reminders.
- **/update JSON**: Append job application information to a Google Sheet. Use backticks (`) around the JSON data to avoid issues with Discord command parsing.

    Example:
    
    ```plaintext
    /update `{"Name of Company": "Discord", "Job Title": "Engineer", "Job ID": "12345", "Link": "https://discord.com/careers", "Status": "Applied", "Location": "NY"}`
    ```
## Images
<img width="1624" alt="Screenshot 2024-07-09 at 4 23 03 AM" src="https://github.com/DarakhTech/Discord-Helper-Bot/assets/54445464/e26bc706-aae8-4938-a63d-31d14b8a0a8c">
<img width="670" alt="Screenshot 2024-07-09 at 4 21 37 AM" src="https://github.com/DarakhTech/Discord-Helper-Bot/assets/54445464/e8ad2a08-b91c-46af-bc7f-eaf6c91cc198">
<img width="670" alt="Screenshot 2024-07-09 at 4 24 08 AM" src="https://github.com/DarakhTech/Discord-Helper-Bot/assets/54445464/a12d02cb-9bb6-4e15-934b-3238d68a19e4">


## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
