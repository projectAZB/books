from books.db_api import DbApi


class TestBookDbApi:

    def test_book_db_api_one(self):
        DbApi.create_book(
            title='Jude the Obscure',
            author='Thomas Hardy',
            genre='Realist Fiction'
        )

        book = DbApi.get_book('Jude the Obscure')
        assert book.author == 'Thomas Hardy'
        assert book.genre == 'Realist Fiction'
        num_books = len(DbApi.get_all_books())
        assert num_books == 1

    def test_book_db_api_two(self):
        DbApi.create_book(
            title='Elective Affinities',
            author='Goethe',
            genre='Romanticism'
        )

        book = DbApi.get_book('Elective Affinities')
        assert book.author == 'Goethe'
        assert book.genre == 'Romanticism'
        num_books = len(DbApi.get_all_books())
        assert num_books == 1

    def test_book_db_api_three(self):
        DbApi.create_book(
            title='Plexus',
            author='Henry Miller',
            genre='Roman à clef'
        )

        book = DbApi.get_book('Plexus')
        assert book.author == 'Henry Miller'
        assert book.genre == 'Roman à clef'
        num_books = len(DbApi.get_all_books())
        assert num_books == 1
