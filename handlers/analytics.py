from handlers.database import DatabaseHandler


def increase_view_count(route: str) -> None:
    """
    Takes current route and add one view to database.
    :param route:
        Takes the current route
    :return:
    """
    db = DatabaseHandler('blog_framework.db')
    query = """ INSERT INTO analytics(route) VALUES(?)
    """
    db.execute_insert_query(query, (route, ))
