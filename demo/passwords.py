import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

models = {
    "100": {
        "model": "ada:ft-acm-research-password-team:initial-model-test-2022-04-15-22-39-03",
        "stop": "\n\n###\n\n"
    },
    "1k": {
        "model": "ada:ft-acm-research-password-team:1k-examples-2022-04-16-17-55-28",
        "stop": "\n"
    },
    "10k": {
        "model": "ada:ft-acm-research-password-team:10k-examples-2022-04-16-18-15-21",
        "stop": "\n"
    }
}

prompt_stop = '\nPassword: \n###\n'

def guess(form):
    prompt = ""
    for key, value in form.items():
        if value != '':
            if key == 'realname':
                prompt += f"Real name is {value}\n"
            if key == 'dob':
                prompt += f"Date of Birth is {value}\n"
            if key == 'gender':
                if value == 'M':
                    prompt += f"Gender is Male\n"
                if value == 'F':
                    prompt += f"Gender is Female\n"
            if key == 'country':
                prompt += f"Country is {value}\n"
            if key == 'twitterid':
                prompt += f"Twitter ID is {value}\n"
            if key == 'about':
                prompt += f"User information: {value}\n"
            if key == 'status':
                prompt += f"User status: {value}\n"
    
    prompt += prompt_stop

    print(prompt)
    completion = get_GPT3_completion(prompt)
    print(completion)
    return completion


def get_GPT3_completion(prompt):
    response = openai.Completion.create(
        model=models['10k']['model'],
        prompt=prompt,
        max_tokens=32,
        temperature=0.8,
        stop=models['10k']['stop']
    )
    return response['choices'][0]['text']
