import os


h1_list = []


def get_h1_list(doc_path):
    for path, dirs, files in os.walk(doc_path):
        for file_name in files:
            file_path = os.path.join(path, file_name)
            if file_name.endswith('.md'):  # 只处理.md
                title = os.path.split(file_name)[1].split('.')[0]
                h1_list.append(f'- [{title}]({file_path})')
                h1_in_md = get_h1_line(file_path)
                if h1_in_md:  # 过滤没有h1的
                    h1_list.append(
                        f"{' ' * 2 * file_path.count(os.sep)}" + f'- [{h1_in_md}]({file_path}#{h1_in_md})')
    return h1_list


def get_h1_line(md_path):
    with open(md_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line.startswith('# '):
                return line.lstrip('# ').rstrip('\n')


for _ in get_h1_list('docs'):
    print(_)

