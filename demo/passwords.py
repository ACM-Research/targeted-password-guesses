import random
import torch
import json
import re
from transformers import GPT2LMHeadModel, GPT2Tokenizer

fake_passwords = [
    "123456",
    "password",
    "12345",
    "123456789",
    "password1",
    "abc123",
    "12345678",
    "qwerty",
    "111111",
    "1234567",
    "1234",
    "iloveyou",
    "sunshine",
    "monkey",
    "1234567890",
    "123123",
    "princess",
    "baseball",
    "dragon",
    "football",
    "shadow",
    "michael",
    "soccer",
    "unknown",
    "maggie",
    "000000",
    "ashley",
    "myspace1",
    "purple",
    "fuckyou",
    "charlie",
    "jordan",
    "hunter",
    "superman",
    "tigger",
    "michelle",
    "buster",
    "pepper",
    "justin",
    "andrew",
    "harley",
    "matthew",
    "bailey",
    "jennifer",
    "samantha",
    "ginger",
    "anthony",
    "qwerty123",
    "qwerty1",
    "peanut",
    "summer",
    "hannah",
    "654321",
    "michael1",
    "cookie",
    "linkedin",
    "madison",
    "joshua",
    "taylor",
    "whatever",
    "mustang",
    "jessica",
    "qwertyuiop",
    "amanda",
    "jasmine",
    "123456a",
    "123abc",
    "brandon",
    "letmein",
    "freedom",
    "basketball",
    "xxx",
    "babygirl",
    "thomas",
    "william",
    "hello",
    "austin",
    "qwe123",
    "123",
    "jackson",
    "fuckyou1",
    "love",
    "family",
    "yellow",
    "trustno1",
    "robert",
    "jesus1",
    "chicken",
    "jordan23",
    "mickey",
    "diamond",
    "scooter",
    "booboo",
    "welcome",
    "george",
    "smokey",
    "cheese",
    "computer",
    "morgan",
    "nicholas",
]

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
password_list_length = 5

def fake_guess():
    return random.sample(fake_passwords, 30)

def guess(name, info):
    password_list = []
    for i in range(password_list_length):
        sequence = (f"Name: {name}\nInfo: {info}\nPassword:")
        inputs = tokenizer.encode(sequence, return_tensors='pt')
        outputs = model.generate(
            inputs, max_length=len(sequence)+20, do_sample=True, temperature=0.5
        )
        output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        match = re.search(r"Password:(.*)", output)
        if match:
            password = match.group(1)
            print(password)
            password_list.append(password)
        else:
            print(f"### Could not find {i}-th password result for output:\n{output}\n\n")

    return password_list
