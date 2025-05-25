# Question: Who is the killer?
# Categories: 7 Kyu

def killer(suspect_info: dict[str, str], dead: list[str]) -> str:
    for killer, list_of_person_they_saw in suspect_info.items():
        is_suspect = True

        for i in range(len(dead)):
            if dead[i] not in list_of_person_they_saw:
                is_suspect = False
                break
        
        if is_suspect:
            return killer