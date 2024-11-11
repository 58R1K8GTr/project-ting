from .file_management import txt_importer


def process(path_file, instance) -> None:
    """Aqui irá sua implementação"""
    news = txt_importer(path_file)
    for index in range(len(instance)):
        old_process = instance.search(index)
        if old_process['nome_do_arquivo'] == path_file:
            return
    new_process = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(news),
        'linhas_do_arquivo': news,
    }
    instance.enqueue(new_process)
    print(new_process)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
