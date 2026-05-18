# Simple Sentiment Analysis Tool

A lightweight Python tool for sentiment analysis using TextBlob and NLTK.

## Features

- **Text Analysis**: Analyze sentiment of individual text strings
- **File Analysis**: Process text files line by line
- **Interactive Mode**: Real-time sentiment analysis in interactive mode
- **Detailed Metrics**: Polarity (-1 to 1) and subjectivity (0 to 1) scores
- **Sentiment Classification**: Automatically classifies as positive, negative, or neutral

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-tool.git
   cd sentiment-analysis-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download NLTK data (required for TextBlob):
   ```bash
   python -m textblob.download_corpora
   ```

## Usage

### Command Line Interface

**Analyze a single text:**
```bash
python sentiment_analysis.py -t "I love this amazing product!"
```

**Analyze a text file:**
```bash
python sentiment_analysis.py -f input.txt
```

**Interactive mode:**
```bash
python sentiment_analysis.py --interactive
```

**Verbose output:**
```bash
python sentiment_analysis.py -t "This could be better" --verbose
```

### Output Examples

```
Text: I love this amazing product!
Sentiment: positive
Polarity: 0.875
Subjectivity: 0.750
```

```
Analyzed 3 lines from 'input.txt':
------------------------------------------------------------------------
Line 1: positive (0.625)
Line 2: negative (-0.350)
Line 3: neutral (0.050)
------------------------------------------------------------------------
Summary: Positive: 1, Negative: 1, Neutral: 1
```

## How It Works

This tool uses [TextBlob](https://textblob.readthedocs.io/), a Python library for processing textual data. TextBlob provides a simple API for common natural language processing (NLP) tasks including:

- **Polarity**: Ranges from -1 (extremely negative) to 1 (extremely positive)
- **Subjectivity**: Ranges from 0 (very objective) to 1 (very subjective)

### Sentiment Classification Rules

- **Positive**: polarity > 0.1
- **Negative**: polarity < -0.1  
- **Neutral**: polarity between -0.1 and 0.1 (inclusive)

## Project Structure

```
sentiment-analysis-tool/
├── sentiment_analysis.py    # Main Python script
├── requirements.txt         # Python dependencies
├── README.md               # This documentation
├── .gitignore              # Git ignore file
└── examples/               # Example files (optional)
    ├── positive.txt
    ├── negative.txt
    └── mixed.txt
```

## Requirements

See `requirements.txt` for exact versions:
- `textblob==0.18.0`
- `nltk==3.8.1`

## Creating Example Files

Create a text file `input.txt` with sample text:

```
This product is absolutely fantastic!
I'm very disappointed with the service.
The weather is nice today.
The food was okay, nothing special.
I hate waiting in long lines.
```

Then analyze it:
```bash
python sentiment_analysis.py -f input.txt --verbose
```

## Limitations

1. **English Language**: Works best with English text
2. **Simple Analysis**: Uses rule-based sentiment analysis (not machine learning)
3. **Context Awareness**: Doesn't understand sarcasm or complex linguistic constructs
4. **Short Texts**: More accurate with complete sentences than single words

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TextBlob](https://textblob.readthedocs.io/) for the sentiment analysis engine
- [NLTK](https://www.nltk.org/) for natural language processing tools
- Inspired by various NLP tutorials and examples

## Support

For issues and questions:
1. Check the [Issues](https://github.com/yourusername/sentiment-analysis-tool/issues) page
2. Create a new issue if your problem isn't already reported

## Version History

- **1.0.0** (Current)
  - Initial release
  - Basic sentiment analysis functionality
  - Command line interface with three modes
  - File processing capabilities

---

**Note**: This is a simple educational tool. For production sentiment analysis, consider more advanced solutions like spaCy, Transformers, or commercial APIs.