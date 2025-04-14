# Yet another code reviewer (YACR)

This is a really simple CLI code reviewer that works with chat models like llama, gemma, etc.

## About project

This project provides a basic command-line interface (CLI) for reviewing code snippets using a language model.  It leverages Langchain and Ollama to interact with a chat model. The primary goal is to provide a quick and easy way to get feedback on code quality and potential bugs.

## Installation

### Installing this python project

1.  Clone the repository:
    ```bash
    git clone https://github.com/ggeorg0/yacr.git
    cd yet-another-code-reviewer
    ```
2. Create a virtual environment (optional but recommended):
    ```bash
    # On Linux:
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    ./venv/Scripts/activate
    ```

2.  Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Installing ollama as local LLM provider

Ollama is a dependency of this project. You need to install it separately.

1.  **Download and Install Ollama:**  Follow the instructions on the official Ollama website: [https://ollama.com/download](https://ollama.com/download)

2.  **Run Ollama:** After installation, run Ollama from your terminal:

    ```bash
    ollama run gemma3:4b
    ```

    Gemma3 with 4B params is a generally good tradeoff between performance and size. Also you can use other models like Llama, Mistral etc.

    However this step is crucial as the code reviewer relies on __some__ chat model being running.  Make sure you have sufficient disk space (at leats 4 GB). Also the model startup can take some time.

## Usage

To use the code reviewer, run the following command in your terminal:

```bash
python yacr.py <filepath>
```

* `<filepath>`:  The path to the Python file you want to review.

* You can provide `-s` flag (or `--silent`): The model input prompt will not be printed to the console.

**Example:**

```bash
python yacr.py yacr.py -s
```

This will read the content of `yacr.py` (yes, it's the script itself) and send it to the chat model for review. The model's response will be printed to the console.

Here is the output:
![Screenshot from 2025-04-15 00-34-06](https://github.com/user-attachments/assets/3763ca2b-085e-4371-95ef-22232b1648ec)
