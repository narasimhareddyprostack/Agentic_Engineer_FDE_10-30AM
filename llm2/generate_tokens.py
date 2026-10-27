import tiktoken

prompt = input("Ask something!")

encoding=tiktoken.get_encoding('cl100k_base')
tokens=encoding.encode(prompt)

print("User Prompt:",prompt)
print(tokens)
print(len(tokens))

print("Prompt:",[encoding.decode([token]) for token in tokens])