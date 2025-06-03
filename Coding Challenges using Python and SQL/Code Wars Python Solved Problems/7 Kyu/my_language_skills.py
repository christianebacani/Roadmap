# Question: My Language Skills
# Categories: 7 Kyu

def my_languages(results: dict[str, int]) -> list[str]:
    sorted_results = sorted(list(results.values()), reverse=True)
    new_results = {}

    for i in range(len(sorted_results)):
        for language, score in results.items():
            if sorted_results[i] == score:
                new_results[language] = score
    
    results = new_results
    answer = []

    for language, score in results.items():
        if score >= 60:
            answer.append(language)
    
    return answer