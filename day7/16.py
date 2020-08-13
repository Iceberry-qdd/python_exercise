def get_suffix(filename, has_dot=False):
    index = filename.rfind('.')
    if 0 < index < len(filename)-1:
        begin_index = index if has_dot else index+1
        return filename[begin_index:]
    else:
        return ''


if __name__ == "__main__":
    filename = str(input('filename='))
    print(get_suffix(filename, True))
