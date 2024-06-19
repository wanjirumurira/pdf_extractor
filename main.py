import fitz
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    print (len(doc))
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        text += page_text + "\n"  # Add a newline to separate page texts
    return (text )

def parse_question_and_answers(text):
    #questions = re.split(r'(?:Question\s*\d+\.|\d+\.|Q\d+:)', text)
    questions = re.split(r'(\bQuestion\s*\d+\.|\bQ\d+\.|\b\d+\))', text)

    #questions = re.split(r'(?:\d+\))', text)
    # print('questions')
    #print(questions)
    qa_pairs = []
    for question in questions[1:]:
        question_block = re.split(r'\n(?=[A-D]\))', question)
        print(len(question_block))
        if len(question_block) >= 2: 
            print(question_block)
            question_text = question_block[0].strip()
            answer_text = [question_block.strip() for ans in question_block[1:0]]
            #print('this is the answer block :', answer_text)        
            qa_pairs.append((question_text, answer_text))
            
        
    return qa_pairs
    

#print(extract_text_from_pdf("./test.pdf"))
pdf_text = extract_text_from_pdf("./test.pdf")
qa_pairs = parse_question_and_answers(pdf_text)
#print(qa_pairs)


