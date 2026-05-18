#!/usr/bin/env python3
"""
Simple Sentiment Analysis Tool
Uses TextBlob to analyze sentiment of text input.
"""

from textblob import TextBlob
import argparse
import sys

def analyze_sentiment(text):
    """
    Analyze sentiment of given text.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        tuple: (polarity, subjectivity, sentiment_label)
            polarity: float between -1 (negative) and 1 (positive)
            subjectivity: float between 0 (objective) and 1 (subjective)
            sentiment_label: 'positive', 'negative', or 'neutral'
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.1:
        sentiment = "positive"
    elif polarity < -0.1:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return polarity, subjectivity, sentiment

def analyze_file(filepath):
    """
    Analyze sentiment of each line in a file.
    
    Args:
        filepath (str): Path to text file
        
    Returns:
        list: List of analysis results for each line
    """
    results = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if line:
                    polarity, subjectivity, sentiment = analyze_sentiment(line)
                    results.append({
                        'line': line_num,
                        'text': line[:50] + "..." if len(line) > 50 else line,
                        'polarity': polarity,
                        'subjectivity': subjectivity,
                        'sentiment': sentiment
                    })
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description="Simple Sentiment Analysis Tool using TextBlob",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "I love this product!"
  %(prog)s -f input.txt
  %(prog)s --interactive
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--text', help='Text to analyze')
    group.add_argument('-f', '--file', help='File containing text to analyze')
    group.add_argument('-i', '--interactive', action='store_true', 
                      help='Enter interactive mode')
    
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Show detailed analysis')
    
    args = parser.parse_args()
    
    if args.text:
        polarity, subjectivity, sentiment = analyze_sentiment(args.text)
        
        print(f"\nText: {args.text}")
        print(f"Sentiment: {sentiment}")
        if args.verbose:
            print(f"Polarity: {polarity:.3f} (range: -1 to 1)")
            print(f"Subjectivity: {subjectivity:.3f} (range: 0 to 1)")
        else:
            print(f"Score: {polarity:.3f}")
    
    elif args.file:
        results = analyze_file(args.file)
        
        print(f"\nAnalyzed {len(results)} lines from '{args.file}':")
        print("-" * 80)
        
        sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for result in results:
            sentiment_counts[result['sentiment']] += 1
            
            if args.verbose:
                print(f"Line {result['line']}:")
                print(f"  Text: {result['text']}")
                print(f"  Sentiment: {result['sentiment']}")
                print(f"  Polarity: {result['polarity']:.3f}")
                print(f"  Subjectivity: {result['subjectivity']:.3f}")
                print()
            else:
                print(f"Line {result['line']}: {result['sentiment']} ({result['polarity']:.3f})")
        
        print("-" * 80)
        print(f"Summary: Positive: {sentiment_counts['positive']}, "
              f"Negative: {sentiment_counts['negative']}, "
              f"Neutral: {sentiment_counts['neutral']}")
    
    elif args.interactive:
        print("Interactive Sentiment Analysis")
        print("Enter text to analyze (or 'quit' to exit):")
        print("-" * 40)
        
        while True:
            try:
                user_input = input("\n> ").strip()
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                polarity, subjectivity, sentiment = analyze_sentiment(user_input)
                
                print(f"Sentiment: {sentiment}")
                print(f"Polarity: {polarity:.3f}")
                print(f"Subjectivity: {subjectivity:.3f}")
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

if __name__ == "__main__":
    main()