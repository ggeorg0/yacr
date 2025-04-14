#!/usr/bin/env python

from argparse import ArgumentParser, Namespace
from langchain.chat_models import init_chat_model
from langchain.prompts import ChatPromptTemplate
from rich.console import Console
from rich.markdown import Markdown

# Install ollama end execute this command to download and run Gemma3 with 4B params:
# >ollama run gemma3:4b
MODEL = "gemma3:4b"

SYSTEM_PROMPT = """
You are a highly skilled programming assistant with expert-level proficiency in Python 3. Your knowledge of the Python language includes a deep understanding of syntax, semantics, and best practices as outlined in the official PEP (Python Enhancement Proposal) specifications. You are well-versed in the structure and content of official documentation, and you use this knowledge to provide accurate, idiomatic, and up-to-date coding solutions.

Your responses should follow the conventions of modern Python programming, prioritize readability and maintainability, and adhere strictly to community standards. When appropriate, you may offer multiple approaches, explain trade-offs, and include references to relevant PEPs or documentation sections.

Do not generate code that relies on outdated practices or unsupported features. Be concise, helpful, and clear in your explanations, especially when assisting with debugging, architectural design, or writing idiomatic Python code.
"""

USER_PROMPT = """Please review the following code:
```python
{code}
```
Avoid rewriting the code, instead point out the places that may raise questions.

Review function after function, for each of which I provide a small report on its code.
Consider:
1. Code quality and adherence to best practices
2. Potential bugs or edge cases
3. Performance optimizations
4. Readability and maintainability
"""


def review_code(code_context: str, args: Namespace):
    model = init_chat_model(model=MODEL, model_provider="ollama")

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("user", USER_PROMPT),
        ]
    )

    prompt = prompt_template.invoke({"code": code_context})

    rich_console = Console()

    if not args.silent_mode:
        print_prompt(prompt, rich_console)

    buffer = []
    for idx, token in enumerate(model.stream(prompt)):
        buffer.append(token.content)
        print(token.content, end="")
    print()

    rich_console.rule("Model Output")

    formatted_output = Markdown("".join(buffer))
    rich_console.clear()
    rich_console.print(formatted_output)


def print_prompt(prompt, rich_console):
    rich_console.rule("Model Input")
    rich_console.print(Markdown(prompt.to_string()))
    rich_console.rule()


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Provide a filepath to your code and get a code review from the LLM "
    )
    parser.add_argument(
        "filepath",
        help="Path to the file whose content will be read and used as code context",
    )
    parser.add_argument(
        "-s",
        "--silent",
        help="Do not print the model input",
        required=False,
        action="store_true",
        dest="silent_mode",
    )
    args = parser.parse_args()

    with open(args.filepath, "r") as file:
        content = file.read()

    review_code(content, args)
