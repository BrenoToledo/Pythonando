# INCLUDES
from Database import JasonDB as db
from rich import print as rprint
import rich

from rich.console import Console

console = Console()


def merge_dict(dict_one, dict_two):
    merged_dict = dict_one | dict_two
    console.log(merged_dict, log_locals=True)


merge_dict({'id': 1}, {'name': 'Ashutosh'})

print(help(rich))
# Exibição na Tela

class ViewCategoria():
    
    def __init__(self):
        rprint(db.ler())
        
    def __str__(self):
        rprint("[italic red]Hello[/italic red] World!", locals())


tela_1 = ViewCategoria()