test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your slope is the wrong value...
          >>> np.isclose(43.77, slope_lin_reg_type_prest, atol = 2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # your intercept is the wrong value...
          >>> np.isclose(36.66, intercept_lin_reg_type_prest, atol = 2)
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
