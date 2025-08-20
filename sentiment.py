from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyze sentiment using TextBlob only
    """
    if not text.strip():
        return None
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment
    if polarity > 0.1:
        sentiment = "Positive"
        emoji = "😊"
    elif polarity < -0.1:
        sentiment = "Negative" 
        emoji = "😞"
    else:
        sentiment = "Neutral"
        emoji = "😐"
    
    # Calculate accuracy (confidence) based on distance from neutral
    accuracy = abs(polarity) * 100
    if accuracy > 100:
        accuracy = 100
    
    return {
        "sentiment": sentiment,
        "emoji": emoji,
        "polarity": round(polarity, 3),
        "subjectivity": round(subjectivity, 3),
        "accuracy": round(accuracy, 1)
    }

def main():
    print("🎭 SENTIMENT ANALYZER (TextBlob Only)")
    print("=" * 40)
    print("Type 'quit' to exit\n")
    print()
    
    while True:
        # Get user input
        text = input("Enter text to analyze: ").strip()
        
        if text.lower() == 'quit':
            print("👋 Goodbye!")
            break
        
        if not text:
            print("❌ Please enter some text!\n")
            continue
        
        # Analyze sentiment
        result = analyze_sentiment(text)
        
        if result:
            print(f"\nText: \"{text}\"")
            print(f"Sentiment: {result['emoji']} {result['sentiment']}")
            print(f"Accuracy: {result['accuracy']}%")
            print(f"Polarity: {result['polarity']} (range: -1 to +1)")
            print(f"Subjectivity: {result['subjectivity']} (range: 0 to 1)")
            print("-" * 40 + "\n")
        else:
            print("❌ Please enter some text!\n")

if __name__ == "__main__":
    main()