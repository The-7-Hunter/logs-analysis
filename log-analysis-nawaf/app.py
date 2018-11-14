import psycopg2

DBname = "news"


def run_query(query):
    db = psycopg2.connect('dbname=' + DBname)
    c = db.cursor()
    c.execute(query)
    output = c.fetchall()
    db.close()
    return output


def top_articles():
    query = """
        SELECT articles.title, COUNT(*) AS number
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.id
        ORDER BY number DESC
        LIMIT 3;
    """
    result = run_query(query)
    print('\n1. What are the most popular three articles of all time?\n')
    for i in result:
        title = i[0]
        label = '" with ' + str(i[1]) + " views"
        print("- " + title + label)


def top_authors():
    query = """
        SELECT authors.name, COUNT(*) AS number
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.id
        ORDER BY number DESC
        LIMIT 3;
    """
    result = run_query(query)

    print('\n2. Who are the most popular article authors of all time?\n')

    for i in result:
        print('- ' + i[0] + ' with ' + str(i[1]) + " views")


def error_days():
    query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3)
          AS error_pers
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status like '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*100.0) / total.requests), 2)
         > 1.00)
        ORDER BY error_pers DESC;
    """

    result = run_query(query)
    print('\n3. On which days did more than 1% of requests lead to errors?\n')
    for i in result:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        print('\t' + date + " -- " + errors)
        print


print('\t---------------------------------')
print('\t     Executing Please Wait        ')
print('\t---------------------------------')
top_articles()
top_authors()
error_days()
