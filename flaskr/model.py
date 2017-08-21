import os
from pathlib import Path

doc_folder = Path('../MDdocs')

class doc_service(object):
    """Doc_service"""
    docs = []

    def __init__(self):
        docs = []
        for x in doc_folder.glob('**/*.md'):
            f = x.open()
            self.docs.append({'title':x.name,'text':f.read()[0:100]})

    def fetchall(self):
        return self.docs

