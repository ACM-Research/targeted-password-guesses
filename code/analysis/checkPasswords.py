import csv

passwordsArray = ["hi", "hi2", "dallas","password"]
topPassMatch = []
targetedPassMatch = []

#Remove this later
targetedArray = [
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
crackedTop =0
topTries = 0
crackedTargeted = 0
targetedTries = 0

with open('users.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for password in csv_reader:
    
        # Check in top 100 passwords
        with open('passwordsList100.txt') as file:
                for line in file:
                    topTries += 1
                    if password[1] == line.strip():
                        crackedTop+=1
                        topPassMatch.append([password[1], topTries])
                        continue

        # Check in targeted array passwords, needs refinement
        for line in targetedArray:
            targetedTries += 1
            if password[1] == line.strip():
                crackedTargeted+=1
                targetedPassMatch.append([password[1], targetedTries])
                continue

        topTries, targetedTries = 0, 0

""" topPassMatchUnique, targetedPassMatchUnique = [],[]
[topPassMatchUnique.append(password[1]) for password[1] in topPassMatch if password[1] not in topPassMatchUnique]
[targetedPassMatchUnique.append(x) for password[1] in targetedPassMatch if password[1] not in targetedPassMatchUnique] """

print("TOP 100 PASSWORDS MATCH \n", len( topPassMatch), "(", len(topPassMatch)/10369*100, "%)", "Passwords match: ",  topPassMatch,'\n\n')
print("TARGETED 100 PASSWORDS MATCH \n", len( targetedPassMatch), "(", len( targetedPassMatch)/10369*100, "%)", "Passwords match: ",  targetedPassMatch)


# % of cracked passwords vs. num of guesses in Top 100; % of guesses vs. num of guesses in targeted list