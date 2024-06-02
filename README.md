# CFG-Assignment-2 -  Cat Fact Generator

A simple Python console application that fetches and displays random cat facts using the [Cat Facts API](https://cat-fact.herokuapp.com/facts/random). The user can specify the number of facts they want, and the facts are then displayed and saved to a file with a timestamped filename.

## Features

- Fetches random cat facts from the Cat Facts API.
- Allows the user to specify the number of facts to fetch.
- Displays the fetched cat facts in the console.
- Asks the user if they want to fetch more facts.
- Saves all fetched facts to a file with a timestamped filename.
- Displays the first five facts if five or more are fetched.

## Usage

1. **Run the Script**

    ```sh
    python cat_fact_generator.py
    ```

2. **Follow the On-Screen Instructions**

    - Enter the number of cat facts you want to fetch.
    - Decide if you want to fetch more facts when prompted.
    - The facts will be displayed in the console and saved to a file with a timestamped filename.

## Example

```plaintext
How many cat facts do you want? 3
Fact 1: Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.
Fact 2: A group of cats is called a clowder.
Fact 3: The world's largest cat measured 48.5 inches long.

Do you want more cat facts? (yes/no): no
All facts saved to cat_facts_20240531_123456.txt

