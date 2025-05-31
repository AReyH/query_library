# Query Library

Query Library is a lightweight tool for generating descriptions and tags for a set of SQL queries using a large language model. It transforms raw SQL into structured metadata, making it easier to catalog, search, and understand your queries at scale.

## Features

* Converts SQL queries into structured dictionaries with:

  * Descriptions of what each query does
  * A list of relevant tags
* Outputs results in a pandas DataFrame for easy analysis or storage
* Powered by OpenRouter’s LLMs (e.g., DeepSeek)

## How It Works

1. Reads a `.txt` file containing SQL queries.
2. Sends the queries to an LLM with a structured prompt.
3. Receives a dictionary with query metadata (query, description, tags).
4. Loads the result into a pandas DataFrame.

## Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/areyh/query_library.git
   cd query_library
   ```

2. Install dependencies:

   ```bash
   pip install pandas openai
   ```

3. Set your OpenRouter API key:

   ```bash
   export API_KEY='your_api_key_here'
   ```

## Usage

1. Add your queries to a file, e.g. `queries.txt`, with each query ending in a semicolon (`;`).
2. Run the script:

   ```bash
   python main.py
   ```

## Example Output

A sample output DataFrame:

| query                 | description                      | tags                 |
| --------------------- | -------------------------------- | -------------------- |
| SELECT \* FROM users; | Retrieves all records from users | \["users", "select"] |

## Roadmap

* Add a CLI interface
* Store output in a local database or JSON file
* Implement search by description or tags

## License

MIT License
