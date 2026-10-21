from sqlalchemy import create_engine, text


db_connection_string = "ВАШИ_ДАННЫЕ"
db = create_engine(db_connection_string)


def test_insert_student():
    connection = db.connect()
    transaction = connection.begin()

    create_student = text(
        "INSERT INTO student("
        "\"user_id\", \"level\", \"education_form\", \"subject_id\") "
        "VALUES ("
        ":new_user_id, :new_level, :new_education_form, :new_subject_id)"
    )

    search_student = text(
        "SELECT \"user_id\" FROM student "
        "WHERE \"user_id\" = :new_user_id"
    )

    students = {
        "new_user_id": 95623,
        "new_level": "Beginner",
        "new_education_form": "personal",
        "new_subject_id": 1
    }

    connection.execute(create_student, students)
    search_result = connection.execute(search_student, students)
    student_id = search_result.scalar()

    assert student_id is not None

    delete_student = text(
        "DELETE FROM student WHERE user_id = :new_user_id"
    )
    connection.execute(delete_student, {"new_user_id": student_id})

    transaction.commit()
    connection.close()


def test_update_student():
    connection = db.connect()
    transaction = connection.begin()

    create_student = text(
        "INSERT INTO student("
        "\"user_id\", \"level\", \"education_form\", \"subject_id\") "
        "VALUES ("
        ":new_user_id, :new_level, :new_education_form, :new_subject_id)"
    )

    search_student = text(
        "SELECT \"user_id\" FROM student "
        "WHERE \"user_id\" = :new_user_id"
    )

    students = {
        "new_user_id": 96623,
        "new_level": "Upper-Intermediate",
        "new_education_form": "personal",
        "new_subject_id": 1
    }

    connection.execute(create_student, students)
    search_result = connection.execute(search_student, students)
    student_id = search_result.scalar()

    assert student_id is not None

    update_student = text(
        "UPDATE student SET level = :updated_level "
        "WHERE user_id = :new_user_id"
    )
    connection.execute(
        update_student, {
            "updated_level": 'Advanced', "new_user_id": student_id
        }
    )

    check_update = text(
        "SELECT \"level\" FROM student "
        "WHERE \"user_id\" = :new_user_id"
    )
    update_result = connection.execute(
        check_update, {"new_user_id": student_id}
    )
    update_level = update_result.scalar()

    assert update_level == "Advanced"

    delete_student = text(
        "DELETE FROM student WHERE user_id = :new_user_id"
    )
    connection.execute(delete_student, {"new_user_id": student_id})

    transaction.commit()
    connection.close()


def test_delete_student():
    connection = db.connect()
    transaction = connection.begin()

    create_student = text(
        "INSERT INTO student("
        "\"user_id\", \"level\", \"education_form\", \"subject_id\") "
        "VALUES ("
        ":new_user_id, :new_level, :new_education_form, :new_subject_id)"
    )

    search_student = text(
        "SELECT \"user_id\" FROM student "
        "WHERE \"user_id\" = :new_user_id"
    )

    students = {
        "new_user_id": 97234,
        "new_level": "Elementary",
        "new_education_form": "group",
        "new_subject_id": 1
    }

    connection.execute(create_student, students)
    search_result = connection.execute(search_student, students)
    student_id = search_result.scalar()

    assert student_id is not None

    delete_student = text(
        "DELETE FROM student WHERE user_id = :new_user_id"
    )
    connection.execute(delete_student, {"new_user_id": student_id})

    search_result = connection.execute(
        search_student, {"new_user_id": student_id}
    )
    student_id = search_result.scalar()

    assert student_id is None

    transaction.commit()
    connection.close()
