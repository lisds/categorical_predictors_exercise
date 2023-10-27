test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
         {
          'code': r"""
          >>> # Hmmm, your function isn't returning the correct value! (This might be becuase it returning an array or series rather than a single value).
          >>> np.isclose(intercept_another_way(q10_df), 36.66, atol = 2)
          True
          """,
          'hidden': False,
          'locked': False
        },
      
                {
          'code': r"""
          >>> # Hmmm, it looks like you tried to pass this question by hard coding the output of your `intercept_another_way` function!
          >>> temp_q10_df = q10_df.copy()
          >>> temp_q10_df['prestige'] = np.random.normal(100, 10, len(temp_q10_df))
          >>> ~np.isclose(intercept_another_way(temp_q10_df), 36.66, atol = 2)
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
