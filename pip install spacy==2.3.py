pip install spacy==2.3.0
python -m spacy download en_core_web_md

import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Define the knowledge base
faq_knowledge_base = {
    "What is the syllabus for CLAT 2025?":
        "The CLAT 2025 syllabus includes English, Current Affairs including GK, Legal Reasoning, Logical Reasoning, and Quantitative Techniques.",
    "How many questions are there in the English section?":
        "There are approximately 28–32 questions in the English section.",
    "Give me last year’s cut-off for NLSIU Bangalore.":
        "Last year's cut-off for NLSIU Bangalore was around AIR 114 for general category.",
    "When is the CLAT exam?":
        "CLAT 2025 is tentatively scheduled for December 2024.",
    "What is the duration of the CLAT exam?":
        "The exam duration is 2 hours."
}

# Function to get top N matches based on semantic similarity
def get_top_matches(user_input, knowledge_base, top_n=3):
    user_doc = nlp(user_input)
    results = []
    for question, answer in knowledge_base.items():
        similarity = user_doc.similarity(nlp(question))
        results.append((question, answer, similarity))
    
    # Sort by similarity score in descending order and return top N
    results.sort(key=lambda x: x[2], reverse=True)
    return results[:top_n]

# Main loop for continuous interaction
while True:
    user_input = input("Ask me something about CLAT (type 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Exiting the chatbot. Goodbye!")
        break
    elif user_input.strip() == '':
        print("No query provided. Please ask a question about CLAT.")
    else:
        top_matches = get_top_matches(user_input, faq_knowledge_base)
        if top_matches:
            best_answer = top_matches[0][1]
            print("\nBot’s Response:")
            print(best_answer)
            print("\nTop Similar FAQs:")
            for idx, (q, a, score) in enumerate(top_matches, 1):
                print(f"{idx}. {q}")
        else:
            print("No matching FAQs found.")