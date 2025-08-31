# Simple Chatbot

This is a simple chatbot project built using [Chainlit](https://docs.chainlit.io/) in Python. The chatbot responds to basic user inputs and demonstrates how to use Chainlit for interactive chat applications.

## Features
- Greets the user when the chat starts.
- Responds to the following messages:
  - `hello`: Replies with a greeting.
  - `how are you?`: Replies with a status message.
  - `bye`: Says goodbye.
  - Any other message: Replies with a default message indicating it didn't understand.

## Getting Started

### Prerequisites
- Python 3.8+
- [Chainlit](https://docs.chainlit.io/) library

### Installation
1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install chainlit
   ```

### Running the Chatbot
Run the following command in your terminal:
```bash
chainlit run main.py
```

This will start the chatbot server. Open the provided URL in your browser to interact with the chatbot.

## File Structure
- `main.py`: Main code for the chatbot logic.
- `README.md`: Project documentation.
- `pyproject.toml`, `uv.lock`: Dependency and environment files.

## Usage
Type messages like `hello`, `how are you?`, or `bye` to see the chatbot's responses. For any other input, the bot will reply that it didn't understand.

## License
This project is for educational purposes.
