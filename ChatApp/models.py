import pymysql
from flask import Flask, abort
from util.DB import DB

# このモジュール関係についての調査が必要。Flaskではないモジュールを別途インストールする必要がある？？

class dbConnect:
    def createUser(id, firstname, lastname, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (id, firstname, lastname, email, password) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(sql, (id, firstname, lastname, email, password))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()
    # UserIdを検索キーにしてグループ一覧を取得
    def getChannel():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            # INNER JOIN のSQL分要確認
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            groups = cur.fetchall()
            return groups
        except Exception as e:
            print(e)
        finally:
            cur.close()

    # グループ名称を検索キーにしてグループを取得（既にそのグループ名が存在しているかどうか確認）
    def getGroupByName(group_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            # INNER JOIN のSQL分要確認
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (group_name))
            group = cur.fetchone()
            return group
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()
    
    def addGroup(newgroupName, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (name, uid) VALUES (%s, %s);"
            cur.execute(sql, (newgroupName, uid))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def updateGroup(groupId, groupName):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels (groupName) VALUES (%s) WHERE groupId = %s;"
            cur.execute(sql, (groupName, groupId))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def addUserGroup(groupId, users):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO user-group (user-id, group-id) VALUES (%s, %s);"
            for i in users:
                cur.execute(sql, (groupId, users[i]))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    # groupIDからグループ名称を取得
    def getGroupByGroupId(groupId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE gid=%s;"
            cur.execute(sql, (groupId))
            group = cur.fetchone()

            sql = "SELECT * FROM user-group WHERE gid=%s;"
            cur.execute(sql, (groupId))
            gusers = cur.fetchall()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    # groupIDを検索条件として、userGroupテーブルに存在しているかどうか
    def getUsersByGroupID(groupId):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM user-group WHERE gid=%s;"
            cur.execute(sql, (groupId))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def getMaxGroupId():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT MAX(groupId) FROM channels;"
            cur.execute(sql)
            maxId = cur.fetchone()
            return maxId
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def deleteChannel(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id = %s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def getMessagesByChannel(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT messages.id, message, messages.uid, users.firstname, users.lastname FROM messages INNER JOIN users ON messages.uid = users.id WHERE cid = %s ORDER BY messages.id ASC;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(e)
            abort(500)
        finally:
            cur.close()

    