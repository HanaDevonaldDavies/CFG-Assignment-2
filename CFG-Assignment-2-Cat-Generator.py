import requests
import json
from datetime import datetime

# Get random cat facts from the API
def get_random_facts(number_of_facts):
    response = requests.get('https://cat-fact.herokuapp.com/facts?animal_type=cat&category=history')
    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list):
            return [fact['text'] for fact in data]
        else:
            return [data['text']]
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

# Function to save the list of facts to a file
def save_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def main():
    # List to store facts
    facts = []

    while True:
        # Ask the user for the number of facts they want
        try:
            number_of_facts = int(input("How many cat facts do you want? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Fetch the random facts
        new_facts = get_random_facts(number_of_facts)
        facts.extend(new_facts)

        # Print the facts
        for i, fact in enumerate(facts, start=1):
            print(f"Fact {i}: {fact}")

        # Ask the user if they want more facts
        another = input("Do you want more cat facts? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    # Save all facts to a file
    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cat_facts_{date_time}.txt"
    all_facts = "\n".join(f"Fact {i+1}: {fact}" for i, fact in enumerate(facts))
    save_to_file(all_facts, filename)
    print(f"All facts saved to {filename}")

    # Boolean value and if..else statement
    if len(facts) >= 5:
        print("Here are the first 5 cat facts:")
        print("\n".join(f"Fact {i+1}: {fact}" for i, fact in enumerate(facts[:5])))
    else:
        print("You have fewer than 5 facts.")
