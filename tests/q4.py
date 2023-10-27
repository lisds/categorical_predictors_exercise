test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
                          {
          'code': r"""
          >>> # Hmmm you haven't created a `type_dummy` column, or it is named incorrectly.
          >>> 'type_dummy' in prof_wc_df.columns
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Your `type_dummy` column contains the wrong values.
          >>> all(prof_wc_df['type_dummy'].values == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
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
