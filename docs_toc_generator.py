import os


h1_list = []


def get_h1_list(doc_path):
    for path, dirs, files in os.walk(doc_path):
        for file_name in files:
            file_path = os.path.join(path, file_name)
            url_path = file_path.replace(os.sep, '/')
            if file_name.endswith('.md'):  # 只处理.md
                title = os.path.split(file_name)[1].split('.')[0]
                h1_list.append(f'- [{title}]({file_path})')
                for h1_in_md in get_h1_line(file_path):
                    if h1_in_md:  # 过滤没有h1的
                        h1_list.append(
                            f"{' ' * 2 * file_path.count(os.sep)}" + f'- [{h1_in_md}]({url_path}#{h1_in_md})')
    return h1_list


def get_h1_line(md_path):
    with open(md_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            if line.startswith('# '):
                yield line.lstrip('# ').rstrip('\n')


for _ in get_h1_list('docs'):
    print(_)

print('alter toc in readme.md after last ---')

readme_filename = 'README.md' if 'README.md' in os.listdir('.') else 'readme.md'


def alter_readme_toc(file, new_h1_list):
    file_bak = "%s.bak" % file
    with open(file, "r", encoding="utf-8") as f1:
        content = f1.read()
    r_loc = content.rfind('\ntoc\n---')
    content = content[:r_loc] +'\ntoc\n---\n\n' + '\n'.join(new_h1_list)

    # 删除源文件 + 备份
    if os.path.exists(file_bak):
        os.remove(file_bak)
    os.rename(file, file_bak)
    
    with open(file,"w",encoding="utf-8") as f:
        f.write(content)
 
alter_readme_toc(readme_filename, h1_list)