test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # your dataframe is missing some columns!
          >>> all(pd.Series(prof_wc_df.columns).isin(['name', 'type', 'income', 'education', 'prestige'])) | all(pd.Series(prof_wc_df.columns).isin(['name', 'type', 'income', 'education', 'prestige', 'type_dummy']))
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It doesn't look like your dataframe contains the correct data!
          >>> (prof_wc_df['type'].value_counts()['prof'] == 18) & (sum(prof_wc_df['type'] == 'bc') == 0)
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
