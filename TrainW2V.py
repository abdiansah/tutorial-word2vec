#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:50:11 2020

@author: abdiansah
"""

import gensim, logging
import os, re, sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                # pra-pengolahan
                line = line.lower()                         # lowercase
                                                            # stopword
                line = re.sub(r'[0-9]|[^\w\s\-]', '', line) # hanya huruf yang diproses
                line = re.sub(r'nya\b','',line)             # hilangkanya akhiran -nya

                yield line.split()

def latih(folder, nama_model):
    sentences = MySentences(folder) # a memory-friendly iterator

    # TRAINING
    model = gensim.models.Word2Vec(sentences, min_count=5, workers=4)

    # RESUME TRAINING
    #model = gensim.models.Word2Vec.load(nama_model)
    #model.train(sentences, total_examples=model.corpus_count, epochs=model.epochs)

    model.save(nama_model)
    print('\nPelatihan Word2Vec selesai...')
    print('Data latih\t: {}'.format(folder))
    print('Nama Model\t: {}'.format(nama_model))

if __name__ == "__main__":
   latih(sys.argv[1], sys.argv[2])

