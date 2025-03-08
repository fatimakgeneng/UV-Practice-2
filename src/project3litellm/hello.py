from litellm import completion
import os

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def call_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash", 
        messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
)
    print(response['choices'][0]['message']['content'])



def call_gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp", 
        messages=[{"role": "user", "content": "who's the founder of PIAIC?"}]
)
    print(response['choices'][0]['message']['content'])


def call_gemini3():
    response = completion(
        model="gemini/gemini-2.0-flash-exp", 
        messages=[{"role": "user", "content": "who's the founder of Pakistan?"}]
)
    print(response['choices'][0]['message']['content'])    