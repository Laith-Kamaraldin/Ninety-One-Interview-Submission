import unittest
from unittest.mock import patch, mock_open
from get_top_scorers import load_file, parse_file, find_top_scorers


class TestGetTopScorers(unittest.TestCase):

    def setUp(self):
        self.sample_csv = (
            "first_name,second_name,score\n"
            "Person,One,56\n"
            "Person,Two,78\n"
            "Person,Three,64\n"
            "Person,Four,78\n"
            "Person,Five,80\n"
            "Person,Six,91\n"
            "Person,Seven,81\n"
            "Person,Eight,91\n"
            "Person,Nine,75\n"
            "Person,Ten,62\n"
        ).strip()

        self.parsed_data = [
            ('Person One', 56),
            ('Person Two', 78),
            ('Person Three', 64),
            ('Person Four', 78),
            ('Person Five', 80),
            ('Person Six', 91),
            ('Person Seven', 81),
            ('Person Eight', 91),
            ('Person Nine', 75),
            ('Person Ten', 62)
        ]

    def test_load_file(self):
        m = mock_open(read_data=self.sample_csv)
        with patch("get_top_scorers.open", m, create=True):
            data = load_file("dummy_file_path")
        self.assertEqual(data, self.sample_csv)

    def test_load_file_not_found(self):
        with self.assertRaises(FileNotFoundError) as context:
            load_file("non_existent_file_path")
        self.assertEqual(
            str(context.exception), "The specified file could not be found."
        )

    def test_parse_file(self):
        result = parse_file(self.sample_csv)
        print(result)
        self.assertEqual(result, self.parsed_data)

    def test_find_top_scorers(self):
        top_score, top_scorers = find_top_scorers(self.parsed_data)
        print(top_score, top_scorers)
        self.assertEqual(top_score, 91)
        self.assertCountEqual(top_scorers, ["Person Six", "Person Eight"])


if __name__ == "__main__":
    unittest.main()
