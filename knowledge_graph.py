from openai_api import *
from visualize_knowledge_graph import *
import ast

def get_prompt(text):
    messages = [
        {"role": "system", "content": """"
        You are a helper tool for a knowedge graph builder application. Your task is to extract entities and relationships from the text provided by the user. 
        Format the output in such a way that it can be directly parsed into Python lists. 
        The format should include:
        
        1. A list of **Entities** in Python list format.
        2. A list of **Relationships**, where each relationship is represented as a tuple in the format: (Entity 1, "Relationship", Entity 2).
        
        Here is the format to follow:
        
        Entities: ["Entity 1", "Entity 2", ..., "Entity N"]
        
        Relationships: [("Entity 1", "Relationship", "Entity 2"), ..., ("Entity X", "Relationship", "Entity Y")]
        
        Example Input:
        Extract entities and relationships from the following text:
        "Michael Jackson, born in Gary, Indiana, was a famous singer known as the King of Pop. He passed away in Los Angeles in 2009."
        
        Expected Output:
        
        Entities: ["Michael Jackson", "Gary, Indiana", "Los Angeles", "singer", "King of Pop", "2009"]
        
        Relationships: [
            ("Michael Jackson", "born in", "Gary, Indiana"), 
            ("Michael Jackson", "profession", "singer"), 
            ("Michael Jackson", "referred to as", "King of Pop"), 
            ("Michael Jackson", "passed away in", "Los Angeles"), 
            ("Michael Jackson", "date of death", "2009")
        ]
        """},
        {"role": "user", "content": f"Extract entities and relationship tuples from the following text:\n\n{text}\n\n"}
        ]
    return messages

def extract_entities_relationships(text):
    try:
        prompt = get_prompt(text)
        response = generate_response(prompt, max_tokens=900)
        return response
    except Exception as e:
        print(f"Error generating response: {e}")
        raise e

def parse_llm_response_content(content):
    # Split the output into entities and relationships sections
    entity_section = content.split("Entities:")[1].split("Relationships:")[0].strip()
    relationship_section = content.split("Relationships:")[1].strip()

    # Use ast.literal_eval to safely evaluate the string into Python lists
    entities = ast.literal_eval(entity_section)
    relationships = ast.literal_eval(relationship_section)
    
    return entities, relationships


def main():
    raw_text = "Sarah is an avid traveler who recently visited New York City. During her trip, she saw the Statue of Liberty, which was designed by Frédéric Auguste Bartholdi and completed in 1886. Sarah also visited the Empire State Building, which was completed in 1931 and was designed by Shreve, Lamb & Harmon. Sarah took a memorable photo in front of the Brooklyn Bridge, which was designed by John A. Roebling and completed in 1883. She also visited Central Park, a large public park in New York City."
    response = extract_entities_relationships(raw_text)
    entities, relationships = parse_llm_response_content(response)
    print(entities)
    print(relationships)
    plot_knowledge_graph(entities, relationships)

if __name__ == "__main__":
    main()
