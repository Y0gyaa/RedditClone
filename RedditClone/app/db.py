import sqlite3

database = sqlite3.connect('reddit.db')
con = database.cursor()

def CreatePostsTable():
    con.execute('''
        CREATE TABLE POSTS (
         ID            INTEGER AUTOINCREMENT PRIMARY KEY,
         CONTENT       TEXT NOT NULL,
         POSTED_ON     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         UPVOTES       INT,
         DOWNVOTES     INT,
         AWARDS        TEXT
        );''')

#CreatePostsTable()


class DbStuff:
    def AddPost(new_post_content):
        print(new_post_content)
        try:
            content = new_post_content.content
            con.execute('''
            INSERT INTO POSTS (CONTENT)
            VALUES (%s);
            ''', content)
            #self.AddPost(new_post_content)
        except sqlite3.Error as error:
            print(error)
    
    def FetchAllPosts():
        try:
            con.execute('''SELECT * FROM POSTS;''')
        except sqlite3.Error as error:
            print(error)

    def EditPost(id,body):
        try:
            content_tuple = (body.content,id)
            con.execute('''
            UPDATE POSTS SET CONTENT = %s WHERE ID = %s;''', content_tuple)
        except sqlite3.Error as error:
            print(error)