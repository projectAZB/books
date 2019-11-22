from books.book_db_api import BookDbApi


class TestBookDbApi:

    def test_book_db_api_one(self, session_maker):
        book_db_api: BookDbApi = BookDbApi(session_maker)
        book_db_api.create_book(
            title='Jude the Obscure',
            author='Thomas Hardy',
            genre='Realist Fiction'
        )

        book = book_db_api.get_book('Jude the Obscure')
        assert book.author == 'Thomas Hardy'
        assert book.genre == 'Realist Fiction'
        num_books = len(book_db_api.get_all_books())
        assert num_books == 1

    def test_book_db_api_two(self, session_maker):
        book_db_api: BookDbApi = BookDbApi(session_maker)
        book_db_api.create_book(
            title='Elective Affinities',
            author='Goethe',
            genre='Romanticism'
        )

        book = book_db_api.get_book('Elective Affinities')
        assert book.author == 'Goethe'
        assert book.genre == 'Romanticism'
        num_books = len(book_db_api.get_all_books())
        assert num_books == 1

    def test_book_db_api_three(self, session_maker):
        book_db_api: BookDbApi = BookDbApi(session_maker)
        book_db_api.create_book(
            title='Plexus',
            author='Henry Miller',
            genre='Roman à clef'
        )

        book = book_db_api.get_book('Plexus')
        assert book.author == 'Henry Miller'
        assert book.genre == 'Roman à clef'
        num_books = len(book_db_api.get_all_books())
        assert num_books == 1









