import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "YOUR API KEY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

vision_model = genai.GenerativeModel('gemini-pro-vision')

import PIL.Image
image = PIL.Image.open('ANY PICTURE OF YOUR CHOICE')

response = vision_model.generate_content(["Explain this image", image])
print(response.text)
