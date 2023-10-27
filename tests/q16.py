test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
                                    {
          'code': r"""
          >>> # Hmmm it looks like you haven't defined a function called `sum_absolute_error`
          >>> "sum_absolute_error" in dir()
          True

          """,
          'hidden': False,
          'locked': False
        },
                          {
          'code': r"""
          >>> # Your `sum_absolute_error` function isn't returning the correct values...
          >>> np.isclose(sum_absolute_error([1, 1], prof_wc_df['type_dummy'], prof_wc_df['prestige']), 1626)
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
