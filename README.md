# OpenAI Python Playground

A simple playground for experimenting with the OpenAI API.

## API Keys

You will have to set up an OpenAI account and get an API key. You can do that [here](https://platform.openai.com/api-keys).

Simply copy the `.env.example` file to `.env` and paste your API key in the `OPENAI_API_KEY` variable.

To run the examples that use Kaggle datasets, you will also need to set up a Kaggle account and get an API key. The API client will automatically search for a `~/.kaggle/kaggle.json` file. You can generate a token [here](https://www.kaggle.com/settings). Documentation for the Kaggle API can be found [here](https://www.kaggle.com/docs/api).
