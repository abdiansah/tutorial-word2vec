# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:34:59 2020

@author: Abdiansah
"""

# import modules & set up logging
import gensim, logging, sys
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def tes(nama_model):
    print('Load model...')
    model = gensim.models.Word2Vec.load(nama_model)
    print('Load model selesai.\n')

    while(1):
        kata = input('\nMasukan kata [ketik \'qqq\' untuk keluar]: ')
        if kata == 'qqq':
            break
        else:
            print('\nKata-kata yang mirip dengan kata \'{}\' adalah:'.format(kata.upper()))

            try:
                #print(model.wv.similarity('jokowi', 'soekarno'))
                #print(model.wv.most_similar(positive=['wanita', 'raja'], negative=['pria'], topn=5))
                #print(model.wv.similarity(kata, ))
                #print(model.wv.similar_by_word(kata, topn=5))
                hasil = model.wv.most_similar(kata, topn=5)
                i = 1
                for h in hasil:
                    #print('{}. {} = {:.2f}'.format(i, h[0],h[1]))
                    print('{}. {} ({:.2f}%)'.format(i, h[0],h[1]*100))
                    i+=1
            except:
                print('Kata \'{}\' tidak ada dalam kamus data'.format(kata.upper()))
            
if __name__ == "__main__":
   tes(sys.argv[1])
