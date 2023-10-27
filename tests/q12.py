test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
                          {
          'code': r"""
          >>> # It looks like your `type_dummy_other` variable is not a numpy array
          >>> type(type_dummy_other) == np.ndarray
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # It looks like your `type_dummy_other` array contains the wrong values!
          >>> all(type_dummy_other == [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
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
