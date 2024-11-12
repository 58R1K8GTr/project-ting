from typing import TypedDict, NotRequired, Literal, Optional


class OccurrenceType(TypedDict):
    linha: int
    conteudo: str


class OccurrenceOptionalContentType(OccurrenceType):
    conteudo: NotRequired[str]


OccurrenceParamType = list[int | str]
KeysOccurrenciesType = list[Literal['linha'] | Optional[Literal['conteudo']]]


def filter_occurrencies(
    parameters: OccurrenceType, keys: KeysOccurrenciesType
) -> OccurrenceOptionalContentType:
    return {key: parameters[key] for key in keys}


def searches(word, instance, keys: KeysOccurrenciesType):
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
                result['ocorrencias'].append(filter_occurrencies(
                    {'linha': number, 'conteudo': line}, keys
                ))
        if len(result['ocorrencias']) > 0:
            results.append(result)
    return results


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    return searches(word, instance, ['linha'])


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    return searches(word, instance, ['linha', 'conteudo'])
