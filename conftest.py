from fixture.application import Application
import pytest
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
target = None
orm_fixture = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = jsonpickle.decode(f.read())
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--config"))["web"]
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture
def db(request):
    db_config = load_config(request.config.getoption("--config"))["db"]
    db_fixture = DbFixture(host=db_config["host"], db_name=db_config["name"], user=db_config["user"],
                           password=db_config["password"])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture
def orm(request):
    global orm_fixture
    db_config = load_config(request.config.getoption("--config"))["db"]
    if orm_fixture is None:
        orm_fixture = ORMFixture(host=db_config["host"], db_name=db_config["name"], user=db_config["user"],
                                 password=db_config["password"])

    #def fin():
    #    db_fixture.destroy()

    #request.addfinalizer(fin)

    return orm_fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):

    def fin():
        if fixture is not None:
            fixture.session.ensure_logout()
            fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--config", action="store", default="config.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(filename):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % filename), encoding="utf-8") as f:
        return jsonpickle.decode(f.read())
