test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your function is not returning the mean of the `wc` group!
          >>> test_1 = np.isclose(get_wc_mean_from_params(slope_lin_reg_type_prest, intercept_lin_reg_type_prest), prof_wc_df[prof_wc_df['type'] == 'prof']['prestige'].mean(), atol = 2)
          >>> test_2 = np.isclose(get_wc_mean_from_params(intercept_lin_reg_type_prest, slope_lin_reg_type_prest), prof_wc_df[prof_wc_df['type'] == 'prof']['prestige'].mean(), atol = 2)
          >>> test_1 or test_2
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Hmm, it looks like you might have hard-coded the output of your function...
          >>> test_3 = np.isclose(get_wc_mean_from_params(10, 10), prof_wc_df[prof_wc_df['type'] == 'prof']['prestige'].mean(), atol = 2)
          >>> ~test_3
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
