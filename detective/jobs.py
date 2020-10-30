import os
from django.conf import settings
from Bio import SeqIO
import random

class Searcher: 

    def search_genbank(self, query):
        files = os.listdir(self.get_base_file_path())
        random.shuffle(files)
        for filename in files:
            path = os.path.join(settings.BASE_DIR, 'data', filename)
            for i, record in enumerate(SeqIO.parse(path, 'genbank')):
                sequence = str(record.seq)
                index = sequence.find(query)
                if index > -1:
                    result = self.translate_index_to_protein(index, record)
                    if result:
                        return result
        return self.get_not_found_tuple()

    def translate_index_to_protein(self, index, record):
        for feature in record.features:
            if feature.type == 'CDS':
                if (feature.location.start <= index <= feature.location.end):
                    protein  = feature.qualifiers['protein_id'][0]
                    return (record.name, index, protein, record.description)
        return None


    def get_not_found_tuple(self):
        return (None, None, None, None)

    def get_base_file_path(self):
        return os.path.join(settings.BASE_DIR, 'data')




