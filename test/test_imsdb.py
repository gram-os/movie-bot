import unittest
from src import imsdb_fetch

class TestMovieFetchingcd(unittest.TestCase):
    def fetchMovieTitlesSucceeds(self):
        """Test that we can fetch movies successfully"""
        
        movieTitles = imsdb_fetch.fetchMovieTitles()
        self.assertIsNotNone(movieTitles)
    
    def fetchMovieTitlesFailsRaisesException(self):
        """Tests that when no movie titles are returned, we raise an exception"""
        
        movieTitles = imsdb_fetch.fetchMovieTitles()
        self.assertRaises(imsdb_fetch.MoviesNotFoundException)
    
    def fetchRandomMovieTitleSucceeds(self):
        """Ensure we get a single title"""
        
        movieTitle = imsdb_fetch.pickRandomMovie()
        self.assertIsNotNone(movieTitle)
    
    def fetchMovieScriptSucceeds(self):
        """Ensure we get script successfully"""
        
        script = imsdb_fetch.getMovieScript()
        self.assertIsNotNone(script)
        
    def fetchMovieScriptFails(self):
        """Ensure we raise exception"""
        
        script = imsdb_fetch.getMovieScript("fdafkldsafj")
        self.assertRaises(imsdb_fetch.ScriptNotFoundException)

if __name__ == '__main__':
    unittest.main()