__author__ = ["jgyasu", "fkiraly"]

from pytorch_forecasting.utils._dependencies import (
    _get_installed_packages,
    _safe_import,
)


def test_import_present_module():
    """Test importing a dependency that is installed."""
    result = _safe_import("pandas")
    assert result is not None
    assert "pandas" in _get_installed_packages()


def test_import_missing_module():
    """Test importing a dependency that is not installed."""
    result = _safe_import("nonexistent_module")
    assert hasattr(result, "__name__")
    assert result.__name__ == "nonexistent_module"


def test_import_without_pkg_name():
    """Test importing a dependency with the same name as package name."""
    result = _safe_import("torch", pkg_name="torch")
    assert result is not None


def test_import_with_different_pkg_name_1():
    """Test importing a dependency with a different package name."""
    result = _safe_import("skbase", pkg_name="scikit-base")
    assert result is not None


def test_import_with_different_pkg_name_2():
    """Test importing another dependency with a different package name."""
    result = _safe_import("cv2", pkg_name="opencv-python")
    assert result is not None


def test_import_submodule():
    """Test importing a submodule."""
    result = _safe_import("torch.nn")
    assert result is not None


def test_import_class():
    """Test importing a class."""
    result = _safe_import("torch.nn.Linear")
    assert result is not None


def test_import_existing_object():
    """Test importing an existing object."""
    result = _safe_import("pandas.DataFrame")
    assert result is not None
    assert result.__name__ == "DataFrame"
    from pandas import DataFrame

    assert result is DataFrame


def test_multiple_inheritance_from_mock():
    """Test multiple inheritance from dynamic MagicMock."""
    Class1 = _safe_import("foobar.foo.FooBar")
    Class2 = _safe_import("barfoobar.BarFooBar")

    class NewClass(Class1, Class2):
        """This should not trigger an error.

        The class definition would trigger an error if multiple inheritance
        from Class1 and Class2 does not work, e.g., if it is simply
        identical to MagicMock.
        """

        pass
