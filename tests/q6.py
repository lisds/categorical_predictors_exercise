test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
                        {
          'code': r"""
          >>> # your `type_dummy` variable is not a numpy array!
          >>> type(type_dummy) == np.ndarray
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # your `type_dummy` array does not contain the correct values
          >>> all(type_dummy == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
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
