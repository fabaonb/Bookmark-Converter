# -*- coding: utf-8 -*-
import sys
import os
import json
import sqlite3

HTML_HEADER = '''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
'''

HTML_FOOTER = '''</DL><p>
'''

def convert_chrome_json(data):
    lines = []
    def process_folder(folder, indent='    '):
        lines.append(f'{indent}<DT><H3>{folder.get("name", "")}</H3>')
        lines.append(f'{indent}<DL><p>')
        for item in folder.get('children', []):
            if item.get('type') == 'url':
                url = item.get('url', '')
                name = item.get('name', '')
                lines.append(f'{indent}    <DT><A HREF="{url}">{name}</A>')
            elif item.get('type') == 'folder':
                process_folder(item, indent + '    ')
        lines.append(f'{indent}</DL><p>')
    
    roots = data.get('roots', {})
    for root_key in ['bookmark_bar', 'other', 'synced']:
        if root_key in roots and roots[root_key].get('children'):
            process_folder(roots[root_key])
    return '\n'.join(lines)

def convert_firefox_sqlite(db_path):
    lines = []
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, dateAdded, lastModified FROM moz_bookmarks WHERE type = 2 AND parent = 0")
    
    def process_folder(parent_id, indent='    '):
        cursor.execute("SELECT id, title, type, fk, dateAdded, lastModified FROM moz_bookmarks WHERE parent = ?", (parent_id,))
        items = cursor.fetchall()
        for item in items:
            bm_id, title, bm_type, fk, date_added, last_modified = item
            if bm_type == 1:
                cursor.execute("SELECT url FROM moz_places WHERE id = ?", (fk,))
                url_row = cursor.fetchone()
                if url_row:
                    attrs = f' ADD_DATE="{date_added // 1000}"' if date_added else ''
                    lines.append(f'{indent}<DT><A HREF="{url_row[0]}"{attrs}>{title or ""}</A>')
            elif bm_type == 2:
                attrs = f' ADD_DATE="{date_added // 1000}" LAST_MODIFIED="{last_modified // 1000}"' if date_added and last_modified else ''
                lines.append(f'{indent}<DT><H3{attrs}>{title or ""}</H3>')
                lines.append(f'{indent}<DL><p>')
                process_folder(bm_id, indent + '    ')
                lines.append(f'{indent}</DL><p>')
    
    for root in cursor.fetchall():
        process_folder(root[0])
    conn.close()
    return '\n'.join(lines)

def detect_and_convert(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    try:
        if ext == '.json' or ext == '':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            data = json.loads(content)
            if 'roots' in data:
                return convert_chrome_json(data)
        elif ext in ['.sqlite', '.db']:
            return convert_firefox_sqlite(file_path)
        elif ext in ['.html', '.htm']:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
    except Exception as e:
        print(f"Error converting {file_path}: {e}")
    return None

def main():
    files = sys.argv[1:]
    if not files:
        print("Please drag and drop bookmark files onto this script.")
        input("Press Enter to exit...")
        return
    
    for file_path in files:
        if not os.path.isfile(file_path):
            continue
        content = detect_and_convert(file_path)
        if content:
            output_path = os.path.splitext(file_path)[0] + '_converted.html'
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(HTML_HEADER + content + '\n' + HTML_FOOTER)
            print(f"Converted: {file_path} -> {output_path}")
        else:
            print(f"Failed to convert: {file_path}")

if __name__ == '__main__':
    main()
