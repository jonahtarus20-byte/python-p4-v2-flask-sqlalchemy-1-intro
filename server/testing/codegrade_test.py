
def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    from models import Pet
    assert Pet.__tablename__ == 'pets'
    assert hasattr(Pet, 'id')
    assert hasattr(Pet, 'name')
    assert hasattr(Pet, 'species')
