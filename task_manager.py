from database import Database

class TaskManager:
    def __init__(self, db):
        self.db = db

    def create_task(self, title, description, date):
        query = """
        CREATE (t:Task {title: $title, description: $description, date: $date})
        RETURN t
        """
        parameters = {'title': title, 'description': description, 'date': date}
        return self.db.execute_query(query, parameters)

    def get_task(self, title):
        query = """
        MATCH (t:Task {title: $title})
        RETURN t
        """
        parameters = {'title': title}
        return self.db.execute_query(query, parameters)

    def update_task(self, title, new_title=None, new_description=None, new_date=None):
        query = """
        MATCH (t:Task {title: $title})
        SET t.title = coalesce($new_title, t.title),
            t.description = coalesce($new_description, t.description),
            t.date = coalesce($new_date, t.date)
        RETURN t
        """
        parameters = {'title': title, 'new_title': new_title, 'new_description': new_description, 'new_date': new_date}
        return self.db.execute_query(query, parameters)

    def delete_task(self, title):
        query = """
        MATCH (t:Task {title: $title})
        DELETE t
        RETURN COUNT(t) AS deleted
        """
        parameters = {'title': title}
        return self.db.execute_query(query, parameters)