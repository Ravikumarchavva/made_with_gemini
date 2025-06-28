# Basic tests for made_with_gemini package


def test_import():
    """Test that the package can be imported."""
    from direct_api import renovation_agent

    assert renovation_agent is not None