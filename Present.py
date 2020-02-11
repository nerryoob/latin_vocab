def pres_stem(word):
  return word[0][:-1]

def pres_end(word):
  conj = word[5]
  if conj == 'verb 3':
    return ['o','is','it','imus','itis','unt']
  else:
    return ['s','t','mus','tis','unt']

def present(word):
  return [sum(i) for i in zip(pres_stem(word),pres_end(word))]

