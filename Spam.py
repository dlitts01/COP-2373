# Drew Bennett-Litts
# COP 2373 Programming Exercise - Spam Score
# This program checks an email message for common spam words and phrases.


def get_spam_words():
    """Return the list of 30 common spam words and phrases."""
    spam_words = [
        "free",
        "guaranteed",
        "act now",
        "limited time",
        "winner",
        "congratulations",
        "click here",
        "cash bonus",
        "risk free",
        "no obligation",
        "verify your account",
        "urgent",
        "make money",
        "earn money",
        "work from home",
        "special promotion",
        "exclusive deal",
        "buy now",
        "order now",
        "claim now",
        "prize",
        "million dollars",
        "credit card",
        "lowest price",
        "miracle",
        "100% satisfied",
        "double your income",
        "apply now",
        "instant access",
        "no cost"
    ]

    return spam_words


def get_email_message():
    """Ask the user to enter an email message and return it."""
    print("Spam Email Checker")
    print("Enter the email message you want to check.")
    print("Press Enter twice when you are finished.\n")

    message_lines = []

    while True:
        line = input()

        if line == "":
            break

        message_lines.append(line)

    email_message = " ".join(message_lines)

    return email_message


def calculate_spam_score(email_message, spam_words):
    """Count spam words/phrases and return the score and matched terms."""
    message_lower = email_message.lower()
    spam_score = 0
    matched_words = []

    # Check each spam word or phrase against the email message.
    for word in spam_words:
        occurrences = message_lower.count(word.lower())

        # Add one point for every occurrence found.
        if occurrences > 0:
            spam_score += occurrences

            # Save the matched word once for the final results list.
            matched_words.append(word)

    return spam_score, matched_words


def rate_spam_likelihood(spam_score):
    """Return a spam likelihood rating based on the spam score."""
    if spam_score == 0:
        likelihood = "Very unlikely to be spam"
    elif spam_score <= 2:
        likelihood = "Low likelihood of spam"
    elif spam_score <= 5:
        likelihood = "Moderate likelihood of spam"
    elif spam_score <= 9:
        likelihood = "High likelihood of spam"
    else:
        likelihood = "Very high likelihood of spam"

    return likelihood


def display_results(spam_score, likelihood, matched_words):
    """Display the final spam score, rating, and matched spam terms."""
    print("\n--- Spam Check Results ---")
    print(f"Spam score: {spam_score}")
    print(f"Likelihood: {likelihood}")

    if matched_words:
        print("Words/phrases that increased the spam score:")

        for word in matched_words:
            print(f"- {word}")
    else:
        print("No spam words or phrases were found.")


def main():
    """Control the main flow of the program."""
    spam_words = get_spam_words()
    email_message = get_email_message()
    spam_score, matched_words = calculate_spam_score(email_message, spam_words)
    likelihood = rate_spam_likelihood(spam_score)
    display_results(spam_score, likelihood, matched_words)


# Start the program.
if __name__ == "__main__":
    main()
