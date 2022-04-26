# poster outline

## introduction

 Imagine trying to hack into your friend's social media account by guessing what password they used to secure it. You do some research to come up with likely guesses – say, you discover they have a dog named "Dixie"and attempt to log in using the password {\tt DixieIsTheBest1}. The problem is that this only works if you have the intuition on how humans choose passwords, and the skills to conduct open-source intelligence gathering.

We refined GPT-3 models on user data from a security breach of the online platform Wattpad in order to generate targeted password guesses \emph{automatically}. This approach combines the vast knowledge of 350 million parameter–model with the personal information of \textbf{1 thousand users}, including usernames, phone numbers, and personal descriptions.

## methods

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
