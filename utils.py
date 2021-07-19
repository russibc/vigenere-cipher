class Utils:
    def split_text(text, key_size):
        split_text = []
        for index in range(0, len(text), key_size):
            split_text.append(text[index: index + key_size])

        return split_text
