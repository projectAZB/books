from books import sqla_db as sqla


class Book(sqla.Model):
    __table_args__ = (sqla.UniqueConstraint('title', 'author', name='_title_author_uc'),)

    id = sqla.Column(sqla.Integer, primary_key=True)
    title = sqla.Column(sqla.String(250), nullable=False, index=True)
    author = sqla.Column(sqla.String(250), nullable=False)
    genre = sqla.Column(sqla.String(250))
