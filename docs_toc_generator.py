import os


def get_toc_list(doc_path):
    toc_list = []
    for path, dirs, files in os.walk(doc_path):
        print('===', path, dirs, files)
        if path not in ['docs', f'docs{os.sep}images']:
            toc_list.append(f'- [{path}]({os.path.join(path, path).replace(os.sep, "/")})')
        for file_name in files:
            file_path = os.path.join(path, file_name)
            url_path = file_path.replace(os.sep, '/')
            if file_name.endswith('.md'):  # 只处理.md
                toc_list.append(f"{' ' * 2 * file_path.count(os.sep)}" + f'- [{file_name}]({url_path})')
    return toc_list


def get_h1_line(md_path):
    with open(md_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line.startswith('# '):
                yield line.lstrip('# ').rstrip('\n')


for _ in get_toc_list('docs'):
    print(_)

print('alter toc in readme.md after last ---')

readme_filename = 'README.md' if 'README.md' in os.listdir('.') else 'readme.md'


def alter_readme_toc(file, new_h1_list):
    with open(file, "w", encoding="utf-8") as f:
        f.write('\n'.join(new_h1_list))


alter_readme_toc(readme_filename, get_toc_list('docs'))
