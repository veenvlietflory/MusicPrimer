# test_musicprimer.py
"""
Tests for MusicPrimer module.
"""

import unittest
from musicprimer import MusicPrimer

class TestMusicPrimer(unittest.TestCase):
    """Test cases for MusicPrimer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MusicPrimer()
        self.assertIsInstance(instance, MusicPrimer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MusicPrimer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
