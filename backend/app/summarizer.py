from transformers import pipeline, AutoTokenizer

# Use Pegasus-XSum for best free summarization quality
MODEL_NAME = 'google/pegasus-xsum'
summarizer = pipeline('summarization', model=MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

MAX_TOKENS = 512  # Pegasus-XSum max tokens

def chunk_text_by_tokens(text, max_tokens=MAX_TOKENS):
    words = text.split()
    chunks = []
    current_chunk = []
    current_len = 0
    for word in words:
        word_tokens = tokenizer.tokenize(word)
        if current_len + len(word_tokens) > max_tokens:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_len = 0
        current_chunk.append(word)
        current_len += len(word_tokens)
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    return chunks

def generate_summary(text, max_length=180, min_length=60, do_sample=False):
    # Truncate to max tokens
    tokens = tokenizer.tokenize(text)
    if len(tokens) > MAX_TOKENS:
        text = tokenizer.decode(tokenizer.encode(text)[:MAX_TOKENS])
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']

def summarize_long_text(text, max_chunks=5):
    chunks = chunk_text_by_tokens(text)
    if len(chunks) > max_chunks:
        chunks = chunks[:max_chunks]
    summaries = []
    for i, chunk in enumerate(chunks):
        if not chunk.strip():
            continue
        try:
            print(f"Summarizing chunk {i+1}/{len(chunks)} (tokens: {len(tokenizer.tokenize(chunk))})")
            summaries.append(generate_summary(chunk))
        except Exception as e:
            print(f"Error summarizing chunk {i+1}: {e}")
            summaries.append("[Error summarizing chunk]")
    if len(summaries) > 1:
        try:
            return generate_summary(' '.join(summaries))
        except Exception as e:
            return ' '.join(summaries)
    return summaries[0] if summaries else '' 