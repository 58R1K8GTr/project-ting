def exists_word(word, instance):
    """Aqui irá sua implementação"""
    results = []
    for index in range(len(instance)):
        news = instance.search(index)
        result = {
            'palavra': word,
            'arquivo': news['nome_do_arquivo'],
            'ocorrencias': []
        }
        for number, line in enumerate(news['linhas_do_arquivo'], 1):
            if word.lower() in line.lower():
                result['ocorrencias'].append({'linha': number})
        if len(result['ocorrencias']) > 0:
            results.append(result)
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
