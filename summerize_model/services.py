from transformers import BartForConditionalGeneration, BartTokenizer

class TransformerService:
    def __init__(self):
        self.model_name = 'facebook/bart-large-cnn'
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)

    def summarize(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
