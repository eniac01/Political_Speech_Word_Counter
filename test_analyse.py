import analyse


tools = analyse.AnalysisTools()
member = analyse.CompareMembers('party', 'db_test.sqlite')
indiv = analyse.IndividualMember('party', 'db_test.sqlite')


def test_clean_words():
    words = tools.clean_words('\n the and hello Greg <h1>')
    assert words == ['hello', 'Greg']
    
    
def test_frequency():
    freq = tools.frequency(['alone', 'alone', 'all', 'all', 'alone', 
                                'alone', 'on', 'a', 'wide', 'wide', 'sea'])
    assert freq == {'alone': 4, 'all': 2, 'on': 1, 'a': 1, 'wide': 2, 'sea': 1}
    
    
def test_top_n_words():
    top = tools.top_n_words({'people': 574,'got': 175, 'want': 346, 'I': 1072, 
                                'country': 249, 'need': 241, 'make': 235, 'know': 200,
                                'new': 198, 'government': 190}, 5)
    assert top == {'I': 1072, 'people': 574, 'want': 346, 'country': 249, 'need': 241}
    

def test_word_match_count():
    count = member.word_match_count(['a', 'b', 'c', 'd', 'e'], ['a','b', 'c', 'g', 'h'])
    assert count == 3


def test_comparison():
    results = member.comparison(3)
    assert results == {'Conservative / Labour': 2, 'Conservative / Liberal': 1, 
                        'Conservative / SDP-Liberal Alliance': 1, 
                        'Conservative / Liberal Democrat': 2, 'Labour / Liberal': 1, 
                        'Labour / SDP-Liberal Alliance': 1, 'Labour / Liberal Democrat': 2, 
                        'Liberal / SDP-Liberal Alliance': 1, 'Liberal / Liberal Democrat': 2, 
                        'SDP-Liberal Alliance / Liberal Democrat': 1}


def test_top_n_for_member():
    results = indiv.top_n_for_member('Labour', 3)
    assert results == {'I': 5241, 'people': 2181, 'new': 1540}