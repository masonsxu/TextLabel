import os
import html
import pandas as pd
from tqdm.std import trange
from create_database import run_sql


def get_data(folderpath_origin):
    filename = os.listdir(folderpath_origin)
    merged_data_list = []
    print('----------------开始合并所有文件中的数据----------------')
    punc = u' \t\n\r\x0b\x0c\xc2\xa0\u2002\u200b\u3000\ue627'
    trans = str.maketrans({key: None for key in punc})  # 删除特殊字符
    for name_index in trange(len(filename)):
        name = filename[name_index]
        if name[-3:] == 'csv':
            path = folderpath_origin + '/' + name
            df = pd.read_csv(path, sep=',', encoding='utf8', skiprows=1)
            for row_data in df.values.tolist():
                new_row = []
                for columns_data in row_data[1:]:
                    new_row.append(
                        html.unescape(html.unescape((str(columns_data))))
                        .translate(trans)
                        .replace('--', '0')
                    )
                merged_data_list.append(new_row)

        else:
            print('\n----------------不是目标文件，跳过当前文件。----------------')
    return merged_data_list


def save_data_sql(folderpath_origin):
    merged_data_list = get_data(folderpath_origin)
    engine = run_sql.create_connection()
    with engine.connect() as conn:
        try:
            conn.execute('SELECT Count(1) FROM `textLabel`')
            print('----------------数据库中已存在表，请删除后重新运行！！！----------------')
        except:
            run_sql.run_sqlite()
            sql_df = pd.DataFrame(
                merged_data_list,
                columns=[
                    'media_type',
                    'media_name',
                    'title',
                    'abstract',
                    'author',
                    'number_of_similar_articles',
                    'original_link',
                    'keyword_frequency',
                    'whether_the_keyword_appears_in_the_title',
                    'topic_term',
                    'emotional_attribute',
                    'emotional_score',
                    'mention_region',
                    'release_time',
                    'micro_Number_of_blog_fans',
                    'number_of_reads',
                    'number_of_likes',
                    'original_author',
                    'number_of_comments',
                    'number_of_reposts',
                ],
            )
            sql_df.to_sql('textLabel', engine, if_exists='append', index=False)


if __name__ == '__main__':
    folderpath_origin = 'data'
    save_data_sql(folderpath_origin)
