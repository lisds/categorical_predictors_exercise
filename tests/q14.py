test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # the slope from the regression you just fitted is the wrong value...
          >>> np.isclose(-43.77, slope_lin_reg_type_OTHER_prest, atol = 2)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # the intercept from the regression you just fitted is the wrong value...
          >>> np.isclose(80.44, intercept_lin_reg_type_OTHER_prest, atol = 2)
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
