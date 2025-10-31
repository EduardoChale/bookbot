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

def sort_on(list_to_sort):
    return list_to_sort["num"]

def sorting_list(unsorted_list):
    sorted_list=[]
    for character in unsorted_list:
        temp_dict={}
        temp_dict["char"]=character
        temp_dict["num"]=unsorted_list[character]
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list