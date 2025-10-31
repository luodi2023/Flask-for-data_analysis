import os
import pandas as pd
from sqlalchemy import create_engine, Engine
from sqlalchemy.pool import QueuePool

# 创建数据库连接引擎
engine = create_engine(f'mysql+pymysql://LUODI:123456@192.168.3.6:3306/yueLaiZhong_canteen',
                       poolclass=QueuePool,
                       pool_size=10,
                       max_overflow=20,
                       pool_timeout=30,
                       pool_recycle=3600,
                       echo=False)


def generateDataFrameList(_engine: Engine) -> list:
    """
    从mysql数据库中获取一系列表并生成DataFrame对象列表
    """

    # SElECT * FROM * 列表

    query_tabs = []
    # Dataframe对象列表
    frames = []

    # SQL语句
    query_showTab = 'SHOW TABLES;'

    tab_frame = pd.read_sql_query(query_showTab, engine)

    # 生成SQL语句列表
    for tab in tab_frame.values:
        query_tabs.append('SELECT * FROM ' + tab[0] + ';')

    for st in query_tabs:
        frames.append(pd.read_sql_query(st, engine))
    # 列名重命名
    excel_path = r'E:\python_pro\flasky\data\悦来中餐厅数据.xlsx'
    excel_file = pd.ExcelFile(excel_path)
    sheet_count = len(excel_file.sheet_names)

    for i in range(sheet_count):
        frame = pd.read_excel(excel_path, sheet_name=excel_file.sheet_names[i])
        frames[i].columns = frame.columns

    return frames
