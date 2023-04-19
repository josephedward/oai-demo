# OpenAI Python App

This is a simple Python application that demonstrates how to interact with OpenAI models through their API. It uses the `openai` Python package to make API requests.

## Requirements
- Python 3.7 or higher
- `openai` Python package (`pip install openai`)
- API key for OpenAI (can be obtained from [https://beta.openai.com/docs/quickstart](https://beta.openai.com/docs/quickstart))

## Usage
- To run the application, set the following environment variables:
    + `OPENAI_API_KEY`: your OpenAI API key
    + `MODEL`: the name of the OpenAI model to use (e.g. `davinci`, `curie`, etc.)

- Then run the following command: `python app.py`
- Input a prompt when prompted
- Wait for the generated text to be returned
- Input another prompt, or type exit to quit the app.

## Docker
- Build the docker image: `docker build -t openai-python-app .`
- Run the container, passing in the required environment variables: `docker run -it --rm -e OPENAI_API_KEY=<your_api_key> -e MODEL=<model_name> openai-python-app`
- Input a prompt when prompted
- Wait for the generated text to be returned
- Input another prompt, or type exit to quit the app.

## Environment Variables
- OPENAI_API_KEY: Your OpenAI API key.
- MODEL: The name of the OpenAI model to use (e.g. davinci, curie, etc.).

## License
This project is licensed under the MIT License.