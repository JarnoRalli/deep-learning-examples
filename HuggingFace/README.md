# 1 Hugging Face

This directory contains examples, such as using existing models, tokenizers etc. from the HuggingFace

# 2 Examples

## 2.1 Miscalleneous
* [Image captioning](./Image_captioning.ipynb)
  * Conditional and un-conditional image captioning
* [FastSpeech 2 text to speech](./FastSpeech2_text_to_speech.ipynb)
  * Text to speech using FastSpeech 2

## 2.2 Language Related

* [Tokenizer_examples_1.ipynb](./Tokenizer_examples_1.ipynb)
  * Examples regarding tokenization using BERT language model
* [Tokenizer_examples_2.ipynb](./Tokenizer_examples_2.ipynb)
  * Examples regarding tokenization related to question-answering language modeling
  * Tokenization of long contexts using sliding window
* [Sentiment analysis](./Sentiment_analysis.ipynb)
  * Sentiment analysis based on given text
  * Transformer based
* [Text generation](./Text_generation.ipynb)
  * Text generation based on a given prompt
  * Transformer based
* [Masked language modeling](./Masked_language_modeling.ipynb)
  * Masked text generation, i.e. find most probable matches for words that have been masked out from the text
  * Can be thought of being related to denoising autoencoders
  * Transformer based
* [Fine_tuning_sentiment_analysis.ipynb](./Fine_tuning_sentiment_analysis.ipynb)
  * Fine tuning a pre-trained Bert model, that has a head with randomly initialized weights, for sentiment analysis

## 2.3 Datasets
* [Dataset_example.ipynb](./Dataset_example.ipynb)
  * An examples regarding how to use HuggingFace's datasets with tokenizers

