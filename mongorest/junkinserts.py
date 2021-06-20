insert_statement = """
            insert into todo(project, task, description) values
            ('project 1', 'task1', 'description1'),
            ('project 1', 'task2', 'description2'),
            ('project 1', 'task3', 'description3'),
            ('project 1', 'task4', 'description4'),
            ('project 2', 'task1', 'description1'),
            ('project 2', 'task2', 'description1'),
            ('project 2', 'spisof', 'description1'),
            ('project 2', 'asdsf', 'description1'),
            ('project 2', 'okay', 'description1'),
            ('project 3', 'task1', 'description1'),
            ('project 3', 'task1654', 'description1'),
            ('project 4', 'do something', 'description1'),
            ('project 5', 'task1', 'big sl sleks aseofpiase ase;lkfase ;lasm;elfkas;lk efma;sleewlfk we oiutherio krtjkler t ewrthjer;lk ewlr;kgj eroigjaher gvlkrdjgh dr'),
            ('project 6', 'task1', 'this sie a ske asddfkjasen ase aseuisaeiu fasek afsjuasefiu asefiul asefiuahgse fja,sefhb akjsehf '),
            ('project 7', 'task1', 'description1')
    """


mongo_insertions = [
    {
        "project": "project 1",
        "task": "task1",
        "description": "description1",
    },
    {
        "project": "project 1",
        "task": "task2",
        "description": "description2",
    },
    {
        "project": "project 1",
        "task": "task3",
        "description": "description3",
    },
    {
        "project": "project 1",
        "task": "task4",
        "description": "description4",
    },
    {
        "project": "project 2",
        "task": "task1",
        "description": "description1",
    },
    {
        "project": "project 2",
        "task": "task2",
        "description": "description1",
    },
    {
        "project": "project 2",
        "task": "spisof",
        "description": "description1",
    },
    {
        "project": "project 2",
        "task": "asdsf",
        "description": "description1",
    },
    {"project": "project 2", "task": "okay", "description": "description1"},
    {
        "project": "project 3",
        "task": "task1",
        "description": "description1",
    },
    {
        "project": "project 3",
        "task": "task1654",
        "description": "description1",
    },
    {
        "project": "project 4",
        "task": "do something",
        "description": "description1",
    },
    {
        "project": "project 5",
        "task": "task1",
        "description": "big sl sleks aseofpiase ase;lkfase ;lasm;elfkas;lk efma;sleewlfk we oiutherio krtjkler t ewrthjer;lk ewlr;kgj eroigjah  gvlkrdjgh dr",
    },
    {
        "project": "project 6",
        "task": "task1",
        "description": "this sie a ske asddfkjasen ase aseuisaeiu fasek afsjuasefiu asefiul asefiuahgse fjaefhb akjsehf ",
    },
    {
        "project": "project 7",
        "task": "task1",
        "description": "description1",
    },
]
