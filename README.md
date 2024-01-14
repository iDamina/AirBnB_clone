# AirBnB clone

This is the first stage of the project - AirBnB clone which is a project
that clones the original AirBnB website. At this stage, the implementation of
the backend interface or a console is developed that can be able to manage the program
data. The console commands like create, update and destroy objects as well as to manage
a file storage system.

---

### This Repository Contents by Project Tasks-

|   Tasks   |   Files    |    Description    |
| --------- | ---------- | ----------------- |
| 0. README, AUTHORS File | [AUTHORS](https://github.com/NinoZara/AirBnB_clone/blob/master/AUTHORS) | Authors page
| 1. Pycodestyle compliant using pep8 | No file for this | All codes are pycodestyle compliant
| 2. Unittests | [/tests](https://github.com/NinoZara/AirBnB_clone.git/) | all class-defining models are unit tested |
| 3. BaseModel | [/models/base_model.py]() | Defines the class model that all other models inherit from |
| 4. Create BaseModel from dictionary| [models/base_model.py](), [tests/]() | Re-creating an instance with the dictionary representation <class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'> |
| 5. Store first object | [models/engine/file_storage.py](), [models/engine/__init__.py](), [models/__init__.py](), [models/base_model.py](), [tests/]() | Re-creating the BaseModel from another one using a particular dictionary representation
| Console 0.0.1 | [console.py](https://github.com/NinoZara/AirBnB_clone/blob/master/console.py) | A program called console.py that contains the entry point of the command interpreter |
| 6. Console 0.1 | [console.py](https://github.com/NinoZara/AirBnB_clone/blob/master/console.py) | Updating the console interpreter to have Create, show, destroy, all and update |
| 7. First User | [models/user.py]() | A class user that inherits from BaseModel |
| 8. More classes! | [models/state.py](), [models/city.py](), [models/amenity.py](), [models/place.py]() and [models/review.py]() | All classes inhering from BaseModel |
| 9. Console 1.0 | [console.py](https://github.com/NinoZara/AirBnB_clone/blob/master/console.py) | Updating Filestrorage to manage correctly serialization and deserialization of all new classes Place, State, City, Amenity and Review |
