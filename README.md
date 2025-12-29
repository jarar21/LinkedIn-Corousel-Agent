
# CrewAI LinkedIn Post Generator

This project uses CrewAI to generate LinkedIn posts on a given topic.

## Setup and Installation

1. **Navigate to the project directory:**
   ```bash
   cd crewai_linkedin_post
   ```

2. **Create a virtual environment:**
   On Windows:
   ```bash
   python -m venv venv
   ```
   On macOS/Linux:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   On Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set your OpenAI API Key:**
   Make sure to set your `OPENAI_API_KEY` as an environment variable. You can do this by creating a `.env` file in the project directory with the following content:
   ```
   OPENAI_API_KEY="your_api_key_here"
   ```
   Then, in `main.py`, uncomment the following lines:
   ```python
   # from dotenv import load_dotenv
   # load_dotenv()
   ```
   Alternatively, you can set it directly in `main.py` (not recommended for security reasons):
   ```python
   # os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"
   ```

## Running the Script

Once you have completed the setup, you can run the script with the following command:
```bash
python main.py
```

You can change the topic of the post by editing the `topic` variable in the `if __name__ == '__main__':` block in `main.py`.
