def Statuses():
    assistances = [
        {
            'id': 1,
            'caseno': '001-01C0001',
            'dob': '1990-01-01',
            'phone': '01095550001',
            'details': [{
                'type': 'education',
                'individualid': '001-01C0001_01',
                'amount': 650,
                'collectioncenter': 'PO 001 Cairo',
                'collectiondate': '2019-06-30'
            },
                {
                'type': 'education',
                'individualid': '001-01C0001_02',
                'amount': 650,
                'collectioncenter': 'PO 001 Cairo',
                'collectiondate': '2019-06-30'
            },
                {
                'type': 'maternity',
                'individualid': '001-01C0001_03',
                'amount': 1000,
                'collectioncenter': 'PO 001 Cairo',
                'collectiondate': '2019-12-31'
            }]
        },
        {
            'id': 2,
            'caseno': '001-01C0002',
            'dob': '1990-02-02',
            'phone': '01095550002',
            'details': [{
                'type': 'education',
                'individualid': '001-01C0002_01',
                        'amount': 650,
                        'collectioncenter': 'PO 001 Cairo',
                'collectiondate': '2019-06-30'
            },
                {
                'type': 'maternity',
                'individualid': '001-01C0002_02',
                'amount': 1000,
                'collectioncenter': 'PO 001 Cairo',
                'collectiondate': '2019-12-31'
            }]
        },
        {
            'id': 3,
            'caseno': '001-01C0003',
            'dob': '1990-03-03',
            'phone': '01095550003',
            'details': [{
                'type': 'maternity',
                'individualid': '001-01C0003_01',
                        'amount': 1000,
                        'collectioncenter': 'PO 002 Alexandria',
                'collectiondate': '2019-12-31'
            },
                {
                'type': 'health',
                'individualid': '001-01C0002_02',
                'amount': 800,
                'collectioncenter': 'PO 001 Alexandria',
                'collectiondate': '2020-12-31'
            }]
        },

        {
            'id': 4,
            'caseno': '001-01C0004',
            'dob': '1990-04-04',
            'phone': '01095550004',
            'details': [{
                'type': 'food',
                'individualid': '001-01C0004_01',
                        'amount': 1200,
                        'collectioncenter': 'PO 010 Cairo',
                'collectiondate': '2020-12-31'
            }]
        }
    ]

    return assistances
