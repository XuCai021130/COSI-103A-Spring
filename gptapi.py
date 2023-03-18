import openai

# Set up the OpenAI API client
openai.api_key = "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"

# test for an API key
if openai.api_key=="YOUR_API_KEY":
    print("You need to get an openapi api key to use this demo")
    exit()

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input("Enter a prompt: ") # "Hello, how are you today?"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)