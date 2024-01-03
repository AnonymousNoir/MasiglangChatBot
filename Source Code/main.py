# These are all the libraries
# JSON for storing virtually the responses of the bot
import json
# RE is for regular expressions
import re
# random responses is for responding to inappropriate answer of the user
import random_responses
# random is for random reponses of the bot specifically based on question and answer of the user
import random
# this library is for delay
import time
# this is for accessing the clear screen of the terminal or console
import os

# ANSI escape codes for text colors
class TextColors:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"

# Default list of questions about a healthy lifestyle in Tagalog
listOfQuestions = [
    "Tanong 1. Para sa unang katanungan, paano mo tinutugunan ang pangangailangan ng iyong katawan sa tamang nutrisyon?",
    "Tanong 2. Ano naman ang mga paborito mong masustansiyang pagkain at bakit?",
    "Tanong 3. Paano mo naman naipapakita ang pag-aalaga sa iyong mental na kalusugan araw-araw?",
    "Tanong 4. Ano ang mga regular na ehersisyo o aktibidad na paborito mo?",
    "Tanong 5. Paano mo hinahandle ang stress sa iyong buhay araw-araw?",
    "Tanong 6. Ano ang mga stratehiya mo para mapanatili ang magandang tulog?",
    "Tanong 7. Paano mo naman naiiwasan ang mga masasamang bisyo sa iyong paligid?",
    "Tanong 8. Ano ang mga personal na paraan mo para ma-maintain ang tamang timbang?",
    "Tanong 9. Paano mo sinusunod ang prinsipyo ng malinis na kapaligiran sa iyong pang-araw-araw na buhay?",
    "Tanong 10. Ano ang mga bagay na nagbibigay sa'yo ng kaligayahan at kasiyahan?",
    "Tanong 11. Paano mo isinasaayos ang iyong oras para maglaan ng sapat na panahon para sa iyong sarili at sa iyong kalusugan?",
    "Tanong 12. Para sa huling katanungan, ano ang mga regular na gawain o ritwal na nakakatulong sa iyong kabuuang kagalingan?"
]

# Storing the recommendations for the summary
listOfRecommendations = [""] * len(listOfQuestions)

# Global static variable to store the name of the user for later usage
user = ""

# Load JSON data
def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)

# Store JSON data of the responses of the bot
response_data = load_json("bot.json")

def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    #response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Wala kang inilagay sa iyong input, maglagay ka para makausap kita :("

    # If there is no good response, return a random one.
    if best_response != 0:
        response_index = score_list.index(best_response)
        bot_response = random.choice(response_data[response_index]["bot_response"])

        bot_recommendation_options = response_data[response_index]["bot_recommendation"]
        bot_recommendation = random.choice(bot_recommendation_options) if bot_recommendation_options else ""

        # Return a random response from the list of responses
        return bot_response, bot_recommendation

    return random_responses.random_string(), ""

# this function is for typing animation
def print_with_typing(text, delay=0.03):
    # iterate all the characters one by one in the text
    for char in text:
        print(char, end='', flush=True)
        # this is for the delay speed of the typing animations
        time.sleep(delay)
    # for spacing
    print()

