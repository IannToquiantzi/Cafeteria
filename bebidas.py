def validate_input(input_str):
  #Se eliminan los espacios en blanco
  input_str = input_str.replace(" ", "")
  parts = input_str.split(",")

  #Se Valida el nombre del artículo
  article_name = parts[0]
  if not article_name.isalpha():
    return False

  if len(article_name) < 2 or len(article_name) > 15:
    return False

  #Se Validan los tamaños
  sizes = parts[1:]
  if not sizes:
    return False

  prev_size = 0
  for size in sizes:
    try:
      size_int = int(size)
      if size_int < 1 or size_int > 48 or size_int <= prev_size:
        return False
      prev_size = size_int
    except ValueError:
      return False

  return True
