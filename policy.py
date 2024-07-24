def ask_questions_and_generate_file():
    # List of questions to ask
    questions = [
        "Site Name?",
        "Rule Name?",
        "To Zone?",
        "From Zone?",
        "Source?",
        "Destination?",
        "Application?",
        "Action?",
        "Description?"
    ]

    # Dictionary to store the answers
    answers = {}

    # Ask each question and store the answer
    for question in questions:
        answer = input(question + " ")
        answers[question] = answer

    #check if the application answer is "any"
    if answers['Application?'] == 'any':
        service = "service " + input ("Service?")
    else:
        service = "service any"

    description = f'"{answers["Description?"]}"'

    # Format the text
    formatted_text = (
        "\n" 
        f"set device-group {answers['Site Name?']} "
        f"pre-rulebase security rules {answers['Rule Name?']} "
        f"to {answers['To Zone?']} "
        f"from {answers['From Zone?']} "
        f"source {answers['Source?']} "
        f"destination {answers['Destination?']} "
        f"application {answers['Application?']} "
        f"action {answers['Action?']} "
        f"description {description} "
        f"{service}"
    )
    

    # Create a text file and write the formatted text to it
    with open("answers.txt", "a") as file:
        file.write(formatted_text)

    print("The answers have been written to answers.txt")

def main():
    while True:
        # Call the function
        ask_questions_and_generate_file()
        repeat = input ("Do you want to add another entry? (y / n) ").strip().lower()
        if repeat != 'y':
            break

main()
