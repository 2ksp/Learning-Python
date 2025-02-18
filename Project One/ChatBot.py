import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data:str):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for theQ in knowledge_base["questions"]:
        if theQ["questions"] == question:
            return theQ
        
def chat_bot():
    knowledge_base: dict = load_knowledge_base('TestBot.json')
    
    while True:
        user_input: str = input('You:')
        
        if user_input.lower() == 'quit':
            break
        
        best_match: str | None = find_best_match(user_input, [theQ["question"] for theQ in knowledge_base["questions"]])
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print('f Bot: {answer}')   
        else:
         print('Bot: I do not know the answer. Can you teach me?')
         new_answer: str = input('Type the answer or "skip" to skip it')

        if new_answer.lower() != 'skip':
            knowledge_base['questions'].append({"question": user_input, "answer": new_answer})
            save_knowledge_base('TestBot.json', knowledge_base)
            print('Bot: Thank you! I have learned something new')
                
if __name__== '__main__':
    chat_bot()
            
       
            
    
  
