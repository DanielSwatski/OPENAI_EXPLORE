from openai import OpenAI
import os
#from /config import OPENAI_API_KEY
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])



# Simple example of what the call looks like
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)



# App idea: This is going to be a news of the day type quiz. It will give you a 4 part answer for stuff
# that happened in the news today. It will be a multiple choice quiz. It will be a multiple choice quiz







