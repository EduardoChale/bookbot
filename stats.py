def count_words(content):
    words=content.split()
    return len(words)
    
def count_character(content):
    updated_content=content.lower()
    character_dict={}
    for character in updated_content:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character]=1
    return character_dict 