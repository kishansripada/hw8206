# Your name: Kishan Sripada
# Your student id: 5212 0336
# Your email: kishansripada@gmail.com
# List who you have worked with on this homework:

import matplotlib.pyplot as plt
import os
import sqlite3
import unittest


def load_rest_data(db):
  conn = sqlite3.connect(db)
  cursor = conn.cursor()

  query = '''SELECT restaurants.name, categories.category, buildings.building, restaurants.rating
FROM restaurants
JOIN categories ON restaurants.category_id = categories.id
JOIN buildings ON restaurants.building_id = buildings.id
'''
  cursor.execute(query)
  data = cursor.fetchall()
  rest_data = {}

  for row in data:

    rest_data[row[0]] = {
      'category': row[1],
      'building': row[2],
      'rating': row[3]
    }

  conn.close()
  return rest_data


#Try calling your functions here
def main():
  # rest_data = load_rest_data('South_U_Restaurants.db')
  # print(rest_data)
  pass


class TestHW8(unittest.TestCase):

  def setUp(self):
    self.rest_dict = {'category': 'Cafe', 'building': 1101, 'rating': 3.8}
    self.cat_dict = {
      'Asian Cuisine ': 2,
      'Bar': 4,
      'Bubble Tea Shop': 2,
      'Cafe': 3,
      'Cookie Shop': 1,
      'Deli': 1,
      'Japanese Restaurant': 1,
      'Juice Shop': 1,
      'Korean Restaurant': 2,
      'Mediterranean Restaurant': 1,
      'Mexican Restaurant': 2,
      'Pizzeria': 2,
      'Sandwich Shop': 2,
      'Thai Restaurant': 1
    }
    self.highest_rating = [('Deli', 4.6), (1335, 4.8)]

  def test_load_rest_data(self):
    rest_data = load_rest_data('South_U_Restaurants.db')
    self.assertIsInstance(rest_data, dict)
    self.assertEqual(rest_data['M-36 Coffee Roasters Cafe'], self.rest_dict)
    self.assertEqual(len(rest_data), 25)

  def test_plot_rest_categories(self):
    cat_data = plot_rest_categories('South_U_Restaurants.db')
    self.assertIsInstance(cat_data, dict)
    self.assertEqual(cat_data, self.cat_dict)
    self.assertEqual(len(cat_data), 14)

  def test_find_rest_in_building(self):
    restaurant_list = find_rest_in_building(1140, 'South_U_Restaurants.db')
    self.assertIsInstance(restaurant_list, list)
    self.assertEqual(len(restaurant_list), 3)
    self.assertEqual(restaurant_list[0], 'BTB Burrito')

  def test_get_highest_rating(self):
    highest_rating = get_highest_rating('South_U_Restaurants.db')
    self.assertEqual(highest_rating, self.highest_rating)


if __name__ == '__main__':
  main()
  unittest.main(verbosity=2)
