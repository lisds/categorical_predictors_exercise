test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your slope (from minimzing the `sum_absolute_error` cost function) is the wrong value...
          >>> np.isclose(45.57, abs_slope_type_prest, atol = 2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # your intercept (from minimzing the `sum_absolute_error` cost function) is the wrong value...
          >>> np.isclose(38.59, abs_intercept_type_prest, atol = 2)
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