# function for run_chat_bot() to run the bot
def run_chat_bot():
    print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
    print_with_typing("Magandang araw! Ako nga pala si Masiglang bot na handang maglingkod sa iyo para sa healthy lifestyle mo!")
    print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
    print_with_typing("Magbibigay lamang ako ng 12 na katanungan na kailangan mong sagutin upang malaman ko ang iyong lifestyle at mabigyan kita ng sagot at rekomendasiyon batay sa iyong magiging kasagutan.")
    
    input("\n Press Enter to proceed...")
    
    # Looping until the user inputs the correct letter
    while True:
        # This serves for clearing the screen or the content of the terminal like a refresh
        os.system('cls')
        print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET} ", end = '')
        print_with_typing("Bago tayo magsimula, nais ko munang malaman ang iyong kasagutan kung sang-ayon ka ba na ibigay ang iyong mga personal na kasagutan patungkol sa iyong healthy lifestyle? Y/N")
        user_agreement = input(f"{TextColors.CYAN}You: {TextColors.RESET}")

        # Check if the users agree to the conditions
        if user_agreement.casefold() == 'y':
            print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
            print_with_typing("Maraming salamat sa iyong pag sang-ayon!")
            print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
            print_with_typing("Para tayo ay makapagsimula na nais ko munang malaman kung ano ang iyong pangalan?")
            
            user = input(f"{TextColors.CYAN}You: {TextColors.RESET}")

            print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
            print_with_typing(f"Magandang araw muli sa'yo {user}! Pindutin mo lamang ang enter sa iyong keyboard para tayo ay magsimula na")

            input("\n Press Enter to proceed...")
            chat_bot_question()
            break
        # Otherwise it will exit the program
        elif user_agreement.casefold() == 'n':
            print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
            print_with_typing("Kung gayon, maraming salamat sa pagsubok ng MASIGLANG CHATBOT!")

            input("\n Press Enter to exit...")
            return
        # This case is for checking the input of the users to type only y or n
        else:
            print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
            print_with_typing("Letter Y or N lamang ang kailangan mong ilagay.")

            input("\n Press Enter to try again...")
            continue

    print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
    print_with_typing(f"Muli, maraming salamat sa pagtangkilik kay Masiglang Bot! Tinitiyak ko na ikaw ay magkakaroon ng isang magandang healthy lifestyle sa buhay mo! Basta iapply mo lamang ang mga natutunan mo at mga naging rekomendasiyon ko para sa iyo. Hanggang sa muli {user}!")
    
    input("\n Press Enter to exit...")
    return
    
# function for chat_bot_summary() to show the summary of recommendations
def chat_bot_summary():
    os.system('cls')
    print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end = '')
    print_with_typing("Maraming salamat sa iyong mga sagot! Para sa iyong sanggunian sa mga naging rekomendasiyon sa bawat tanong kanina. Ito ang listahan ng mga rekomendasiyon para iyong hindi makalimutan:")
    # Iterating all the stored listOfRecommendations to show in the summary using for loop
    for i in range(len(listOfRecommendations)):
        print(f"REKOMENDASIYON {i+1}: {listOfRecommendations[i]}")

    input("\n Press Enter to proceed...")
    os.system('cls')

# function for chat_bot_question() to start the 12 questions
def chat_bot_question():
    i = 0  # Initialize the index

    # Using while loop to iterate all the questions with the use of len for getting the total length of the array listOfQuestions
    # This also serves to track the current question number to avoid resetting it again when the user inputs inappropriate answer
    while i < len(listOfQuestions):
        os.system('cls')
        print('\n')

        print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end='')
        print_with_typing(listOfQuestions[i])

        user_input = input(f"{TextColors.CYAN}You: {TextColors.RESET}")
        bot_response, bot_recommendation = get_response(user_input)

        print(f"{TextColors.GREEN}MASIGLANG BOT: {TextColors.RESET}", end='')
        print_with_typing(bot_response)

        # If there's a content in bot recommendation, there will be a recommendation
        if bot_recommendation:
            print(f"{TextColors.GREEN}REKOMENDASIYON KO PARA SA IYO: {TextColors.RESET}", end='')
            print_with_typing(bot_recommendation)
        # Otherwise it will ask the question again if there's no detection appropriate answer from the user
        else:
            input("\nPress Enter to try again...")
            # Ask the question again if there's no recommendation
            continue  # Go to the next iteration without incrementing i

        listOfRecommendations[i] = bot_recommendation

        input("\nPress Enter to proceed to the next question...")
        i += 1  # Increment the index for the next iteration

    # To call the function summary after the loop
    chat_bot_summary()

# This is the driver code to run the main program
if __name__ == "__main__":
    run_chat_bot()