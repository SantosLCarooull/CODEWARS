def reverse_words(text):
    return " ".join(word[::-1] for word in text.split((" "))) #.join add espaço ##[::-1] fatiamento que inverte ###.split serapara o texto em palavras
  
reverse_words("Abacate é gostoso")

