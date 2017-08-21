import os
from pathlib import Path


class doc_service(object):
    """Doc_service"""
    doc_folder = Path('./MDdocs')
    docs = []

    def __init__(self):
        docs = []
        #print(self.doc_folder)
        for x in self.doc_folder.glob('**/*.md'):
            print(x.name)
            f = x.open()
            self.docs.append({'title':x.name,'text':f.read()[0:100]})

    def fetchall(self):
        return self.docs

