import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # WORK WITH CATEGORIES
    def get_categories(self):       # get all categories
        categories = self.cursor.execute(
            "SELECT id, category_name FROM categories;"
        )
        return categories.fetchall()

    def add_category(self, new_category):
        try:
            self.cursor.execute(
                "INSERT INTO categories (category_name) VALUES(?);",
                (new_category,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def rename_category(self, old_name, new_name):
        try:
            self.cursor.execute(
                "UPDATE categories SET category_name=? WHERE category_name=?;",
                (new_name, old_name)
            )
            self.conn.commit()
            return True
        except:
            return False

    def delete_category(self, name):
        try:
            self.cursor.execute(
                "DELETE FROM categories WHERE category_name=?;",
                (name,)
            )
            self.conn.commit()
            return True
        except:
            return False

    def check_category_exists(self, name):
        lst = self.cursor.execute(
            f"SELECT * FROM categories WHERE category_name=?",
            (name,)
        ).fetchall()
        if not lst:
            return True
        else:
            return False
    #with product
    def get_product(self):       
        categories = self.cursor.execute(
            "SELECT id, category_name FROM product;"
        )
        return categories.fetchall()

    def add_product(self, new_category):
        try:
            self.cursor.execute(
                "INSERT INTO product (category_name) VALUES(?);",
                (new_category,)
            )
            self.conn.commit()
            return True
        except:
            return False


    def delete_product(self, name):
        try:
            self.cursor.execute(
                "DELETE FROM product WHERE category_name=?;",
                (name,)
            )
            self.conn.commit()
            return True
        except:
            return False
