import os
from openai import OpenAI

def ai_image(prompt):

  os.environ["OPENAI_API_KEY"] = "API-KEY"

  client = OpenAI(
      api_key=os.environ.get("OPENAI_API_KEY"),
  )

  response = client.images.generate(
    model="dall-e-3",
    prompt=f"{prompt}의 홍보 포스터",
    size="1024x1024",
    quality="standard",
    n=1,
  )

  image_url = response.data[0].url
  return image_url