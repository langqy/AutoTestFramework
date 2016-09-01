# -*- coding: utf-8 -*-
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

import config


def db_connect():
    # 读取配置，链接数据库，返回session
    db_con = config.DefaultConfig().db_connect
    db_session = sessionmaker(bind=create_engine(db_con))
    return db_session()

# todo
# 数据库基本库


def db_oracle_connect():
    db_con = config.DefaultConfig().db_connect
    print db_con
    db_engine = create_engine('oracle://' + db_con)
    db_session = sessionmaker(bind=db_engine)
    return db_session
