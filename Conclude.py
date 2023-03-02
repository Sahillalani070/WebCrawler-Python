"""
------------------------------------------------------------------------
[Conclude]
------------------------------------------------------------------------
Author:Sahil Lalani
File Name: Conclude.py
Version: 2020-07-18
------------------------------------------------------------------------
"""

# Import

from Container import Extract



# Functions

def Conclude(categories, file_names):
    """
    -------------------------------------------------------
    
    Use: Conclude(category, file_names)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    corpus = genCorpus(categories, file_names)
    corpus_length = len(corpus)
    print(corpus)


   # Write into file
    file_corpus = open("feature\\" + "corpus.txt", "w+", encoding="utf8")
    file_corpus_lenth = open("train\\" + "corpus_len.txt", "w+", encoding="utf8")

    file_corpus_lenth.write(str(corpus_length))

    for g in corpus:
       file_corpus.write(g + "\n")
    
    file_corpus.close()

    print("\n")
    for c in categories:

       category = c # Select current category
       counter = 1

       for i in file_names:
         word_list = Extract("dataset\\" + category + "\\" + i) # Get Word List
         binary_feature = genBinFeature(corpus, word_list)
         print(":: Category [{}] ~ File [{}] ::".format(category, i))
         print(binary_feature, "\n\n")


         # Write into file
         bin_file_name = "feature\\" + category + "\\" + category + "_bf" + str(counter) + ".txt"
         file_bf = open(bin_file_name, "w+", encoding="utf8")

         for k in range(len(corpus)):
            file_bf.write("{}\n".format(binary_feature[k]))

         file_bf.close()
         counter += 1

    # Iterating through categories
    for c in categories:

      category = c # Select current category
      counter = 1

      for j in file_names:
         word_list = Extract("dataset\\" + category + "\\" + j) # Get Word List
         wordlist_length = len(word_list)
         tf_feature = genTFreqFeature(corpus, word_list)
         print(":: Category [{}] ~ File [{}] ::".format(category, j))
         print(tf_feature, "\n\n")


         # Write into file
         length_file_name = "feature\\" + category + "\\" + category + "_len" + str(counter) + ".txt"
         tf_file_name = "feature\\" + category + "\\" + category + "_tf" + str(counter) + ".txt"

         file_len_tf = open(length_file_name, "w+", encoding="utf8")
         file_len_tf.write(str(wordlist_length))

         file_tf = open(tf_file_name, "w+", encoding="utf8")

         for l in range(len(corpus)):
            file_tf.write("{}\n".format(tf_feature[l]))

         file_tf.close()
         counter += 1


def genCorpus(categories, file_names):
    """
    -------------------------------------------------------
    Generate Text Corpus for the given categories

    Use: corpus = genCorpus(categories)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    corpus = []

   # Iterating through categories
    for c in categories:

       category = c # Select current category

       # Extract Data from Current Category
       for j in file_names:
         word_list = Extract("dataset\\" + category + "\\" + j) # Get Word List

         # Appending to corpus list
         for k in word_list:
            
            # Only append if already not in corpus
            if k not in corpus:
               corpus.append(k)

    return corpus



def genBinFeature(corpus, word_list):
    """
    -------------------------------------------------------
    Generate Binary Feature word list from passed in text
    corpus and word_list

    Use: binary_feature = genBinFeature(corpus, word_list)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    binary_feature = []

    for _ in range(len(corpus)):
      binary_feature.append(0)
      
    for j in range(len(corpus)):
      if corpus[j] in word_list:
         binary_feature[j] = 1

    return binary_feature



def genTFreqFeature(corpus, word_list):
    """
    -------------------------------------------------------
    Generate Binary Feature word list from passed in text
    corpus and word_list

    Use: TF_feature = genTFreqFeature(corpus, word_list)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    TF_feature = []

    for _ in range(len(corpus)):
      TF_feature.append(0)

    for i in range(len(corpus)):
      for j in range(len(word_list)):
         if corpus[i] == word_list[j]:
               TF_feature[i] += 1

    return TF_feature