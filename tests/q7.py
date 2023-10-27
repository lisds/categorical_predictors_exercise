test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
              {
          'code': r"""
          >>> # your `prestige` variable is not a numpy array!
          >>> type(prestige) == np.ndarray
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # your `prestige` array does not contain the correct values!
          >>> all(prestige == [16, 41, 34, 39, 52, 38, 59, 92, 45, 81, 76, 73, 82, 83, 89, 57, 88, 90, 93, 87, 90, 76, 90, 97])
          True

          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
