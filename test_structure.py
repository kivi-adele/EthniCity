
from openai import OpenAI
client = OpenAI(api_key='')


def generate_customs(festival_name):
  client = OpenAI(
      api_key="please input your key",
  )

 

  response = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="gpt-3.5-turbo",
  )
  print("** Complete Response Object **")
  print(response)
  print("\n** Individual Attributes**")
  # Print each attribute name and value
  for attr, value in response.__dict__.items():
      print(f"{attr}: {value}")

# Example usage with a simple prompt
prompt = "Write a poem about a cat"
generate_customs(prompt)
