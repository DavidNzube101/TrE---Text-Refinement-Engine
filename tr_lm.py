import numpy as np
from . import TrLMSentenceSpliter as ss
import re
import random
import json
import os

class TrLM:
    """The TrLM Model finetuned for creative & literal works"""
    def __init__(self, prompt):
        self.prompt = prompt
    
    def refinePrompt(self):

        class Summarizer:
            def __init__(self, document):
                self.document = document
                self.sentences = ss.split_sentences(self.document)
                self.sentence_importance = [len(sentence.split()) for sentence in self.sentences]

            def compute_importance_scores(self):
                return self.sentence_importance

            def compute_baseline(self, importance_scores):
                return np.mean(importance_scores)

            def compute_adaptive_difference(self, importance_scores):
                baseline = self.compute_baseline(importance_scores)
                return [abs(score - baseline) for score in importance_scores]

            def generate_summary(self, threshold=random.choice([0.5, 0.6, 0.7])):
                importance_scores = self.compute_importance_scores()
                adaptive_diff_scores = self.compute_adaptive_difference(importance_scores)
                summary = [self.sentences[i] for i, score in enumerate(adaptive_diff_scores) if score > threshold]
                return summary

        class Paraphraser:
            """Paraphrases words in the document"""
            def __init__(self, document):
                self.document = document
                # Define a list of verbs and their corresponding synonyms.
                # os.getcwd()
                _verbs = open("data\\trlm_verbs.bet", "r", encoding="utf-8").read()



                self.verb_synonyms = json.loads(_verbs)

                

            def tokenizer(self):
                # Tokenize the text into words
                words = re.findall(r'\b\w+\b', self.document.lower())  # Convert to lowercase for case-insensitive matching
                return words

            def verbs_identifier(self, words):
                # Identify verbs within the text
                verbs = [word for word in self.tokenizer() if word in self.verb_synonyms]
                return verbs

            def generate_paraphrased(self):
                # Randomly select a synonym and replace the verb
                new_text = self.document
                verbs = self.verbs_identifier(new_text)
                for verb in verbs:
                    synonyms = self.verb_synonyms.get(verb, [verb])  # Use the verb itself if no synonyms are available
                    random_synonym = random.choice(synonyms)
                    new_text = re.sub(r'\b{}\b'.format(verb), random_synonym, new_text, count=1)

                return new_text

        # Sample document
        samp_text = """ Natural language processing (NLP) is a field of artificial intelligence. It focuses on the interaction between computers and humans through natural language. It is used in various applications such as chatbots, sentiment analysis, and machine translation. NLP algorithms process and analyze text data to derive meaning and enable communication.
        """
        # input("Your Text: ")


        # Create the TextSummarizer instance
        summarizer = Summarizer(self.prompt)

        # Generate a summary
        if (len(re.findall(r'\b\w+\b', samp_text))) < 3:
            summary = f"{summarizer.generate_summary()}"
            # _ = "Just Perfect!"

        elif (len(re.findall(r'\b\w+\b', samp_text))) < 10:
            summary = f"{summarizer.generate_summary()}"
            # _ = "Just Perfect!"

        elif (len(re.findall(r'\b\w+\b', samp_text))) < 20:
            summary = f"{summarizer.generate_summary()}"
            # _ = "Just Perfect!"

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 30:
            summary = summarizer.generate_summary(threshold=1)

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 50:
            summary = summarizer.generate_summary(threshold=1)

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 75:
            summary = summarizer.generate_summary(threshold=3)

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 150:
            summary = summarizer.generate_summary(threshold=10)

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 500:
            summary = summarizer.generate_summary(threshold=15)

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 750:
            summary = summarizer.generate_summary(threshold=25)

        elif (len(re.findall(r'\b\w+\b', samp_text))) > 1000:
            summary = summarizer.generate_summary(threshold=25)

        else:
            summary = summarizer.generate_summary()

        summary = "\n".join(summary)

        ph = Paraphraser(summary)
            
        refinedText = ph.generate_paraphrased()

        # Length of words before the process
        length_before = ((len(re.findall(r'\b\w+\b', self.prompt))))
        
        # Length of words after the process
        length_after = ((len(re.findall(r'\b\w+\b', refinedText))))

        # Summary Rate(Content Reduction Factor)
        try:
            CRF = round( (( ( int(length_before) - int(length_after) ) / int(length_before) ) * 100), 1) 
        except Exception:
            CRF = "-" 
            
        CRF = f"{str(CRF)}%"

        if (refinedText == "") or (refinedText == " ") or (refinedText == "\n"):
            refinedText = "Sorry, could'nt process prompt. This can be caused be caused by a number of factors: ◾ Prompt was either empty or null ◾ Prompt was too short to be refined i.e. prompt < 10 words ◾ Internal Server Error - That's on us ◾ Fault is from our side. Click the thumbs down button on the right panel."
            CRF = "-"



        return [refinedText, length_before, length_after, CRF]

    def advanceRefineText(self, threshold="Default", tone="Default", refinementStyle="PANDS"):
        try:
            if False:
                pass
            
            else:
                if threshold == "Default":
                    threshold = random.choice([0.5, 0.6, 0.7])
                    
                class SummarizerAD:
                    def __init__(self, document):
                        self.document = document
                        self.sentences = ss.split_sentences(self.document)
                        self.sentence_importance = [len(sentence.split()) for sentence in self.sentences]

                    def compute_importance_scores(self):
                        return self.sentence_importance

                    def compute_baseline(self, importance_scores):
                        return np.mean(importance_scores)

                    def compute_adaptive_difference(self, importance_scores):
                        baseline = self.compute_baseline(importance_scores)
                        return [abs(score - baseline) for score in importance_scores]

                    def generate_summary(self, threshold=threshold):
                        importance_scores = self.compute_importance_scores()
                        adaptive_diff_scores = self.compute_adaptive_difference(importance_scores)
                        summary = [self.sentences[i] for i, score in enumerate(adaptive_diff_scores) if score > threshold]
                        return summary

                class ParaphraserAD:
                    """Paraphrases words in the document"""
                    def __init__(self, document):
                        self.document = document
                        # Define a list of verbs and their corresponding synonyms.
                        # os.getcwd()
                        _verbs = open("data\\trlm_verbs.bet", "r", encoding="utf-8").read()
                        _verbs_c = open("data\\tones\\trlm_verbs_casual.bet", "r", encoding="utf-8").read()
                        _verbs_p = open("data\\tones\\trlm_verbs_professional.bet", "r", encoding="utf-8").read()
                        _verbs_s = open("data\\tones\\trlm_verbs_shakespeare.bet", "r", encoding="utf-8").read()



                        if tone == "Casual":
                            self.verb_synonyms = json.loads(_verbs_c)
                        elif tone == "Professional":
                            self.verb_synonyms = json.loads(_verbs_p)
                        elif tone == "Playwright - Shakespare":
                            self.verb_synonyms = json.loads(_verbs_s)
                        else:
                            self.verb_synonyms = json.loads(_verbs)

                        

                    def tokenizer(self):
                        # Tokenize the text into words
                        words = re.findall(r'\b\w+\b', self.document.lower())  # Convert to lowercase for case-insensitive matching
                        return words

                    def verbs_identifier(self, words):
                        # Identify verbs within the text
                        verbs = [word for word in self.tokenizer() if word in self.verb_synonyms]
                        return verbs

                    def generate_paraphrased(self):
                        # Randomly select a synonym and replace the verb
                        new_text = self.document
                        verbs = self.verbs_identifier(new_text)
                        for verb in verbs:
                            synonyms = self.verb_synonyms.get(verb, [verb])  # Use the verb itself if no synonyms are available
                            random_synonym = random.choice(synonyms)
                            new_text = re.sub(r'\b{}\b'.format(verb), random_synonym, new_text, count=1)

                        return new_text

                                    
                if refinementStyle == "Just Paraphase":

                    phad = ParaphraserAD(self.prompt)

                    refinedTextAD = phad.generate_paraphrased()

                elif refinementStyle == "Just Summarize":
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    refinedTextAD = adsummary

                elif refinementStyle == "Tenses - Past tense":
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    phad = ParaphraserAD(adsummary)

                    refinedTextAD = "Tenses and Voices coming soon..."

                elif refinementStyle == "Tenses - Present tense":
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    phad = ParaphraserAD(adsummary)

                    refinedTextAD = "Tenses and Voices coming soon..."

                elif refinementStyle == "Tenses - Future tense":
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    phad = ParaphraserAD(adsummary)

                    refinedTextAD = "Tenses and Voices coming soon..."

                elif refinementStyle == "Voices - Active Voice":
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    phad = ParaphraserAD(adsummary)

                    refinedTextAD = "Tenses and Voices coming soon..."

                elif refinementStyle == "Voices - Passive Voice":
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    phad = ParaphraserAD(adsummary)

                    refinedTextAD = "Tenses and Voices coming soon..."

                        
                else:
                    summarizerAD = SummarizerAD(self.prompt)

                    adsummary = summarizerAD.generate_summary()

                    adsummary = "\n".join(adsummary)

                    phad = ParaphraserAD(adsummary)

                    refinedTextAD = phad.generate_paraphrased()

                # Length of words before the process
                length_before = ((len(re.findall(r'\b\w+\b', self.prompt))))
                
                # Length of words after the process
                length_after = ((len(re.findall(r'\b\w+\b', refinedTextAD))))

                # Summary Rate(Content Reduction Factor)
                try:
                    CRF = round( (( ( int(length_before) - int(length_after) ) / int(length_before) ) * 100), 1) 
                except Exception:
                    CRF = "-"
                    
                CRF = f"{str(CRF)}%"

                if (refinedTextAD == "") or (refinedTextAD == " ") or (refinedTextAD == "\n"):
                    refinedTextAD = "Sorry, could'nt process prompt. This can be caused be caused by a number of factors: ◾ Prompt was either empty or null ◾ Prompt was too short to be refined i.e. prompt < 10 words ◾ Internal Server Error - That's on us ◾ Fault is from our side. Click the thumbs down button on the right panel."
                    CRF = "-"



                return [refinedTextAD, length_before, length_after, CRF]

        except Exception as ed:
            print(f"The error-> '{ed}' <-")
            return [random.choice(["An error has occured!\nPlease Try again", "Scarab is having problems, please try again later", "An error has occured and this might be due to your `TrE` choice. Please try again with a different engine."]), "-", "-", "-"]