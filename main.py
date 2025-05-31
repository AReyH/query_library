import pandas as pd
import json
from openai import OpenAI
import os

base_prompt = '''Generate a description for the following list of SQL queries at the end of this
                  prompt. The list could be of length 1 to N (N being any integer greater than 1).
                  Also generate tags for what the query may be related to.
                  Return the query, description, and tags (in a list) in a dictionary
                  format similar to this {"query":[query],"description":[description],
                  "tags":[tags]}. Where query is the list of queries, and description is a list of
                  the respective descriptions, and tags is the list of respective list of tags.
                  Do not return any "\n" characters. Do not return any newline characters.
                  Also make a list of the possible tags, and distribute them along the queries.
                  The queries may be related to each other. Do not start the return with a "json". It should
                  start as a normal dictionary with a "{" and end with a "}"'''

def read_input(queries_txt):
  f = open(queries_txt)

  queries = f.read().replace('\n','').split(';')

  return queries


def generate_json(prompt):
    client = OpenAI(
        api_key=API_KEY,
        base_url='https://openrouter.ai/api/v1'
    )

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ]
    )

    result = completion.choices[0].message.content

    return result



def create_table(data):
  df = pd.DataFrame(data)
  return df

if __name__ == '__main__':
  queries = read_input('/content/queries.txt')
  prompt = generate_json(f'{base_prompt} {queries}')
  data = json.loads(prompt)
  df = create_table(data)
