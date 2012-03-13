#coding=utf-8
from math import tanh
import sqlite3

class searchnet:
    def __init__(self, dbname):
       self.con = sqlite3.connect(dbname)

    def __del__(self):
       self.con.close()

    def make_tables(self):
        self.con.execute('drop table hiddennode')
        self.con.execute('drop table wordhidden')
        self.con.execute('drop table hiddenurl')
        self.con.execute('create table hiddennode(create_key)')
        self.con.execute('create table wordhidden(fromid, toid, strength)')
        self.con.execute('create table hiddenurl(fromid, toid, strength)')
        self.con.commit()

    def get_strength(self, fromid, toid, layer):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.con.execute('select strength from %s where fromid = %d and toid = %d'%(table, fromid, toid)).fetchone()
        #连接不存在的情况下返回默认值
        if not res:
            #单词层到隐藏层
            if layer == 0: return -0.2
            #单词层到url层
            if layer == 1: return 0
        return res[0]

    def set_strength(self, fromid,toid, layer, strength):
        if layer == 0: 
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.con.execute('select rowid from %s where fromid = %d and toid = %d'%(table, fromid, toid)).fetchone()
        if not res:
            self.con.execute('insert into %s (fromid, toid, strength) values (%d, %d, %f)'%(table, fromid, toid, strength))
        else:
            rowid = res[0]
            self.con.execute('update %s set strength = %f where rowid = %d'%(table, strength, rowid))

    def generate_hidden_node(self, word_ids, urls):
        if len(word_ids) > 3:
            return None
        #检查我们是否已经为这组单词建好了一个节点
        create_key = '_'.join(sorted([str(wi) for wi in word_ids]))
        res = self.con.execute("select rowid from hiddennode where create_key='%s'"%create_key).fetchone()
        if not res:
            cur = self.con.execute("insert into hiddennode (create_key) values ('%s')"%create_key)
            hidden_id = cur.lastrowid
            #set default weight
            for word_id in word_ids:
                self.set_strength(word_id, hidden_id, 0, 1.0/len(word_ids))
            for url_id in urls:
                self.set_strength(hidden_id, url_id, 1, 0.1)
            self.con.commit()
                    


