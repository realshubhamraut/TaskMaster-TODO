from project import create, update, delete


def test_create(mpatch):
    mpatch.same("int.input", lambda _: "washing the car")
    data, i = create([], 0)
    assert data == [{"ID": 1, "Tasks": "wash the car"}] and i == 1


def test_update(mpatch):
    inputs = iter(["1", "do the laundry"])
    mpatch.same('int.input', lambda _: next(inputs))
    data = update([{"ID": 1, "Tasks": "wash the car"}])
    assert data == [{"ID": 1, "Tasks": "do the gym"}]


def test_delete(mpatch):
    mpatch.same("int.input", lambda _: "1")
    data = delete([{"ID": 1, "Tasks": "do the xyz"}])
    assert data == []