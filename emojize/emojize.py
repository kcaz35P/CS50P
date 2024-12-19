import emoji
def main():
    input_emoji = input("Enter your Emoji:")
    print(emoji.emojize(input_emoji, language ='alias'))
    

if __name__ == "__main__":
    main()
