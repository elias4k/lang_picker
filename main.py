from time import sleep

try:
    json_file_path = "es.json"
    print("Ingrese la ruta del archivo:")
    origin_file_path = input()
    origin_file_path = origin_file_path.replace("\\", "/")
    with open(origin_file_path, encoding="utf8") as origin_file:
        text = origin_file.read()
        arr0 = text.split("@lang('")
        words = []
        for frase in arr0:
            word = frase.split("')")[0]
            words.append(word)
        words.pop(0)
        words = list(set(words))

        with open(json_file_path, "w", encoding="utf8") as json_file:

            if len(words) < 1:
                print("No encontré nada.")
            else:
                print("Esto fue lo que encontré:")
                json_file.write("{\n")
                for word in words:
                    print(word)
                    json_file.write('\t"' + word + '": ' + '"' + word + '",\n')
                json_file.write("}")

    print("\n\nListo, recuerda borrar la coma al final del último valor.")
except Exception as ex:
    print("Algo salió mal :'v")
    print(str(ex))




