import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# تأكدي من تحميل المكتبات إذا كنتِ تشغلين الكود محلياً
# nltk.download('punkt')
# nltk.download('stopwords')

def summarize_text(text, num_sentences=2):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    word_frequencies = {}
    for word in words:
        if word not in stop_words and word.isalnum():
            word_frequencies[word] = word_frequencies.get(word, 0) + 1
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summary_sentences)

# مثال
my_text = "Artificial intelligence is the simulation of human intelligence processes by machines. These processes include learning and reasoning. AI is used in many fields to improve efficiency."
print("Summary:", summarize_text(my_text))

