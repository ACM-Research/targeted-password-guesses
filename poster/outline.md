# poster outline

## introduction

 Imagine trying to hack into your friend's social media account by guessing what password they used to secure it. You do some research to come up with likely guesses – say, you discover they have a dog named "Dixie"and attempt to log in using the password {\tt DixieIsTheBest1}. The problem is that this only works if you have the intuition on how humans choose passwords, and the skills to conduct open-source intelligence gathering.

We refined GPT-3 models on user data from a security breach of the online platform Wattpad in order to generate targeted password guesses \emph{automatically}. This approach combines the vast knowledge of a 350 million parameter–model with the personal information of 1 thousand users, including usernames, phone numbers, and personal descriptions and automatically generates personalized password guesses

## methods

We went through every data leak listed on haveibeenpwned.com and selected a variety of datasets to further examine. In June 2020, Wattpad (an online platform for reading and writing stories) was hacked, and the personal information and passwords of 270 million users were revealed. This data breach is particularly well-suited to our research because it connects unstructured text data (user descriptions and statuses) to corresponding passwords. This kind of data is particularly well-suited for refining a large text transformer like GPT-3, and it's what sets our research apart from a previous study which created a framework for generating targeted guesses using \emph{structured} pieces of user information. The original dataset's passwords were hashed with the bcrypt algorithm, so we used data from the crowdsourced password recovery website Hashmob to match plain text passwords with corresponding user data.

We refined a version of the GPT-3 text transformer called Ada in three trials by giving it 100, 1000, and 10000 examples. We then tested each 

- why we picked Wattpad leak
	- list of leaks on haveibeenpwned
- Hashmob cracked passwords
- SQLite to align the data
- refining Ada on 100, 1000, and 10000 tokens
- refining Curie 
- testing with models and most popular passwords
- similarity testing

## results

- similarity curves
- correct guess percentage curves

## applications

- analyze security of employee's passwords
- crack more passwords from a data leak
- analyze security of individual passwords, say when registering for an account

## moving forward

- [depending on what the data looks like] we could scale up the model to train on Curie or Davinci
	- or to save on costs for more power, refactor the project to use the open-source alternative GPT-J
- more analysis 

## references

- https://blog.eleuther.ai/gpt3-model-sizes/
- https://hashmob.net/hashlists/info/4364-Wattpad.com%20bcrypt
