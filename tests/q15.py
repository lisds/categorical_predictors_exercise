test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmm, your function isn't returning the mean of the `wc` group
          >>> np.isclose(mixed_up_mean(intercept_lin_reg_type_OTHER_prest, slope_lin_reg_type_prest), prof_wc_df.groupby(by = 'type')['prestige'].agg('mean')['wc'], atol = 2)
          True

          """,
          'hidden': False,
          'locked': False
        },
                {
          'code': r"""
          >>> # Hey! It looks as though you tried to hard code you answer!
          >>> ~np.isclose(mixed_up_mean(10, 10), prof_wc_df.groupby(by = 'type')['prestige'].agg('mean')['wc'], atol = 2) 
          True

          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
