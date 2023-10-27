test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # It doesn't look like you've sorted your dataframe correctly!
          >>> all(prof_wc_df['type'].iloc[:6].values == ['wc', 'wc', 'wc', 'wc', 'wc', 'wc'])
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It doesn't look like you've sorted your dataframe correctly!
          >>> all(prof_wc_df['type'].iloc[-6:].values == ['prof', 'prof', 'prof', 'prof', 'prof', 'prof'])
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
