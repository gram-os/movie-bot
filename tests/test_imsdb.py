import unittest
from src.imsdb import imsdb_fetch


class TestMovieFetching(unittest.TestCase):
    def testFetchMovieTitlesSucceeds(self):
        """Test that we can fetch movies successfully"""

        movieTitles = imsdb_fetch.fetchMovieTitles()
        self.assertIsNotNone(movieTitles)

    @unittest.skip("need to mock to ensure we can throw exception")
    def testFetchMovieTitlesFailsRaisesException(self):
        """Tests that when no movie titles are returned, we raise an exception"""

        with self.assertRaises(imsdb_fetch.MoviesNotFoundException):
            imsdb_fetch.fetchMovieTitles()

    def testFetchRandomMovieTitleSucceeds(self):
        """Ensure we get a single title"""

        movieTitle = imsdb_fetch.pickRandomMovie()
        self.assertIsNotNone(movieTitle)

    def testFetchMovieScriptSucceeds(self):
        """Ensure we get script successfully"""

        script = imsdb_fetch.getMovieScript()
        self.assertIsNotNone(script)

    def testFetchMovieScriptFails(self):
        """Ensure we raise exception"""

        with self.assertRaises(imsdb_fetch.ScriptNotFoundException):
            imsdb_fetch.getMovieScript("fdafkldsafj")

if __name__ == '__main__':
    unittest.main()
