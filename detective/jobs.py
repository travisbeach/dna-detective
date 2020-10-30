import os
from django.conf import settings
from Bio import SeqIO
import random

class Searcher: 

    def search_genbank(self, query):
        """
            Args:
                query: string to search for

            Returns:
                Tuple representing (name, index, protein, and description)

        """

        # Randomize the order of files we are analyzing
        files = os.listdir(self._get_base_file_path())
        random.shuffle(files)
        for filename in files:
            path = os.path.join(settings.BASE_DIR, 'data', filename)
            # parse file
            for i, record in enumerate(SeqIO.parse(path, 'genbank')):
                sequence = str(record.seq)
                index = sequence.find(query)
                # if there is a match, we need to use the index to look up which protein
                # the rection encodes
                if index > -1:
                    result = self._translate_index_to_protein(index, record)
                    if result:
                        return result
        return (None, None, None, None)

    def _translate_index_to_protein(self, index, record):
        """
            Args:
                index: int,  index of the start of the query string
                record: SeqRecord, datastructure containing the parsed file

            Returns:
                Tuple representing (name, index, protein, and description) or null if no match

        """
        for feature in record.features:
            if feature.type == 'CDS':
                #need to verify that the starting index of the match corresponds to a protein 
                if (feature.location.start <= index <= feature.location.end):
                    protein  = feature.qualifiers['protein_id'][0]
                    return (record.name, index, protein, record.description)
        return None

    def _get_base_file_path(self):
        return os.path.join(settings.BASE_DIR, 'data')




