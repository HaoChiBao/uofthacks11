import cohere 
co = cohere.Client('pdm3fybwqkzCV5BkUhptIesobKyqZvpMmnmteNvZ') # This is your trial API key
response = co.chat( 
  model='command',
  message='Hello, how are you?',
  temperature=0.7,
  chat_history=[],
  prompt_truncation='AUTO',
  stream=True,
  citation_quality='accurate',
  connectors=[],
  documents=[]
) 
print(response)