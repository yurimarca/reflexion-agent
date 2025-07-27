# Reflexion Agent

This repository is part of the [LangGraph: Build Advanced LLM Agents with LangChain](https://www.udemy.com/course/langgraph/) Udemy course.  
It demonstrates how to build an iterative, tool-using AI agent workflow using [LangChain](https://python.langchain.com/) and [LangGraph](https://github.com/langchain-ai/langgraph).

## Features

- **Graph-based agent workflow**: Modular, iterative reasoning using LangGraph.
- **Tool integration**: Uses web search (Tavily) to enhance answers.
- **Iterative refinement**: The agent drafts, searches, and revises answers in a loop.

## Environment Setup

To run this project, we recommend using `pyenv` and `pyenv-virtualenv` for consistent environment management.

1.  **Install `pyenv` and `pyenv-virtualenv`:**  
    Follow the official installation guides for your operating system:  
    * [pyenv Installation](https://github.com/pyenv/pyenv#installation)  
    * [pyenv-virtualenv Installation](https://github.com/pyenv/pyenv-virtualenv#installation)  
    Ensure your shell is configured to initialize `pyenv` and `pyenv-virtualenv` (check your `~/.bashrc`, `~/.zshrc`, etc.).

2.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

3.  **Generate API keys and add to your environment file:**  
    - Copy `src/example.env` to `.env` and fill in your API keys (OpenAI, Tavily, etc.).

4.  **Install the required Python version:**
    ```bash
    pyenv install 3.10
    ```

5.  **Create and activate the virtual environment:**
    ```bash
    pyenv virtualenv 3.10 reflexion-agent
    pyenv local reflexion-agent # This creates a .python-version file for auto-activation
    ```

6.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

7.  **Run the project:**
    ```bash
    python src/main.py
    ```

## Usage

After running the project, the agent will process a sample prompt, use web search as needed, and iteratively refine its answer.  
You can modify the prompt or agent logic in `src/main.py` and related files.

### Response sample

**Write about the importance of the paper 'Attetion is all you need' for the current state of AI.**

The paper 'Attention Is All You Need' significantly impacted the AI domain through introducing the Transformer model, which utilized an 'attention' mechanism[1]. This mechanism enabled the model to focus differently on variable parts of the input data, efficiently capturing dependencies irrespective of their distance. It was a novel approach as the 'attention' mechanism superseded the sequential nature of conventional techniques—recurrent neural networks (RNNs) and convolutional neural networks (CNNs)[2]. This shift brought about notable improvements in computational efficiency and long-term dependencies, thereby transforming natural language processing (NLP)[2].

The Transformer model subsequently led to the development of advanced models such as BERT, GPT-2, and T5[3]. These offshoot technologies accelerated applications arising from NLP like machine translation, text generation, and question-answering[3]. Evidence of the Transformer model's success has triggered efforts to apply it across other areas in AI, emphasizing the ground-breaking implications of the 'Attention Is All You Need' paper[1][4].

In real-world applications, the Transformer model demonstrates its potential in areas like machine translation, text summarization, text generation, caption generation for images, programming assistance, and speech recognition and synthesis[5].

References:
[1]https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html
[2]http://jalammar.github.io/illustrated-transformer/
[3]https://towardsdatascience.com/transformers-141e32e69591
[4]https://arxiv.org/abs/1706.03762v5
[5]https://medium.com/@hassaanidrees7/transformers-in-action-real-world-applications-of-transformer-models-1092b4df8927

## License

This project is for educational purposes as part of the [LangGraph Udemy course](https://www.udemy.com/course/langgraph/).