import pytest
from http import HTTPStatus
from clients.exercises.exercises_client import ExercisesClient, CreateExerciseRequestSchema
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from clients.exercises.exercises_schema import (
    CreateExerciseResponseSchema, 
    GetExerciseResponseSchema, 
    UpdateExerciseResponseSchema, 
    UpdateExerciseRequestSchema
)
from tools.assertions.exercises import (
assert_create_exercise_response, 
assert_get_exercise_response, 
assert_update_exercise_response
)
from tools.assertions.schema import validate_json_schema
from fixtures.exercises import ExerciseFixture



@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self,
        exercises_client: ExercisesClient,
        function_course: CourseFixture,
    ):

        request = CreateExerciseRequestSchema(course_id=function_course.response.course.id)
        
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(
            response.text
        )
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)
        validate_json_schema(
            response.json(), response_data.model_json_schema()
        )



    def test_get_exercise(self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture
    ):
       response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
       response_data = GetExerciseResponseSchema.model_validate_json(
           response.text
       )
       assert_status_code(response.status_code, HTTPStatus.OK)
       assert_get_exercise_response(response_data, function_exercise.response)
       
       validate_json_schema(
           response.json(), response_data.model_json_schema()
       )

    def test_update_exercise(self,
        exercises_client: ExercisesClient,
        function_exercise: ExerciseFixture,
        function_course: CourseFixture
    ):
        request = UpdateExerciseRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_data = UpdateExerciseResponseSchema.model_validate_json(
            response.text
        )
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)
        validate_json_schema(
            response.json(), response_data.model_json_schema()
        )