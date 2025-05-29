-- name: getSubjects :many
SELECT * FROM subjects;

-- name: getSubjectsByFaculty :many
SELECT * FROM subjects WHERE "facultyId"=$1;

-- name: getSubjectById :one
SELECT * FROM subjects WHERE "id"=$1;

-- name: getSubjectBySemester :many
SELECT * FROM subjects WHERE "semester"=$1;

-- name: getSubjectsByStage :many
SELECT * FROM subjects WHERE "stage"=$1;

-- name: getSubjectBySemesterFacultyStage :many
SELECT * FROM subjects WHERE "semester"=$1 AND "facultyId"=$2 AND "stage"=$3;

-- name: createSubject :one
INSERT INTO subjects ("name", "facultyId", "aisid", "stage", "semester", "aisCode")
VALUES ($1,$2,$3,$4,$5,$6)
RETURNING "id";

-- name: searchSubject :many
WITH search AS (
    SELECT to_tsquery('slovak', string_agg(lexeme || ':*', ' & ' order by positions)) AS query
    FROM unnest(to_tsvector('slovak', UNACCENT($1)))
)
SELECT subjects.*
FROM subjects, search
WHERE (subjects.search_vector @@ search.query);